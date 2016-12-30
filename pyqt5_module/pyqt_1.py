#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                         GPL-license
#
# Title: PyQt5                       Version: 1.0
# Date:30-12-16                      Language: python3
# Description: qt5 gui
#
###############################################################
# do something

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui_imagedialog import Ui_ImageDialog

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_ImageDialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())

#todo voor één of andere reden wwerkt het nog niet
