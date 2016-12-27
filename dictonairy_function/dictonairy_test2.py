#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek
#
# Title: dictonary_test2                 Version: 1.0
# Date: 27-12-16                        Language: python3
# Description: maken van een bibliotheek dictorary dus
#
###############################################################

exdict = {'jack':[15,'blond'], 'bob':[22,'bruin'], 'alice':[12,'rood']}

print(exdict)
'''
dit is een dictonary in een dictonary, om nu waarden uit te printen
doe je onderstaande
'''
print(exdict['jack'])
'''
dit print 15 en blond wil je enkel blond uitprinten dan
doe je onderstaande
'''
print(exdict['jack'][1])
'''of'''
print(exdict['jack'][0]) # de index plaats dus van je dictonary

