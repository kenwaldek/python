#! /usr/bin/env python3
#  -*- coding:utf-8 -*-

###############################################################
#      ©      ___                      __   ___
#       |__/ |__  |\ | |  |  /\  |    |  \ |__  |__/
#       |  \ |___ | \| |/\| /~~\ |___ |__/ |___ |  \
#
# Title: time test              Version: 1.0
# Date:  21-12-16               Language: python3
# Description: testen van tijd en datum module
#
###############################################################


import datetime
import time
#######
tijd = datetime.datetime.now()
print (tijd)
#######
datum = datetime.date.today()
print (datum)
#######
tijd1 = datetime.datetime.today()
print (tijd1)
