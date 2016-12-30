#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                           GPL-license
#
# Title: timetest2                      Version: 1.0
# Date: 27-12-16                        Language: python3
# Description: tkinter module testje
#
###############################################################

from tkinter import *
from tkinter import ttk
import time

root = Tk()
time1 = ''
clock = Label(root, font=('times', 60, 'bold'), bg='red') # color red
clock.pack(fill=BOTH, expand=2)
def tick():
    global time1
    # get the current local time and day from the PC

    time2 = time.strftime('%H:%M:%S - %A') # day added %A
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)

    clock.after(200, tick)

tick()
root.mainloop()
