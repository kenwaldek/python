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
def func(**kwargs):
    for item in kwargs.items():
        print (item)

func(x=400, y=3)  # print deze waarden uit


