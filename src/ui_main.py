# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './main.ui'
#
# Created: Wed May 14 09:36:34 2014
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.devBox = QtGui.QComboBox(self.centralwidget)
        self.devBox.setGeometry(QtCore.QRect(20, 60, 241, 31))
        self.devBox.setObjectName("devBox")
        self.scanBtn = QtGui.QPushButton(self.centralwidget)
        self.scanBtn.setGeometry(QtCore.QRect(290, 60, 93, 27))
        self.scanBtn.setObjectName("scanBtn")
        self.fileBox = QtGui.QLineEdit(self.centralwidget)
        self.fileBox.setGeometry(QtCore.QRect(20, 20, 241, 27))
        self.fileBox.setObjectName("fileBox")
        self.fileBtn = QtGui.QPushButton(self.centralwidget)
        self.fileBtn.setGeometry(QtCore.QRect(290, 20, 93, 27))
        self.fileBtn.setObjectName("fileBtn")
        self.exitBtn = QtGui.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(300, 220, 93, 27))
        self.exitBtn.setObjectName("exitBtn")
        self.burnBtn = QtGui.QPushButton(self.centralwidget)
        self.burnBtn.setGeometry(QtCore.QRect(190, 220, 93, 27))
        self.burnBtn.setObjectName("burnBtn")
        self.msgBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.msgBox.setEnabled(True)
        self.msgBox.setGeometry(QtCore.QRect(10, 103, 381, 101))
        self.msgBox.setUndoRedoEnabled(False)
        self.msgBox.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.msgBox.setObjectName("msgBox")
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 220, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuH_elp = QtGui.QMenu(self.menubar)
        self.menuH_elp.setObjectName("menuH_elp")
        self.menu_tools = QtGui.QMenu(self.menubar)
        self.menu_tools.setObjectName("menu_tools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.actionSd_partition = QtGui.QAction(MainWindow)
        self.actionSd_partition.setObjectName("actionSd_partition")
        self.action_Dnw = QtGui.QAction(MainWindow)
        self.action_Dnw.setObjectName("action_Dnw")
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Exit)
        self.menuH_elp.addAction(self.action_About)
        self.menu_tools.addAction(self.actionSd_partition)
        self.menu_tools.addAction(self.action_Dnw)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())
        self.menubar.addAction(self.menuH_elp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.exitBtn, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QObject.connect(self.action_Exit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.scanBtn.setText(QtGui.QApplication.translate("MainWindow", "Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.fileBtn.setText(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.exitBtn.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.burnBtn.setText(QtGui.QApplication.translate("MainWindow", "Burn", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuH_elp.setTitle(QtGui.QApplication.translate("MainWindow", "H&elp", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_tools.setTitle(QtGui.QApplication.translate("MainWindow", "&tools", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSd_partition.setText(QtGui.QApplication.translate("MainWindow", "sd_partition", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Dnw.setText(QtGui.QApplication.translate("MainWindow", "&dnw", None, QtGui.QApplication.UnicodeUTF8))

