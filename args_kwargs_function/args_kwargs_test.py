#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                         GPL-license
#
# Title: args, kwargs                 Version: 1.0
# Date: 07-01-17                      Language: python3
# Description: args kwargs functions testing
#
###############################################################

# do something
def func(*args):
    for arg in args:
        print (arg)

# func(1, 2, 3, 54, 'ham')
## of onderstaande
l = [1, 2, 3, 54, 'ham']
func(*l)


