#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license
#
# Title: return function              Version: 1.0
# Date: 2-2-2017                      Language: python3
# Description: examples of return values
#
###############################################################
# Share if you care, do something


###
def rol_2_dice():
    import random
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    return d1 + d2

print(rol_2_dice())

###
def sum_up(val1,val2):
    return val1 + val2

print(sum_up(10, 5))

###
def remove_mod(string, mod_val):
    new_string = ''
    for index in range(0, len(string)):
        if index % mod_val!= 0:
            new_string = new_string + string[index]
    return new_string

a = remove_mod('this is a string', 2)  #verwijderd telkens tot de 2de letter
print(a)

###
def hilo(list_of_nums):
    high = float("-inf")
    low = float("inf")
    for index in range(0, len(list_of_nums)):
        if list_of_nums[index] > high:
            high = list_of_nums[index]
        if list_of_nums[index] < low:
            low = list_of_nums[index]
        return high, low

high, low = hilo([1,3,5,6,7,9,5,15])
print(high)
print(low)

###
