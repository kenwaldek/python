#! /usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
# Zet waarschuwingen uit.
GPIO.setwarnings(False)

while (True):
        GPIO.output(23, True)
        time.sleep(0.5)
        GPIO.output(23, False)
        time.sleep(0.5)
