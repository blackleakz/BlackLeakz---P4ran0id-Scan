#!/usr/bin/env python3
# BlackLeakz-P4ran0id_scan.py
# Author: BlackLeakz
# Version: 0.1a
# Website: http://cod3-project.gq/
# Github: 
#--------------------------------------------------------------------------------------------------------------------------------

import os
import sys
import time
import datetime 
import socket
import platform
import subprocess 
import ipaddress
from ip2geotools.databases.noncommercial import DbIpCity

from time import sleep
from datetime import datetime
from socket import *
from contextlib import redirect_stdout

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QProcess


#--------------------------------------------------------------------------------------------------------------------------------


timex = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


systemx = platform.system()

dir_path = os.getcwd()

#--------------------------------------------------------------------------------------------------------------------------------


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 665)
        MainWindow.setStyleSheet("background-color: #CFCFCF;\n"
"color: #00FF1B;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 651))
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
        self.setLog_btn.clicked.connect(self.setlogfile)

        
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
        self.openlogs_btn.setGeometry(QtCore.QRect(200, 150, 80, 24))
        self.openlogs_btn.setObjectName("openlogs_btn")
        self.openlogs_btn.clicked.connect(self.openlogs_all)

        self.checkLogBox = QtWidgets.QCheckBox(self.scan_tab)
        self.checkLogBox.setGeometry(QtCore.QRect(20, 100, 161, 22))
        self.checkLogBox.setObjectName("checkLogBox")
        
        self.consolelog_label.raise_()
        self.target_inp.raise_()
        self.target_label.raise_()
        self.scanBtn.raise_()
        self.consoleLog.raise_()
        self.progressBar.raise_()
        self.openlogs_btn.raise_()
        self.checkLogBox.raise_()
        self.tabWidget.addTab(self.scan_tab, "")
        self.terminal_tab = QtWidgets.QWidget()
        self.terminal_tab.setObjectName("terminal_tab")
        
        self.terminal = QtWidgets.QTextBrowser(self.terminal_tab)
        self.terminal.setGeometry(QtCore.QRect(10, 30, 761, 481))
        self.terminal.setStyleSheet("background-color: black;\n"
"color: white;")
        self.terminal.setObjectName("terminal")
        
        self.terminalcmd_inp = QtWidgets.QLineEdit(self.terminal_tab)
        self.terminalcmd_inp.setGeometry(QtCore.QRect(10, 520, 681, 24))
        self.terminalcmd_inp.setObjectName("terminalcmd_inp")
        self.terminalcmd_inp.returnPressed.connect(self.send_terminal)

        
        self.sendBtn = QtWidgets.QPushButton(self.terminal_tab)
        self.sendBtn.setGeometry(QtCore.QRect(700, 520, 71, 24))
        self.sendBtn.setObjectName("sendBtn")
        self.sendBtn.clicked.connect(self.send_terminal)

        self.terminal_target_inp = QtWidgets.QLineEdit(self.terminal_tab)
        self.terminal_target_inp.setGeometry(QtCore.QRect(10, 580, 311, 24))
        self.terminal_target_inp.setObjectName("terminal_target_inp")
        
        self.label = QtWidgets.QLabel(self.terminal_tab)
        self.label.setGeometry(QtCore.QRect(10, 560, 91, 16))
        self.label.setObjectName("label")
        
        self.tabWidget.addTab(self.terminal_tab, "")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
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
        self.checkLogBox.setText(_translate("MainWindow", "Logging output to file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scan_tab), _translate("MainWindow", "Scan"))
        self.sendBtn.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "Arguments:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.terminal_tab), _translate("MainWindow", "Terminal"))

#--------------------------------------------------------------------------------------------------------------------------------

## PIPE
    def handle_stdout_consoleLog(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("latin1")
        self.consoleLog.append(stdout)  

    def handle_stdout_terminal(self):
        datax = self.p.readAllStandardOutput()
        stdoutx = bytes(datax).decode("latin1")
        self.terminal.append(stdoutx) 


###

#--------------------------------------------------------------------------------------------------------------------------------

### Auto-Scan functions

## GET GEOLOCATION
    def geolocation_get(self):
            isExist = os.path.exists("geo")
            if isExist == True:
                    os.chdir("geo")
            if isExist == False:
                    os.mkdir("geo")
                    os.chdir("geo")
                    
            response = DbIpCity.get(self.target_inp.text(), api_key='free')
            country = str(response.country)
            region = str(response.region)
            city = str(response.city)
            
            os.system('echo ' + country + " >> geo.log")
            os.system('echo ' + region + " >> geo.log")
            os.system('echo ' + city + " >> geo.log")
            
            self.consoleLog.append("Console<>> Got Geolocation.")
            self.consoleLog.append("Console<>> Country: " + response.country)
            self.consoleLog.append("Console<>> Region: " + response.region)
            self.consoleLog.append("Console<>> City: " + response.city)
            self.consoleLog.append("Console<>> Log is written to file, located at \geo\geo.log.")
            
            
            self.consoleLog.append("Console<>> " + dir_path)
            for path in os.listdir(dir_path):
                    if os.path.isfile(os.path.join(dir_path, path)):
                            self.terminal.append(path)
            
            os.chdir("..")
            

 # GET PING           
    def ping(self):
            self.consoleLog.append("Console<>> Starting PING. Your target: " + self.target_inp.text() + "\n")
            self.p = QProcess()
            self.p.setStandardOutputFile("ping.txt");

            self.p.readyReadStandardOutput.connect(self.handle_stdout_consoleLog)
            self.p.start("ping ", [self.target_inp.text()])
            self.p.waitForFinished();
           # self.p.close();
           
            
            
        
# GET ROUTE        
    def trace(self):
            self.consoleLog.append("Console<>> Starting TRACE. Your target: " + self.target_inp.text() + "\n")
            self.p = QProcess()
            self.p.setStandardOutputFile("trace.txt");
            self.p.readyReadStandardOutput.connect(self.handle_stdout_consoleLog)
            
            if systemx == "Windows":
                    self.p.start("tracert ", [self.target_inp.text()])
                    self.p.waitForFinished();
                  #  self.p.close();
                    
            if systemx == "Linux":
                    self.p.start("traceroute ", [self.target_inp.text()])
                  #  self.p.waitForFinished();
                   # self.p.close();
            
  #####
#--------------------------------------------------------------------------------------------------------------------------------
 
  #### Terminal Functions   
  
  # GET ROUTE       
    def term_trace(self):
            if systemx == "Windows":
                 targetxy = self.terminal_target_inp.text()
                 self.terminal.append("Console<>> Starting trace-route: " + targetxy)
                 self.p = QProcess()
                 self.p.readyReadStandardOutput.connect(self.handle_stdout_terminal)
                 self.p.setStandardOutputFile("term_trace.txt");
                 self.p.start("tracert ", [targetxy])
                # self.p.waitForFinished();
                 #self.p.close();
                 
            if systemx == "Linux":
                 targetxy = self.terminal_target_inp.text()
                 self.terminal.append("Console<>> Starting trace-route: " + targetxy)
                 self.p = QProcess()
                 self.p.readyReadStandardOutput.connect(self.handle_stdout_terminal)
                 self.p.setStandardOutputFile("term_trace.txt");
                 self.p.start("traceroute ", [targetxy])
                 #self.p.waitForFinished();
                 #self.p.close();
        
# GET GEOLOCATION_TERM

#     def global_geo(self, arg1, *vartuple):
#             self.terminal.append(arg1)
#             for var in vartuple:
#                     response = DbIpCity.get(str(var), api_key='free')
#                     self.terminal.append(var)
#                     city = str(response.city)
##                     region = str(response.region)#
#                     country = str(response.country)
                    
#                     self.terminal.append("Console<>> City: " + city)
#                     self.terminal.append("Console<>> Region: " + region)
#                     self.terminal.append("Console<>> Country: " + country)
#             return

    def geolocation_get_term(self):
            isExist = os.path.exists("geo")
            if isExist == True:
                    os.chdir("geo")
            if isExist == False:
                    os.mkdir("geo")
                    os.chdir("geo")
                    
            response = DbIpCity.get(self.terminal_target_inp.text(), api_key='free')
            country = str(response.country)
            region = str(response.region)
            city = str(response.city)
            
            os.system('echo ' + country + " >> geo.log")
            os.system('echo ' + region + " >> geo.log")
            os.system('echo ' + city + " >> geo.log")
            
            self.terminal.append("Console<>> Got Geolocation.")
            self.terminal.append("Console<>> Country: " + response.country)
            self.terminal.append("Console<>> Region: " + response.region)
            self.terminal.append("Console<>> City: " + response.city)
            self.terminal.append("Console<>> Log is written to file, located at \geo\geo.log.")
            
            
            self.terminal.append("Console<>> " + dir_path)
            for path in os.listdir(dir_path):
                    if os.path.isfile(os.path.join(dir_path, path)):
                            self.terminal.append(path)
            
            os.chdir("..")
            
#     def test(self, ip ):
#             ip = self.terminal_target_inp.text()
#             response = DbIpCity.get(ip, api_key='free')
#             print (ip)
#             return

# # Now you can call printme function
#     ip = "192.168.1.1"
#     test( ip )
#     response = DbIpCity.get(ip, api_key='free')
    
    
# GET HELP        
    def help(self):
            self.terminal.append("Console<>> HELP_DOCUMENTATION ")
            self.terminal.append("Console<>> !t trace | !p ping ")

# Input Handling Func            
    def send_terminal(self):
        cmd = self.terminalcmd_inp.text()
        self.terminal.append("Console<>> " + cmd)
        self.terminalcmd_inp.setText("") 
        
        if cmd == "!h":
                self.help()
        if cmd == "!t":
                self.term_trace()
        if cmd == "!g":
                self.geolocation_get_term()
        # if cmd == "!gm":
        #         ips = self.terminal_target_inp.text()
        #         ipxx = str(ips)
        #        # ipsx = ipaddress.ip_address(ips)
                
        #         self.global_geo( ipxx )
        #         #self.global_geo( "40.113.110.67 ", "40.113.110.67", "13.107.5.88")
                
        if cmd == "dir":
                
                self.terminal.append("Console<>> " + dir_path)
                for path in os.listdir(dir_path):
                        if os.path.isfile(os.path.join(dir_path, path)):
                                self.terminal.append(path)
             
                        
                        
                        
                
                
                
        else:
                self.p = QProcess()
                self.p.readyReadStandardOutput.connect(self.handle_stdout_terminal)
                self.p.start(cmd)
                #self.p.waitForFinished();
                #self.p.close();
        
  
            
#--------------------------------------------------------------------------------------------------------------------------------


    ######################    
  # Autoscan main-function      
    def scantarget(self):
            self.consoleLog.append("Console<>> Starting auto-scan. Your target: " + self.target_inp.text() + "\n")
            self.ping()
            self.p.waitForFinished();
            self.p.close();
            self.trace()
            self.geolocation_get()
        

        
  
#--------------------------------------------------------------------------------------------------------------------------------

    def setlogfile(self):
            reply = QMessageBox()
            reply.setWindowTitle("Info")
            reply.setText("Logfile set.")
            reply.exec()
            



    def openlogs_all(self):
            reply = QMessageBox()
            reply.setWindowTitle("Info")
            reply.setText("Open all logs now")
            reply.exec()


#--------------------------------------------------------------------------------------------------------------------------------
  
        
    
           

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
          
        
    
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
    