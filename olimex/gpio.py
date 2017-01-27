#!/usr/bin/env python3

from pyA20.gpio import gpio
from pyA20.gpio import port
import time

gpio.init()

led = port.PG9

gpio.setcfg(led, gpio.OUTPUT)
# gpio.setcfg(led, 1) is hetzelfde

while (True):
    gpio.output(led, gpio.LOW)
    time.sleep(0.5)
    gpio.output(led, gpio.HIGH)
    time.sleep(0.5)
