#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                             GPL-license
#
# Title: enumerate function               Version: 1.0
# Date: 28-12-16                          Language: python3
# Description: return an tuplle containing the count
# and the list variables
###############################################################

example = ['left', 'right', 'up', 'down']


for i, j in enumerate(example):  #juiste manier om genummerde lijst te maken
    print(i, j)

# for i in range(len(example)):  # dit is geen juiste manier
#     print(i, example(i))       # dit is geen juiste manier
print('###')
new_dict = dict(enumerate(example))  # print een dictionary
print(new_dict)



