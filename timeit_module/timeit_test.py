#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek
#
# Title: timeit module                         Version: 1.0
# Date: 28-12-16                          Language: python3
# Description: meet de duur van uitvoerende code
#
###############################################################
import timeit

# print(timeit.timeit('1+3', number=1000))
#
print('##########################')

# input_list = range(100)
#
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False

# xyz = (i for i in input_list if div_by_five(i))  #dit is een generator

# xyz = [i for i in input_list if div_by_five(i)]  # dit is een lijst

print(timeit.timeit('''input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))''', number=50))
