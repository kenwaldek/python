#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license
#
# Title: close program                         Version: 1.0
# Date: 2-2-17                          Language: python3
# Description: close a programm from within python with os mod
#
###############################################################
# Share if you care, do something
import os

def closeFile():
    try:
        os.system('pkill python3')

    except Exception:

