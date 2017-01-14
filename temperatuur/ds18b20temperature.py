#!/usr/bin/python
# This file is: /usr/share/cacti/site/scripts/flow_temps.py

import os, glob, time, sys, datetime

#Set up the location of the DS18B20 sensors in the system
device_folder = glob.glob('/sys/bus/w1/devices/28*')
device_file = [device_folder[0] + '/w1_slave',device_folder[1] + '/w1_slave']

def read_temp_raw(): #A function that grabs the raw temp data from the sensors
   f_1 = open(device_file[0], 'r')
   lines_1 = f_1.readlines()
   f_1.close()
   f_2 = open(devicefrom Tkinter import *

colours = ['red','green','orange','white','yellow','blue']

r = 0
for c in colours:
    Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
    Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
    r = r + 1

mainloop()_file[1], 'r')
   lines_2 = f_2.readlines()
   f_2.close()
   return lines_1 + lines_2

def read_temp(): #A function to check the connection was good and strip out the temperature
   lines = read_temp_raw()
   while lines[0].strip()[-3:] != 'YES' or lines[2].strip()[-3:] != 'YES':
      time.sleep(0.2)
      lines = read_temp_raw()
   equals_pos = lines[1].find('t='), lines[3].find('t=')
   temp = float(lines[1][equals_pos[0]+2:])/1000, float(lines[3][equals_pos[1]+2:])/1000
   return temp

temp = read_temp() #get the temp
print('T1:'+str(temp[0])+' T2:'+str(temp[1]))
