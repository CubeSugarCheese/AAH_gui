# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_guiMainWindow(object):
    def setupUi(self, guiMainWindow):
        guiMainWindow.setObjectName("guiMainWindow")
        guiMainWindow.setWindowModality(QtCore.Qt.WindowModal)
        guiMainWindow.setEnabled(True)
        guiMainWindow.resize(422, 515)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        guiMainWindow.setFont(font)
        guiMainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon(ico)/akhelper_color.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        guiMainWindow.setWindowIcon(icon)
        guiMainWindow.setWindowOpacity(1.0)
        guiMainWindow.setStyleSheet("QTabBar::tab {\n"
"  color: [color];\n"
"  padding: 7px 16px;\n"
"  background-color: [background];\n"
"  border-right: 6px solid [background];\n"
"  border-left:  6px solid [background];\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:hover {\n"
"  background-color: [hover];\n"
"  border-right: [hover];\n"
"  border-left: [hover];\n"
"  color: [color];\n"
"}\n"
"\n"
"QTabBar::tab:disabled {\n"
"  background-color: #bbbbbb;\n"
"  border-right: #bbbbbb;\n"
"  border-left: #bbbbbb;\n"
"  color: [color];\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"  color: [color];\n"
"  border-bottom: 6px solid [bottom];\n"
"  background-color: [background];\n"
"  border-right: 6px solid [background];\n"
"  border-left:  6px solid [background];\n"
"}\n"
"\n"
"QTabBar:close-button {\n"
"    /*workaround to avoid close button. Do !not! add this image!*/\n"
"    image: url(:/closebutton.png);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(guiMainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 350, 381, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.runningState = QtWidgets.QLabel(self.centralwidget)
        self.runningState.setGeometry(QtCore.QRect(30, 310, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.runningState.setFont(font)
        self.runningState.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.runningState.setFocusPolicy(QtCore.Qt.TabFocus)
        self.runningState.setLineWidth(1)
        self.runningState.setTextFormat(QtCore.Qt.AutoText)
        self.runningState.setObjectName("runningState")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(280, 310, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.helpGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.helpGroupBox.setGeometry(QtCore.QRect(20, 20, 381, 81))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.helpGroupBox.setFont(font)
        self.helpGroupBox.setObjectName("helpGroupBox")
        self.closeGameButton = QtWidgets.QPushButton(self.helpGroupBox)
        self.closeGameButton.setGeometry(QtCore.QRect(260, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.closeGameButton.setFont(font)
        self.closeGameButton.setObjectName("closeGameButton")
        self.openGameButton = QtWidgets.QPushButton(self.helpGroupBox)
        self.openGameButton.setGeometry(QtCore.QRect(140, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.openGameButton.setFont(font)
        self.openGameButton.setObjectName("openGameButton")
        self.initializationButton = QtWidgets.QPushButton(self.helpGroupBox)
        self.initializationButton.setGeometry(QtCore.QRect(20, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.initializationButton.setFont(font)
        self.initializationButton.setObjectName("initializationButton")
        self.BattlegGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.BattlegGroupBox.setGeometry(QtCore.QRect(20, 120, 381, 181))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.BattlegGroupBox.setFont(font)
        self.BattlegGroupBox.setObjectName("BattlegGroupBox")
        self.label_5 = QtWidgets.QLabel(self.BattlegGroupBox)
        self.label_5.setGeometry(QtCore.QRect(130, 50, 71, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.startBattleButton = QtWidgets.QPushButton(self.BattlegGroupBox)
        self.startBattleButton.setGeometry(QtCore.QRect(260, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.startBattleButton.setFont(font)
        self.startBattleButton.setObjectName("startBattleButton")
        self.quickStartBattleButton = QtWidgets.QPushButton(self.BattlegGroupBox)
        self.quickStartBattleButton.setGeometry(QtCore.QRect(140, 140, 221, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.quickStartBattleButton.setFont(font)
        self.quickStartBattleButton.setStyleSheet("")
        self.quickStartBattleButton.setObjectName("quickStartBattleButton")
        self.label_7 = QtWidgets.QLabel(self.BattlegGroupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 71, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.BattlegGroupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 71, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.BattlegGroupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_6.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_6.setLineWidth(1)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")
        self.stage = QtWidgets.QLineEdit(self.BattlegGroupBox)
        self.stage.setGeometry(QtCore.QRect(20, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        self.stage.setFont(font)
        self.stage.setStyleSheet("QLineEdit, QLineEdit:hover {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 1px solid #dddddd;\n"
"    color: black;\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QLineEdit:editable{\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #b2dfdb;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #eeeeee;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"    color: #111111;\n"
"}\n"
"QLineEdit:pressed {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"}\n"
"\n"
"")
        self.stage.setText("")
        self.stage.setObjectName("stage")
        self.battleTime = QtWidgets.QLineEdit(self.BattlegGroupBox)
        self.battleTime.setGeometry(QtCore.QRect(140, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        self.battleTime.setFont(font)
        self.battleTime.setStyleSheet("QLineEdit, QLineEdit:hover {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 1px solid #dddddd;\n"
"    color: black;\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QLineEdit:editable{\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #b2dfdb;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #eeeeee;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"    color: #111111;\n"
"}\n"
"QLineEdit:pressed {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"}\n"
"\n"
"")
        self.battleTime.setText("")
        self.battleTime.setObjectName("battleTime")
        self.quickBattleTime = QtWidgets.QLineEdit(self.BattlegGroupBox)
        self.quickBattleTime.setGeometry(QtCore.QRect(20, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        self.quickBattleTime.setFont(font)
        self.quickBattleTime.setStyleSheet("QLineEdit, QLineEdit:hover {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 1px solid #dddddd;\n"
"    color: black;\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QLineEdit:editable{\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #b2dfdb;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #eeeeee;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"    color: #111111;\n"
"}\n"
"QLineEdit:pressed {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"}\n"
"\n"
"")
        self.quickBattleTime.setText("")
        self.quickBattleTime.setObjectName("quickBattleTime")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(160, 310, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.helpGroupBox.raise_()
        self.BattlegGroupBox.raise_()
        self.textBrowser.raise_()
        self.runningState.raise_()
        self.stopButton.raise_()
        self.clearButton.raise_()
        guiMainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(guiMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 422, 23))
        self.menuBar.setStyleSheet("")
        self.menuBar.setObjectName("menuBar")
        self.settingsMenu = QtWidgets.QMenu(self.menuBar)
        self.settingsMenu.setStyleSheet("")
        self.settingsMenu.setObjectName("settingsMenu")
        self.toolsMenu = QtWidgets.QMenu(self.menuBar)
        self.toolsMenu.setStyleSheet("")
        self.toolsMenu.setObjectName("toolsMenu")
        guiMainWindow.setMenuBar(self.menuBar)
        self.settings = QtWidgets.QAction(guiMainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/all/settings_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon1)
        self.settings.setObjectName("settings")
        self.about = QtWidgets.QAction(guiMainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/all/about_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about.setIcon(icon2)
        self.about.setObjectName("about")
        self.taskPlanning = QtWidgets.QAction(guiMainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/all/planning_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.taskPlanning.setIcon(icon3)
        self.taskPlanning.setObjectName("taskPlanning")
        self.settingsMenu.addAction(self.settings)
        self.settingsMenu.addSeparator()
        self.settingsMenu.addAction(self.about)
        self.toolsMenu.addAction(self.taskPlanning)
        self.menuBar.addAction(self.settingsMenu.menuAction())
        self.menuBar.addAction(self.toolsMenu.menuAction())

        self.retranslateUi(guiMainWindow)
        QtCore.QMetaObject.connectSlotsByName(guiMainWindow)

    def retranslateUi(self, guiMainWindow):
        _translate = QtCore.QCoreApplication.translate
        guiMainWindow.setWindowTitle(_translate("guiMainWindow", "Arknights Auto Helper GUI "))
        self.textBrowser.setHtml(_translate("guiMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.runningState.setText(_translate("guiMainWindow", "运行状态"))
        self.stopButton.setText(_translate("guiMainWindow", "中止线程"))
        self.helpGroupBox.setTitle(_translate("guiMainWindow", "辅助操作模块"))
        self.closeGameButton.setText(_translate("guiMainWindow", "退出游戏"))
        self.openGameButton.setText(_translate("guiMainWindow", "打开游戏"))
        self.initializationButton.setText(_translate("guiMainWindow", "初始化辅助"))
        self.BattlegGroupBox.setTitle(_translate("guiMainWindow", "战斗模块"))
        self.label_5.setText(_translate("guiMainWindow", "战斗次数："))
        self.startBattleButton.setText(_translate("guiMainWindow", "开始战斗"))
        self.quickStartBattleButton.setText(_translate("guiMainWindow", "以当前游戏内选中关卡开始战斗"))
        self.label_7.setText(_translate("guiMainWindow", "战斗次数："))
        self.label_4.setText(_translate("guiMainWindow", "关卡："))
        self.label_6.setText(_translate("guiMainWindow", "快速战斗"))
        self.clearButton.setText(_translate("guiMainWindow", "清除记录"))
        self.settingsMenu.setTitle(_translate("guiMainWindow", "设置"))
        self.toolsMenu.setTitle(_translate("guiMainWindow", "工具"))
        self.settings.setText(_translate("guiMainWindow", "设置"))
        self.settings.setShortcut(_translate("guiMainWindow", "Ctrl+S"))
        self.about.setText(_translate("guiMainWindow", "关于"))
        self.about.setShortcut(_translate("guiMainWindow", "Ctrl+A"))
        self.taskPlanning.setText(_translate("guiMainWindow", "任务规划"))
        self.taskPlanning.setShortcut(_translate("guiMainWindow", "Ctrl+T"))
import spec_rc
