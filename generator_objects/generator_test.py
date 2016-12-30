#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                             GPL-license
#
# Title: generator object                 Version: 1.0
# Date: 28-12-16                          Language: python3
# Description: generator objects uitleggen
#
###############################################################

input_list = [5,10,11,2,15,20,5,2,3,1] # een lijst
# zoeken van alle nummers die deelbaar zijn door 5
def div_by_five(num): # functie die nummers bevat 'num'
    if num  %  5  == 0: # if else statement
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i)) #dit is een generator object

# xyz = [] # dat is hetgeen die bovenstaaande regel uitvoerd is hetzelfde dus
# for i in input_list:
#     if div_by_five(i):
#         xyz.append(i) # tot hier hetzelfde als boven

# onderstaande voert het uit is geen generator object meer
[print(i) for i in xyz]
print(xyz)



