#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                   GPL-license
#
# Title: .format                Version:
# Date:  24-12-16               Language: python3
# Description: testing .format string format
#
###############################################################
print ('{:10}'.format('test'))
###
name = "kenny"
print ("my name is {:1} and it works".format(name))
###
print ('{:d}'.format(42)) # nummers = :d van decimaal
###
print ("{:f}".format(3.141592653589793)) # float na de comma dus PI
###
a = "dit"
b = "zijn"
c = "variablen"
print('{0}, {1}, {2}'.format('a', 'b', 'c')) # dit zijn strings
print('{0}, {1}, {2}'.format(a, b, c)) # dit zijn de variablen
###
