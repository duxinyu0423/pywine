import os
import os
import subprocess
import webbrowser
from threading import Thread

from PyQt5.Qt import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog

from ui.mainui import Ui_MainWindow
from .log import logger, string_stream, log_path


class Pywine(QMainWindow, Ui_MainWindow):
    str_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Pywine, self).__init__(parent)
        # 基本变量
        self.sudo_password = ""  # 记录密码
        self.root_path = os.path.abspath(os.getcwd())  # 记录当前工作目录
        self.file_path = self.root_path
        # 启动UI
        self.setupUi(self)
        self.setWindowTitle('Pywine')
        self.logolabel.setPixmap(QPixmap("./source/ncepu.png"))
        # 加载日志配置
        self.logger = logger
        self.string_stream = string_stream
        self.log_info("Logging started.")
        self.log_info("log_path: {}".format(log_path))
        self.log_info("pwd: " + self.root_path)
        # 配置右侧命令行
        # self.bash = BashShell(string_stream)
        # self.bash.str_signal.connect(self.update_bash_shell)
        # self.bash.start()
        self.str_signal.connect(self.log_info)
        self.connect_action_all()
        self.log_info("Pywine started.")
        # 固定UI大小
        self.setFixedSize(873, 531)
        # 显示UI
        self.show()

    def connect_action_all(self) -> None:
        """
        Connect action all
        :return:
        """
        self.passwordButton.clicked.connect(self.verify_sudo_password)
        self.wineinstallaction.triggered.connect(self.wineinstall_action)
        self.winesetaction.triggered.connect(self.wineset_action)
        self.winerestartaction.triggered.connect(self.winerestart_action)
        self.wineuninstaller.triggered.connect(self.wineuninstall_action)
        self.purgewine.triggered.connect(self.purgewine_action)
        self.document.triggered.connect(self.document_action)
        self.luanma.triggered.connect(self.luan_action)  # 没有乱码问题
        self.Introduction.triggered.connect(self.introduction_action)
        self.fileopenAction.triggered.connect(self.file_action)
        self.setexepath_button.clicked.connect(self.file_action)
        self.installbutton.clicked.connect(self.install_action)
        self.othertools.triggered.connect(self.othertools_action)
        self.wechat.triggered.connect(lambda: self.install_action_web(
            "https://dldir1v6.qq.com/weixin/Windows/WeChatSetup_x86.exe",
            None))
        self.QQ.triggered.connect(lambda: self.install_action_web(
            "https://dldir1.qq.com/qqfile/qq/QQNT/Windows/QQ_9.9.9_240412_x86_01.exe",
            None))
        self.kugou.triggered.connect(lambda: self.install_action_web(
            "https://downmini.yun.kugou.com/web/kugou_10250.exe",
            None))
        self.wangyi.triggered.connect(lambda: self.install_action_web(
            "https://d1.music.126.net/dmusic/NeteaseCloudMusic_Music_official_3.0.0.Beta.03.25.202691.32.exe",
            None))
        self.action7_Zip.triggered.connect(lambda: self.install_action_web(
            "https://www.7-zip.org/a/7z2301-x64.exe",
            None))
        self.qqmusic_2.triggered.connect(lambda: self.install_action_web(
            "https://dldir1.qq.com/music/clntupate/linux/deb/qqmusic_1.1.5_amd64_.deb",
            None))
        self.dingding.triggered.connect(lambda: self.install_action_web(
            "https://dtapp-pub.dingtalk.com/dingtalk-desktop/xc_dingtalk_update/linux_deb/Release/com.alibabainc.dingtalk_7.5.10.404071_amd64.deb",
            None))
        self.tengxunmeeting.triggered.connect(lambda: self.install_action_web(
            "https://updatecdn.meeting.qq.com/cos/fcdc2a010a25561a4d23e168b677b493/TencentMeeting_0300000000_3.19.1.400_x86_64_default.publish.deb",
            None))


    def install_action_web(self, url: str, name: str = None) -> None:
        if self.is_password_valid() is False:
            return
        self.log_info("wine install {}".format(url.split("/")[-1]))
        thread = Thread(target=self.install_exe_func, args=(url, True, name))
        thread.start()

    def install_action(self) -> None:
        if self.is_password_valid() is False:
            return
        self.log_info("wine install {}".format(self.file_path))
        thread = Thread(target=self.install_exe_func, args=(self.file_path, False))
        thread.start()

    def install_exe_func(self, file_path: str, is_web_url: bool = False, name: str = None) -> None:
        """
        该函数可以从本地路径或者网络中下载，并安装exe文件或者deb文件到linux系统中
        :param name: 文件名称，如果为空，自动生成
        :param file_path: 当是web网页时该变量是网站下载地址，否则是文件地址
        :param is_web_url: 是否是网站下载地址
        :return:
        """
        if name is None:
            name = file_path.split("/")[-1]
        if name.endswith(".deb"):  # 部分软件支持Linux版本
            self.str_signal.emit("start download from {}".format(file_path))
            ret = subprocess.run("wget -nc -O source/app/{} {}".format(name, file_path), shell=True,
                                 stdout=subprocess.PIPE)
            ret = subprocess.run("echo {} | sudo -S dpkg -i source/app/{}".format(self.sudo_password, name), shell=True,
                                 stdout=subprocess.PIPE)
            self.str_signal.emit(ret.stdout.decode("utf-8"))
            self.str_signal.emit("{} 安装完成，请在桌面打开".format(name))
            return

        if not is_web_url:
            ret = subprocess.run("wine {}".format(file_path), shell=True, stdout=subprocess.PIPE)
            self.str_signal.emit(ret.stdout.decode("utf-8"))
        else:
            self.str_signal.emit("start download from {}".format(file_path))
            ret = subprocess.run("wget -nc -O source/app/{} {}".format(name, file_path), shell=True,
                                 stdout=subprocess.PIPE)
            self.str_signal.emit(ret.stdout.decode("utf-8"))
            ret = subprocess.run("wine source/app/{}".format(name), shell=True, stdout=subprocess.PIPE)
            self.str_signal.emit(ret.stdout.decode("utf-8"))
        self.str_signal.emit("wine install finished.")

    def file_action(self) -> None:
        fileDlg = QFileDialog()
        fileDlg.setDirectory(self.file_path)
        if fileDlg.exec_():
            self.file_path = fileDlg.selectedFiles()[0]
            # self.log_info(self.root_path[])
            self.log_info("file_path: {}".format(self.file_path))
            if not self.file_path.endswith(".exe"):
                QMessageBox.information(self, "错误", "请选择EXE文件")

    def introduction_action(self) -> None:
        self.log_info("introduction started.")
        QMessageBox.information(self, "软件介绍", "这是一个基于wine项目,可以在linux系统上运行Windows程序的图形化软件")

    def luan_action(self) -> None:
        self.log_info("Luanma Fix started.")
        thread = Thread(target=self.luan_func, args=())
        thread.start()

    def luan_func(self) -> None:
        ret = subprocess.run("cp source/fonts/* ~/.wine/drive_c/windows/Fonts/", shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        self.str_signal.emit("Luanma Fix finished.")

    def document_action(self) -> None:
        self.log_info("wine document start.")
        thread = Thread(target=self.document_func, args=())
        thread.start()

    def document_func(self) -> None:
        webbrowser.open("https://www.winehq.org/help")

    def purgewine_action(self) -> None:
        if self.is_password_valid() is False:
            return
        self.log_info("purge wine start.")
        thread = Thread(target=self.purgewine_func, args=())
        thread.start()

    def purgewine_func(self) -> None:
        ret = subprocess.run("echo %s | sudo -S apt purge wine* -y" % self.sudo_password, shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        ret = subprocess.run("echo %s | sudo -S rm -rf ~/.wine" % self.sudo_password, shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        ret = subprocess.run("echo %s | sudo -S apt autoremove -y" % self.sudo_password, shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        ret = subprocess.run("echo %s | sudo -S rm -r ~/.local/share/applications" % self.sudo_password, shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        ret = subprocess.run("echo %s | sudo -S rm -r ~/.config/menus/applications-merged/wine*" % self.sudo_password,
                             shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        self.str_signal.emit("purge wine done.")

    def wineuninstall_action(self) -> None:
        self.log_info("wineinstaller started.")
        thread = Thread(target=self.wineuninstall_func, args=())
        thread.start()

    def wineuninstall_func(self) -> None:
        ret = subprocess.run("wine uninstaller", shell=True, stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        self.str_signal.emit("wineinstaller killed.")

    def winerestart_action(self) -> None:
        self.log_info("wine restart.")
        thread = Thread(target=self.winerestart_func, args=())
        thread.start()

    def winerestart_func(self) -> None:
        ret = subprocess.run("wineboot", shell=True, stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))

    def wineset_action(self) -> None:
        self.log_info("winecfg started.")
        thread = Thread(target=self.wineset_func, args=())
        thread.start()

    def wineset_func(self) -> None:
        self.str_signal.emit("安装wine-mono-9.0.0-x86.msi")
        ret = subprocess.run("wget -nc -O source/msi/wine-mono-9.0.0-x86.msi "
                             "https://mirrors.ustc.edu.cn/wine/wine/wine-mono/9.0.0/wine-mono-9.0.0-x86.msi",
                             shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        ret = subprocess.run("wine start /i source/msi/wine-mono-9.0.0-x86.msi", shell=True,
                             stdout=subprocess.PIPE)
        # self.str_signal.emit(ret.stdout.decode("utf-8"))
        self.str_signal.emit("安装wine-gecko-2.47.4-x86.msi")
        ret = subprocess.run("wget -nc -O source/msi/wine-gecko-2.47.4-x86.msi "
                             "https://mirrors.ustc.edu.cn/wine/wine/wine-gecko/2.47.4/wine-gecko-2.47.4-x86.msi",
                             shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        ret = subprocess.run("wine start /i source/msi/wine-gecko-2.47.4-x86.msi", shell=True,
                             stdout=subprocess.PIPE)
        # self.str_signal.emit(ret.stdout.decode("utf-8"))

        self.str_signal.emit("安装wine-gecko-2.47.4-x86_64.msi")
        ret = subprocess.run("wget -nc -O source/msi/wine-gecko-2.47.4-x86_64.msi "
                             "http://mirrors.ustc.edu.cn/wine/wine/wine-gecko/2.47.4/wine-gecko-2.47.4-x86_64.msi",
                             shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        ret = subprocess.run("wine start /i source/msi/wine-gecko-2.47.4-x86_64.msi", shell=True,
                             stdout=subprocess.PIPE)
        # self.str_signal.emit(ret.stdout.decode("utf-8"))

        ret = subprocess.run("winecfg", shell=True, stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        self.str_signal.emit("winecfg killed.")

    def wineinstall_action(self) -> None:
        if self.is_password_valid() is False:
            return
        thread = Thread(target=self.wineinstall_func)
        thread.start()

    def wineinstall_func(self) -> None:
        self.str_signal.emit("正在添加 32 位架构支持")
        ret = subprocess.run("echo %s | sudo -S dpkg --add-architecture i386" % self.sudo_password, shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))

        ret = subprocess.run("echo %s | sudo -S mkdir -pm755 /etc/apt/keyrings" % self.sudo_password, shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))

        ret = subprocess.run(
            "echo %s | sudo -S cp source/winehq.key /etc/apt/keyrings/winehq-archive.key" % self.sudo_password,
            shell=True,
            stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        self.str_signal.emit("秘钥导入完成")

        ret = subprocess.run("echo %s | sudo -S echo \"deb [arch=amd64,i386 "
                             "signed-by=/usr/share/keyrings/winehq-archive.key] "
                             "https://mirrors.tuna.tsinghua.edu.cn/wine-builds/ubuntu/ focal main\" "
                             "> /etc/apt/sources.list.d/winehq.list" %
                             self.sudo_password, shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        self.str_signal.emit("软件源配置完成")

        ret = subprocess.run("echo %s | sudo -S apt update" % self.sudo_password, shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        self.str_signal.emit("软件列表更新完成")

        ret = subprocess.run("echo %s | sudo -S apt install --install-recommends winehq-stable -y" % self.sudo_password,
                             shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        self.str_signal.emit("wine安装完成")

        ret = subprocess.run("echo %s | sudo -S apt install winetricks -y" % self.sudo_password, shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        self.str_signal.emit("winetricks安装完成")
        self.str_signal.emit("全部安装完成")

    def othertools_action(self):
        self.log_info("start othertools")
        thread = Thread(target=self.othertools_func)
        thread.start()

    def othertools_func(self) -> None:
        ret = subprocess.run("winetricks", shell=True,
                             stdout=subprocess.PIPE)
        self.str_signal.emit(ret.stdout.decode("utf-8"))
        self.log_info("othertools stop")

    def verify_sudo_password(self):
        """
        使用 sudoers 文件验证提供的 sudo 密码是否正确。
        Returns:
            如果密码正确，则返回 True；否则，返回 False。
        """
        password = self.passwordEdit.text()
        # 使用 subprocess.run 执行 sudo 命令, 通过运行结果判断密码是否正确
        try:
            subprocess.run('echo %s | sudo -S /bin/true ' % password, check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
            self.log_info("sudo password is ok.")
            self.sudo_password = password
        except subprocess.CalledProcessError:
            self.sudo_password = ""
            self.log_info("sudo password is wrong.")
        self.is_password_valid()

    def is_password_valid(self) -> bool:
        if self.sudo_password == "":
            QMessageBox.information(self, "提示", "请输入正确的sudo密码！")
            self.log_info("sudo password is wrong.")
            return False
        return True

    def log_info(self, msg: str) -> None:
        """
        记录日志
        :param msg: 日志消息类型
        :return:
        """
        self.logger.info(msg)
        self.string_stream.seek(0)
        tmp_str = self.string_stream.read()
        self.string_stream.seek(0)
        self.string_stream.truncate(0)
        # 空字符串不更新
        if tmp_str == "" or tmp_str is None or tmp_str == "\n" or tmp_str.endswith("==> \n"):
            return
        # 替换结尾的换行符
        tmp_str = tmp_str[:-1] if tmp_str.endswith("\n") else tmp_str
        self.update_bash_shell(tmp_str)

    def update_bash_shell(self, bash_str: str) -> None:
        """
        更新右侧bash shell内容
        :param bash_str:
        :return:
        """
        # logger.debug(bash_str)
        self.bashbrowser.append(bash_str)

# class BashShell(QThread):
#     str_signal = pyqtSignal(str)
#
#     def __init__(self, buffer_string_io: io.StringIO):
#         super().__init__()
#         self.buffer_string_io = buffer_string_io
#
#     def run(self):
#         while True:
#             self.buffer_string_io.seek(0)
#             tmp_str = self.buffer_string_io.read()
#             # 空字符串不更新
#             if tmp_str == "" or tmp_str is None:
#                 continue
#             self.str_signal.emit(tmp_str)
#             self.buffer_string_io.seek(0)
#             self.buffer_string_io.truncate(0)
#             sleep(0.02)
