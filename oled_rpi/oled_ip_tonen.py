#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license
#
# Title: print ip on oled ssd1306     Version: 1.0
# Date: 30-01-20117                   Language: python3
# Description: print het ip adress op je oled scherm
# wanneer je rpi opstart zodat je je ip weet
###############################################################
# Share if you care, do something

## voeg onderstaande toe aan /etc/rc.local
# sleep 30
# sudo python3 /home/pi/waar_je_script_opslaat.py

import os
import sys
from luma.core.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from PIL import ImageFont

## kijkt of dit script op raspberry pi uitgevoerd wordt zoniet error
if os.name != 'posix':
    sys.exit('{} platform not supported'.format(os.name))

## eth0 ip --> kies welke je wil eth0 of Wlan0
ipaddress = os.popen("ifconfig eth0 | grep 'inet addr' | awk -F: '{print $2}' | awk '{print $1}'").read()
#ipaddress = os.popen("ifconfig wlan0 | grep 'inet addr' | awk -F: '{print $2}' | awk '{print $1}'").read()

## kies je netwerk lan of wifi
toon_netwerk = 'eth0'
# toon_netwerk = 'wlan0'

## kies het gewenste oled type ssd1306, ssd1325, ssd1331, sh1106
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

## niet aankomen kiest het fonttype
font_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                         'fonts', 'C&C Red Alert [INET].ttf'))
font2 = ImageFont.truetype(font_path, 20)

## main programma niet aankomen
while True:
        with canvas(device) as draw:
            try:
                draw.rectangle(device.bounding_box, outline="white", fill="black")
                draw.text((10, 20), toon_netwerk, font=font2, fill="white")
                draw.text((10, 40), ipaddress, font=font2, fill="white")
            except KeyboardInterrupt:
                break