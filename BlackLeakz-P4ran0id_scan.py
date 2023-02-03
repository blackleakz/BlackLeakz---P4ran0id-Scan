#!/usr/bin/env python3
# BlackLeakz-P4ran0id_scan.py
# Author: BlackLeakz
# Version: 0.1a
# Website: http://cod3-project.gq/
# Github: 

import os
import sys
import time
import datetime 
import socket
import platform
import subprocess 

from os import *
from time import sleep
from datetime import datetime
from socket import *

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QProcess




timex = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


systemx = platform.system()


   
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 600)
        MainWindow.setStyleSheet("background-color: #CFCFCF;\n"
"color: #00FF1B;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 601))
        self.tabWidget.setStyleSheet("color: rgb(17, 15, 15);")
        self.tabWidget.setObjectName("tabWidget")
        
        self.login_tab = QtWidgets.QWidget()
        self.login_tab.setObjectName("login_tab")
        
        self.username_inp = QtWidgets.QLineEdit(self.login_tab)
        self.username_inp.setGeometry(QtCore.QRect(50, 70, 291, 24))
        self.username_inp.setObjectName("username_inp")
        self.password_inp = QtWidgets.QLineEdit(self.login_tab)
        self.password_inp.setGeometry(QtCore.QRect(50, 120, 291, 24))
        self.password_inp.setObjectName("password_inp")
        
        self.login_btn = QtWidgets.QPushButton(self.login_tab)
        self.login_btn.setGeometry(QtCore.QRect(260, 160, 80, 24))
        self.login_btn.setObjectName("login_btn")
        
        self.usrlabel = QtWidgets.QLabel(self.login_tab)
        self.usrlabel.setGeometry(QtCore.QRect(50, 50, 91, 16))
        self.usrlabel.setObjectName("usrlabel")
        
        self.passwordlabel = QtWidgets.QLabel(self.login_tab)
        self.passwordlabel.setGeometry(QtCore.QRect(50, 100, 91, 16))
        self.passwordlabel.setObjectName("passwordlabel")
        
        self.label_2 = QtWidgets.QLabel(self.login_tab)
        self.label_2.setGeometry(QtCore.QRect(420, 50, 49, 16))
        self.label_2.setObjectName("label_2")
        
        self.state_label = QtWidgets.QLabel(self.login_tab)
        self.state_label.setGeometry(QtCore.QRect(470, 50, 49, 16))
        self.state_label.setStyleSheet("color: rgb(0, 255, 217);")
        self.state_label.setObjectName("state_label")
        
        self.tabWidget.addTab(self.login_tab, "")
        
        self.config_tab = QtWidgets.QWidget()
        self.config_tab.setObjectName("config_tab")
        
        self.loadconfig_btn = QtWidgets.QPushButton(self.config_tab)
        self.loadconfig_btn.setGeometry(QtCore.QRect(20, 30, 80, 24))
        self.loadconfig_btn.setObjectName("loadconfig_btn")
        
        self.saveconfig_btn = QtWidgets.QPushButton(self.config_tab)
        self.saveconfig_btn.setGeometry(QtCore.QRect(20, 60, 80, 24))
        self.saveconfig_btn.setObjectName("saveconfig_btn")
        
        self.config_progressBar = QtWidgets.QProgressBar(self.config_tab)
        self.config_progressBar.setGeometry(QtCore.QRect(20, 520, 741, 23))
        self.config_progressBar.setProperty("value", 0)
        self.config_progressBar.setObjectName("config_progressBar")
        
        self.logpath_inp = QtWidgets.QLineEdit(self.config_tab)
        self.logpath_inp.setGeometry(QtCore.QRect(20, 150, 321, 24))
        self.logpath_inp.setObjectName("logpath_inp")
        
        self.logpathlabel = QtWidgets.QLabel(self.config_tab)
        self.logpathlabel.setGeometry(QtCore.QRect(20, 130, 141, 16))
        self.logpathlabel.setObjectName("logpathlabel")
        
        self.setLog_btn = QtWidgets.QPushButton(self.config_tab)
        self.setLog_btn.setGeometry(QtCore.QRect(260, 180, 80, 24))
        self.setLog_btn.setObjectName("setLog_btn")
        
        self.tabWidget.addTab(self.config_tab, "")
        
        self.scan_tab = QtWidgets.QWidget()
        self.scan_tab.setObjectName("scan_tab")
        
        self.target_inp = QtWidgets.QLineEdit(self.scan_tab)
        self.target_inp.setGeometry(QtCore.QRect(20, 40, 261, 24))
        self.target_inp.setStyleSheet("background-color: #9E9E9E;\n"
"color: #00FFD1;\n"
"")
        self.target_inp.setObjectName("target_inp")
        
        self.target_label = QtWidgets.QLabel(self.scan_tab)
        self.target_label.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.target_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.target_label.setObjectName("target_label")
        
        self.consoleLog = QtWidgets.QTextBrowser(self.scan_tab)
        self.consoleLog.setGeometry(QtCore.QRect(20, 361, 741, 131))
        self.consoleLog.setStyleSheet("background-color: black;\n"
"color: white;")
        self.consoleLog.setObjectName("consoleLog")
        
        self.progressBar = QtWidgets.QProgressBar(self.scan_tab)
        self.progressBar.setGeometry(QtCore.QRect(20, 510, 741, 23))
        self.progressBar.setStyleSheet("color: rgb(255, 0, 4);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        
        self.scanBtn = QtWidgets.QPushButton(self.scan_tab)
        self.scanBtn.setGeometry(QtCore.QRect(200, 70, 80, 24))
        self.scanBtn.setObjectName("scanBtn")
        self.scanBtn.clicked.connect(self.scantarget)
        
        self.consolelog_label = QtWidgets.QLabel(self.scan_tab)
        self.consolelog_label.setGeometry(QtCore.QRect(20, 340, 101, 16))
        self.consolelog_label.setObjectName("consolelog_label")
        
        self.openlogs_btn = QtWidgets.QPushButton(self.scan_tab)
        self.openlogs_btn.setGeometry(QtCore.QRect(200, 110, 80, 24))
        self.openlogs_btn.setObjectName("openlogs_btn")
        self.openlogs_btn.clicked.connect(self.openlogs_all)
        
        self.consolelog_label.raise_()
        self.target_inp.raise_()
        self.target_label.raise_()
        self.scanBtn.raise_()
        self.consoleLog.raise_()
        self.progressBar.raise_()
        self.openlogs_btn.raise_()
        self.tabWidget.addTab(self.scan_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.consoleLog.append("Console<>> Console started. " + timex)

        if systemx == "Windows":
            reply = QMessageBox()
            reply.setWindowTitle("OS-Detection")
            reply.setText("Detected Windows.")
            reply.exec()
        
        if systemx == "Linux":
            reply = QMessageBox()
            reply.setWindowTitle("OS-Detection")
            reply.setText("Detected Linux.") 
            reply.exec()
            
        
      

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BlackLeakz - P4ran0id Scan  |  v0.1a"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.usrlabel.setText(_translate("MainWindow", "Username:"))
        self.passwordlabel.setText(_translate("MainWindow", "Password:"))
        self.label_2.setText(_translate("MainWindow", "Status:"))
        self.state_label.setText(_translate("MainWindow", "STATE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login_tab), _translate("MainWindow", "Login"))
        self.loadconfig_btn.setText(_translate("MainWindow", "Load Config"))
        self.saveconfig_btn.setText(_translate("MainWindow", "Save Config"))
        self.logpathlabel.setText(_translate("MainWindow", "Enter Output-Log-Path:"))
        self.setLog_btn.setText(_translate("MainWindow", "Set"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config_tab), _translate("MainWindow", "Config"))
        self.target_inp.setToolTip(_translate("MainWindow", "Enter a target ip. ipv4 or ipv6, or a hostname  (dns)"))
        self.target_inp.setWhatsThis(_translate("MainWindow", "target inputbox"))
        self.target_label.setText(_translate("MainWindow", "Target IP or Hostname:"))
        self.scanBtn.setText(_translate("MainWindow", "Scan"))
        self.consolelog_label.setText(_translate("MainWindow", "ConsoleLog"))
        self.openlogs_btn.setText(_translate("MainWindow", "Open Logs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scan_tab), _translate("MainWindow", "Scan"))




    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("latin1")
        self.consoleLog.append(stdout)  



    def ping(self):
        self.consoleLog.append("Console<>> Starting PING. Your target: " + self.target_inp.text() + "\n")
        self.p = QProcess()
        self.p.readyReadStandardOutput.connect(self.handle_stdout)
        self.p.start("ping ", [self.target_inp.text()])
        
        
        
        
    
    def trace(self):
        self.consoleLog.append("Console<>> Starting TRACE. Your target: " + self.target_inp.text() + "\n")
        self.p = QProcess()
        self.p.readyReadStandardOutput.connect(self.handle_stdout)
        if systemx == "Windows":
            self.p.start("tracert ", [self.target_inp.text()])
        if systemx == "Linux":
            self.p.start("traceroute ", [self.target_inp.text()])

        
        
    def scantarget(self):
        self.consoleLog.append("Console<>> Starting auto-scan. Your target: " + self.target_inp.text() + "\n")
        self.ping()
        self.p.waitForFinished();
        self.p.close();
        self.trace()
        

        
  





    def openlogs_all(self):
        #print("Console<>> Open ALL LOGS!")
        self.consoleLog.append("Console<>> Opening all log files.  " + "\n")


   
        
    
        

        
    

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
          
        
    
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()