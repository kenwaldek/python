#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license
#
# Title: kivy A20                     Version: 1.0
# Date: 22-01-2017                    Language: python3
# Description: kivy button on the A20 micro from olimex
#
###############################################################
# Share if you care, do something
import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from pyA20.gpio import gpio
from pyA20.gpio import port
import os
import sys

if not os.getegid() == 0: # kijkt of je root bent
	sys.exit('script must be run as root!') # zoniet do...

# Set up GPIO definitions
ledPin1 = port.PG4
# init the GPIO
gpio.init()
# Set pins as output or input
gpio.setcfg(ledPin1, gpio.OUTPUT)

# Led toggle on/off
def press_callback(obj):
	print("Button pressed,", obj.text)
	if obj.text == 'LED 1':
		if obj.state == "down":
			print ("button on 1")
			gpio.output(ledPin1, 1)
		else:
			print ("button off 1")
			gpio.output(ledPin1, 1)


class MyApp(App):

	def build(self):
		# Set up the layout:
		layout = GridLayout(cols=5, spacing=30, padding=30, row_default_height=150)

		# Make the background gray:
		with layout.canvas.before:
			Color(.2,.2,.2,1)
			self.rect = Rectangle(size=(800,600), pos=layout.pos)

		# Create the rest of the UI objects (and bind them to callbacks, if necessary):
		outputControl1 = ToggleButton(text="LED 1")
		outputControl1.bind(on_press=press_callback)

		# Add the UI elements to the layout:
		layout.add_widget(outputControl1)

		return layout

if __name__ == '__main__':
	MyApp().run()