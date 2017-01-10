#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                         GPL-license
#
# Title: PyQt5 status bar            Version: 1.0
# Date:30-12-16                      Language: python3
# Description: qt5 gui statusbar
#
###############################################################
# do something
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 status bar example'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Message in statusbar.')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())