#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license
#
# Title: kivy                         Version: 1.0
# Date: 17-01-2017                    Language: python3
# Description: testing of the kivy module
#
###############################################################
# Share if you care, think of it like an pythonic way
# do something

import kivy
kivy.require('1.8.0') # op rpi gebruik 1.8.0
from kivy.app import App
from kivy.uix.button import Label

class kivi_test(App):
    def build(self):
        return Label(text='hello kivy test')


if __name__ == "__main__":
    KiviTest = kivi_test()
    KiviTest.run()