#! /usr/bin/env python3
#  -*- coding:utf-8 -*-

###############################################################
# GPL-license
#      ©      ___                      __   ___
#       |__/ |__  |\ | |  |  /\  |    |  \ |__  |__/
#       |  \ |___ | \| |/\| /~~\ |___ |__/ |___ |  \
#
# Title: datetime               Version: 1.0
# Date:  21-12-16               Language: python3
# Description: testen van datetime module
#
################################################################

import datetime
#######
tijd = datetime.datetime.now()
print ("tijd", tijd)
#######
tijd1 = datetime.datetime.today()
print ("tijd1", tijd1)
#######
datum = datetime.date.today()
print ("datum", datum)
print ("jaar", datum.year)
print ("maand", datum.month)
print ("dag", datum.day)
"""
je gemaakte variable en dan .statement erbij toevoegen
soms met () erachter soms zonder. zie hierboven
"""
from datetime import date
datum2 = date.today()
print ("datum2", datum2)
