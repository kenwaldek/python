#! /usr/bin/env python3
#  -*- coding:utf-8 -*-

###############################################################
#  © kenwaldek                  MIT-license
#
# Title: time                   Version: 1.0
# Date:  21-12-16               Language: python3
# Description: testen van time module
################################################################
import time

t = time.asctime()
t2 = time.localtime()
t3 = time.clock()
t4 = time.ctime()
t5 = time.strftime("%H:%M:%S") # uur minuten seconden
# belangrijk dat je het format in een string plaatst
t6 = time.strftime("%Z") # is tijdszone
t7 = time.strftime("%x  %X") # gemakkelijkere manier
t8 = time.time() #aantel sec sinds 1970 tot nu
t9 = "niets"
print (t)
print (t2)
print (t3)
print (t4)
print (t5)
print (t6)
print (t7)
print (t8)
print (t9)
