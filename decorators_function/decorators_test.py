#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                         GPL-license
#
# Title: decorators test              Version: 1.0
# Date:  07-01-2017                   Language: python3
# Description: werken met decorators, wrappers voorbeelden
#
###############################################################
import os

def Exists(oldfunc):
    def inside(filename):
        if (os.path.exists(filename)):
            oldfunc(filename)
        else:
            print('the file does not exist')

    return inside

@Exists  #dit is de decorator
def outputline(infile):
    with open(infile) as f:
        print(f.readlines())


outputline("decorators_test.py")  # hier wordt hij aangeroepen kijken of hij bestaat in dit geval
outputline('doesnotexits.py')  # file wordt aangeroepen kijken of hij bestaat in dit geval niet
