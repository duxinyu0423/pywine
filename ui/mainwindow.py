# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(746, 411)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(370, 10, 20, 341))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 11, 341, 341))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Buttonchoose = QtWidgets.QPushButton(self.widget)
        self.Buttonchoose.setObjectName("Buttonchoose")
        self.verticalLayout.addWidget(self.Buttonchoose)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(410, 10, 321, 341))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelpicture = QtWidgets.QLabel(self.widget1)
        self.labelpicture.setTextFormat(QtCore.Qt.AutoText)
        self.labelpicture.setAlignment(QtCore.Qt.AlignCenter)
        self.labelpicture.setObjectName("labelpicture")
        self.verticalLayout_2.addWidget(self.labelpicture)
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.Buttonrun = QtWidgets.QPushButton(self.widget1)
        self.Buttonrun.setObjectName("Buttonrun")
        self.verticalLayout_2.addWidget(self.Buttonrun)
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 746, 23))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menusoft = QtWidgets.QMenu(self.menubar)
        self.menusoft.setObjectName("menusoft")
        self.menubangongruanjian = QtWidgets.QMenu(self.menusoft)
        self.menubangongruanjian.setObjectName("menubangongruanjian")
        self.menu = QtWidgets.QMenu(self.menusoft)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menusoft)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menusoft)
        self.menu_3.setObjectName("menu_3")
        self.menuMusic = QtWidgets.QMenu(self.menusoft)
        self.menuMusic.setObjectName("menuMusic")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.menufixer = QtWidgets.QMenu(self.menubar)
        self.menufixer.setObjectName("menufixer")
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)
        self.actionChoose = QtWidgets.QAction(MainWindow1)
        self.actionChoose.setObjectName("actionChoose")
        self.actionQQ = QtWidgets.QAction(MainWindow1)
        self.actionQQ.setObjectName("actionQQ")
        self.actionWeChat = QtWidgets.QAction(MainWindow1)
        self.actionWeChat.setObjectName("actionWeChat")
        self.actionWPS = QtWidgets.QAction(MainWindow1)
        self.actionWPS.setObjectName("actionWPS")
        self.actionWeChat_2 = QtWidgets.QAction(MainWindow1)
        self.actionWeChat_2.setObjectName("actionWeChat_2")
        self.actionWPS_2 = QtWidgets.QAction(MainWindow1)
        self.actionWPS_2.setObjectName("actionWPS_2")
        self.actionzh = QtWidgets.QAction(MainWindow1)
        self.actionzh.setObjectName("actionzh")
        self.actioncfg = QtWidgets.QAction(MainWindow1)
        self.actioncfg.setObjectName("actioncfg")
        self.actiontxt = QtWidgets.QAction(MainWindow1)
        self.actiontxt.setObjectName("actiontxt")
        self.actiondelete = QtWidgets.QAction(MainWindow1)
        self.actiondelete.setObjectName("actiondelete")
        self.actionreboot = QtWidgets.QAction(MainWindow1)
        self.actionreboot.setObjectName("actionreboot")
        self.actionTencentMeeting = QtWidgets.QAction(MainWindow1)
        self.actionTencentMeeting.setObjectName("actionTencentMeeting")
        self.actionsteam = QtWidgets.QAction(MainWindow1)
        self.actionsteam.setObjectName("actionsteam")
        self.actionDingDing = QtWidgets.QAction(MainWindow1)
        self.actionDingDing.setObjectName("actionDingDing")
        self.actionQQGame = QtWidgets.QAction(MainWindow1)
        self.actionQQGame.setObjectName("actionQQGame")
        self.actionWeGame = QtWidgets.QAction(MainWindow1)
        self.actionWeGame.setObjectName("actionWeGame")
        self.actionTencentVedio = QtWidgets.QAction(MainWindow1)
        self.actionTencentVedio.setObjectName("actionTencentVedio")
        self.actionAiqiyiVedio = QtWidgets.QAction(MainWindow1)
        self.actionAiqiyiVedio.setObjectName("actionAiqiyiVedio")
        self.actionQQMusic = QtWidgets.QAction(MainWindow1)
        self.actionQQMusic.setObjectName("actionQQMusic")
        self.actionCloudMusic = QtWidgets.QAction(MainWindow1)
        self.actionCloudMusic.setObjectName("actionCloudMusic")
        self.actionfoobar2000 = QtWidgets.QAction(MainWindow1)
        self.actionfoobar2000.setObjectName("actionfoobar2000")
        self.actionwineinstall = QtWidgets.QAction(MainWindow1)
        self.actionwineinstall.setObjectName("actionwineinstall")
        self.menufile.addAction(self.actionChoose)
        self.menubangongruanjian.addAction(self.actionWPS)
        self.menubangongruanjian.addSeparator()
        self.menubangongruanjian.addAction(self.actionTencentMeeting)
        self.menubangongruanjian.addSeparator()
        self.menubangongruanjian.addAction(self.actionDingDing)
        self.menu.addAction(self.actionQQ)
        self.menu.addSeparator()
        self.menu.addAction(self.actionWeChat)
        self.menu_2.addAction(self.actionsteam)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionWeGame)
        self.menu_3.addAction(self.actionTencentVedio)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionAiqiyiVedio)
        self.menuMusic.addAction(self.actionQQMusic)
        self.menuMusic.addSeparator()
        self.menuMusic.addAction(self.actionCloudMusic)
        self.menuMusic.addSeparator()
        self.menuMusic.addAction(self.actionfoobar2000)
        self.menusoft.addAction(self.menubangongruanjian.menuAction())
        self.menusoft.addSeparator()
        self.menusoft.addAction(self.menu.menuAction())
        self.menusoft.addSeparator()
        self.menusoft.addAction(self.menu_2.menuAction())
        self.menusoft.addSeparator()
        self.menusoft.addAction(self.menu_3.menuAction())
        self.menusoft.addSeparator()
        self.menusoft.addAction(self.menuMusic.menuAction())
        self.menuhelp.addAction(self.actionzh)
        self.menufixer.addAction(self.actionwineinstall)
        self.menufixer.addSeparator()
        self.menufixer.addAction(self.actioncfg)
        self.menufixer.addSeparator()
        self.menufixer.addAction(self.actiontxt)
        self.menufixer.addSeparator()
        self.menufixer.addAction(self.actionreboot)
        self.menufixer.addSeparator()
        self.menufixer.addAction(self.actiondelete)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menusoft.menuAction())
        self.menubar.addAction(self.menufixer.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "Switch"))
        self.Buttonchoose.setText(_translate("MainWindow1", "选择文件"))
        self.textEdit.setPlaceholderText(_translate("MainWindow1", "请选择文件路径（所有已安装软件默认在/home/username/.wine/drive_c/Program Files (x86)路径下）"))
        self.labelpicture.setText(_translate("MainWindow1", "这里应该有一张图片"))
        self.label.setText(_translate("MainWindow1", "   Switch can run windows application on Linux"))
        self.Buttonrun.setText(_translate("MainWindow1", "安装/运行"))
        self.menufile.setTitle(_translate("MainWindow1", "文件"))
        self.menusoft.setTitle(_translate("MainWindow1", "常用软件"))
        self.menubangongruanjian.setTitle(_translate("MainWindow1", "办公软件"))
        self.menu.setTitle(_translate("MainWindow1", "通讯软件"))
        self.menu_2.setTitle(_translate("MainWindow1", "娱乐软件"))
        self.menu_3.setTitle(_translate("MainWindow1", "影视软件"))
        self.menuMusic.setTitle(_translate("MainWindow1", "音乐软件"))
        self.menuhelp.setTitle(_translate("MainWindow1", "帮助"))
        self.menufixer.setTitle(_translate("MainWindow1", "工具"))
        self.actionChoose.setText(_translate("MainWindow1", "选择文件"))
        self.actionQQ.setText(_translate("MainWindow1", "QQ"))
        self.actionWeChat.setText(_translate("MainWindow1", "WeChat"))
        self.actionWPS.setText(_translate("MainWindow1", "Wps"))
        self.actionWeChat_2.setText(_translate("MainWindow1", "WeChat"))
        self.actionWPS_2.setText(_translate("MainWindow1", "WPS"))
        self.actionzh.setText(_translate("MainWindow1", "中文乱码解决"))
        self.actioncfg.setText(_translate("MainWindow1", "wine设置"))
        self.actiontxt.setText(_translate("MainWindow1", "wine文档"))
        self.actiondelete.setText(_translate("MainWindow1", "软件卸载"))
        self.actionreboot.setText(_translate("MainWindow1", "wine重启"))
        self.actionTencentMeeting.setText(_translate("MainWindow1", "腾讯会议"))
        self.actionsteam.setText(_translate("MainWindow1", "Steam"))
        self.actionDingDing.setText(_translate("MainWindow1", "钉钉"))
        self.actionQQGame.setText(_translate("MainWindow1", "QQ游戏"))
        self.actionWeGame.setText(_translate("MainWindow1", "WeGame"))
        self.actionTencentVedio.setText(_translate("MainWindow1", "腾讯视频"))
        self.actionAiqiyiVedio.setText(_translate("MainWindow1", "爱奇艺"))
        self.actionQQMusic.setText(_translate("MainWindow1", "QQ音乐"))
        self.actionCloudMusic.setText(_translate("MainWindow1", "网易云音乐"))
        self.actionfoobar2000.setText(_translate("MainWindow1", "foobar2000"))
        self.actionwineinstall.setText(_translate("MainWindow1", "wine安装"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
