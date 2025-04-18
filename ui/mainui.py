# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 416, 480))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logolabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.logolabel.setMinimumSize(QtCore.QSize(0, 250))
        self.logolabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logolabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.logolabel.setObjectName("logolabel")
        self.verticalLayout_2.addWidget(self.logolabel)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.passwordEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.passwordEdit.setMinimumSize(QtCore.QSize(180, 0))
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.horizontalLayout_2.addWidget(self.passwordEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.passwordButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.passwordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.passwordButton.setObjectName("passwordButton")
        self.horizontalLayout_2.addWidget(self.passwordButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.setexepath_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.setexepath_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setexepath_button.setObjectName("setexepath_button")
        self.verticalLayout_2.addWidget(self.setexepath_button)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.installbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.installbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.installbutton.setObjectName("installbutton")
        self.verticalLayout_2.addWidget(self.installbutton)
        self.bashbrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.bashbrowser.setGeometry(QtCore.QRect(420, 0, 451, 481))
        self.bashbrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.bashbrowser.setObjectName("bashbrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 23))
        self.menubar.setObjectName("menubar")
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        self.toolMenu = QtWidgets.QMenu(self.menubar)
        self.toolMenu.setObjectName("toolMenu")
        self.commonMenu = QtWidgets.QMenu(self.menubar)
        self.commonMenu.setObjectName("commonMenu")
        self.menu = QtWidgets.QMenu(self.commonMenu)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.commonMenu)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.commonMenu)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.commonMenu)
        self.menu_4.setObjectName("menu_4")
        self.helpMenu = QtWidgets.QMenu(self.menubar)
        self.helpMenu.setObjectName("helpMenu")
        self.aboutMenu = QtWidgets.QMenu(self.menubar)
        self.aboutMenu.setObjectName("aboutMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fileopenAction = QtWidgets.QAction(MainWindow)
        self.fileopenAction.setObjectName("fileopenAction")
        self.wineinstallaction = QtWidgets.QAction(MainWindow)
        self.wineinstallaction.setObjectName("wineinstallaction")
        self.Introduction = QtWidgets.QAction(MainWindow)
        self.Introduction.setObjectName("Introduction")
        self.luanma = QtWidgets.QAction(MainWindow)
        self.luanma.setObjectName("luanma")
        self.winesetaction = QtWidgets.QAction(MainWindow)
        self.winesetaction.setObjectName("winesetaction")
        self.winerestartaction = QtWidgets.QAction(MainWindow)
        self.winerestartaction.setObjectName("winerestartaction")
        self.actionQQ = QtWidgets.QAction(MainWindow)
        self.actionQQ.setObjectName("actionQQ")
        self.QQ = QtWidgets.QAction(MainWindow)
        self.QQ.setObjectName("QQ")
        self.wechat = QtWidgets.QAction(MainWindow)
        self.wechat.setObjectName("wechat")
        self.kugou = QtWidgets.QAction(MainWindow)
        self.kugou.setObjectName("kugou")
        self.wangyi = QtWidgets.QAction(MainWindow)
        self.wangyi.setObjectName("wangyi")
        self.qqmusic = QtWidgets.QAction(MainWindow)
        self.qqmusic.setObjectName("qqmusic")
        self.document = QtWidgets.QAction(MainWindow)
        self.document.setObjectName("document")
        self.action7_Zip = QtWidgets.QAction(MainWindow)
        self.action7_Zip.setObjectName("action7_Zip")
        self.wineuninstaller = QtWidgets.QAction(MainWindow)
        self.wineuninstaller.setObjectName("wineuninstaller")
        self.purgewine = QtWidgets.QAction(MainWindow)
        self.purgewine.setObjectName("purgewine")
        self.qqmusic_2 = QtWidgets.QAction(MainWindow)
        self.qqmusic_2.setObjectName("qqmusic_2")
        self.dingding = QtWidgets.QAction(MainWindow)
        self.dingding.setObjectName("dingding")
        self.tengxunmeeting = QtWidgets.QAction(MainWindow)
        self.tengxunmeeting.setObjectName("tengxunmeeting")
        self.othertools = QtWidgets.QAction(MainWindow)
        self.othertools.setObjectName("othertools")
        self.fileMenu.addAction(self.fileopenAction)
        self.toolMenu.addAction(self.wineinstallaction)
        self.toolMenu.addAction(self.winesetaction)
        self.toolMenu.addAction(self.winerestartaction)
        self.toolMenu.addAction(self.wineuninstaller)
        self.toolMenu.addAction(self.purgewine)
        self.toolMenu.addAction(self.othertools)
        self.menu.addAction(self.QQ)
        self.menu.addAction(self.wechat)
        self.menu_2.addAction(self.kugou)
        self.menu_2.addAction(self.wangyi)
        self.menu_2.addAction(self.qqmusic_2)
        self.menu_3.addAction(self.action7_Zip)
        self.menu_4.addAction(self.dingding)
        self.menu_4.addAction(self.tengxunmeeting)
        self.commonMenu.addAction(self.menu.menuAction())
        self.commonMenu.addAction(self.menu_2.menuAction())
        self.commonMenu.addAction(self.menu_3.menuAction())
        self.commonMenu.addAction(self.menu_4.menuAction())
        self.helpMenu.addAction(self.luanma)
        self.helpMenu.addAction(self.document)
        self.aboutMenu.addAction(self.Introduction)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.toolMenu.menuAction())
        self.menubar.addAction(self.commonMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())
        self.menubar.addAction(self.aboutMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logolabel.setText(_translate("MainWindow", "NCEPU"))
        self.label.setText(_translate("MainWindow", "                      Windows软件适配安装器"))
        self.label_2.setText(_translate("MainWindow", "sudo密码"))
        self.passwordButton.setText(_translate("MainWindow", "确认"))
        self.setexepath_button.setText(_translate("MainWindow", "选择EXE文件"))
        self.installbutton.setText(_translate("MainWindow", "安装 运行"))
        self.fileMenu.setTitle(_translate("MainWindow", "文件"))
        self.toolMenu.setTitle(_translate("MainWindow", "工具"))
        self.commonMenu.setTitle(_translate("MainWindow", "常用"))
        self.menu.setTitle(_translate("MainWindow", "聊天软件"))
        self.menu_2.setTitle(_translate("MainWindow", "音乐软件"))
        self.menu_3.setTitle(_translate("MainWindow", "工具"))
        self.menu_4.setTitle(_translate("MainWindow", "办公"))
        self.helpMenu.setTitle(_translate("MainWindow", "帮助"))
        self.aboutMenu.setTitle(_translate("MainWindow", "关于"))
        self.fileopenAction.setText(_translate("MainWindow", "打开"))
        self.wineinstallaction.setText(_translate("MainWindow", "wine安装"))
        self.Introduction.setText(_translate("MainWindow", "项目介绍"))
        self.luanma.setText(_translate("MainWindow", "一键解决乱码"))
        self.winesetaction.setText(_translate("MainWindow", "wine设置"))
        self.winerestartaction.setText(_translate("MainWindow", "wine重启"))
        self.actionQQ.setText(_translate("MainWindow", "QQ"))
        self.QQ.setText(_translate("MainWindow", "QQ"))
        self.wechat.setText(_translate("MainWindow", "微信"))
        self.kugou.setText(_translate("MainWindow", "酷狗音乐"))
        self.wangyi.setText(_translate("MainWindow", "网易音乐"))
        self.qqmusic.setText(_translate("MainWindow", "QQ音乐"))
        self.document.setText(_translate("MainWindow", "Wine文档"))
        self.action7_Zip.setText(_translate("MainWindow", "7-Zip"))
        self.wineuninstaller.setText(_translate("MainWindow", "卸载已安装软件"))
        self.purgewine.setText(_translate("MainWindow", "卸载wine"))
        self.qqmusic_2.setText(_translate("MainWindow", "QQ音乐"))
        self.dingding.setText(_translate("MainWindow", "钉钉"))
        self.tengxunmeeting.setText(_translate("MainWindow", "腾讯会议"))
        self.othertools.setText(_translate("MainWindow", "其他工具"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
