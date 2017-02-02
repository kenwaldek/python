#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license
#
# Title: countdown teller             Version: 1.0
# Date:     31-01-2017                Language: python3
# Description: een countdown timer functie
#
###############################################################
# Share if you care, do something

#!/usr/bin/python

import time

def countdown(count):
    while (count >= 0):
        print ('The count is: ', count)
        count -= 1
        time.sleep(1)

countdown(10)
print ("Good bye!")