#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license
#
# Title: oled and hc05             Version: 1.0
# Date: 30-01-2017                 Language: python3
# Description: measure distants and print on oled with rpi
#
###############################################################
# Share if you care, do something
import os
import time
import sys
from PIL import ImageFont
from luma.core.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import RPi.GPIO as GPIO

if os.name != 'posix':
    sys.exit('{} platform not supported'.format(os.name))

TRIG = 23  # Associate pin 23 to TRIG
ECHO = 24  # Associate pin 24 to ECHO
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)  # Set pin as GPIO out
GPIO.setup(ECHO, GPIO.IN)

while True:
  try:
    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    print ("Wachten op sensor")
    time.sleep(2)                            #Delay of 2 seconds

    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG, False)                 #Set TRIG as LOW

    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
      pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
      pulse_end = time.time()                #Saves the last known time of HIGH pulse

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points

    if distance > 2 and distance < 400:      #Check whether the distance is within range
      print ("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
    else:
      print ("Out Of Range")

    # font_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
    #                                          'fonts', 'C&C Red Alert [INET].ttf'))
    #
    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             'fonts', 'tiny.ttf'))
    ## soorten fonts + twee hierboven

    # FreePixel.ttf
    # miscfs_.ttf
    # pixelmix.ttf
    # ProggyTiny.ttf
    # tiny.ttf

    font2 = ImageFont.truetype(font_path, 20)
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((10, 20), str(distance) + ' cm', font=font2, fill="white")
        draw.text((10, 0), 'gemeten afstand', fill="white")
        draw.text((10, 40), 'hc 05 sensor',font=font2, fill="white")

        time.sleep(1)
  except KeyboardInterrupt:
    break

GPIO.cleanup()
