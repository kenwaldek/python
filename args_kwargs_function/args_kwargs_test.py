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
def func(*args): # args zijn variabelen toekennen
    for arg in args:
        print (arg)

# func(1, 2, 3, 54, 'ham')
## of onderstaande
l = [1, 2, 3, 54, 'ham'] # maken van een lijst met waarden in
func(*l) # hier roep je de variablen lijst aan


