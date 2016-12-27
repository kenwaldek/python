#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek
#
# Title: String Concatenation             Version: 1.0
# Date: 27-12-16                          Language: python3
# Description: String Concatenation strings
#
###############################################################

names = ['kenny', 'sofie', 'jill', 'samantha']

# for name in names:
#     print('hello there,' +name)
#     print(' '.join(['hello there ,', name]))
print(', '.join(names))

who = 'gary'
how_many = 12

print(who, 'bought', how_many, 'apples today')
# onderstaande is de juiste manier in python3
print('{} bought {} apples today!' .format(who, how_many))

