#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license
#
# Title: kivy rpi                     Version: 1.0
# Date: 19-01-2017                    Language: python3
# Description: kivy button with rpi
#
###############################################################
# Share if you care, do something
import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle

import RPi.GPIO as GPIO

# Set up GPIO:
ledPin1 = 17
ledPin2 = 18
ledPin3 = 24
ledPin4 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.output(ledPin1, GPIO.LOW)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.output(ledPin2, GPIO.LOW)
GPIO.setup(ledPin3, GPIO.OUT)
GPIO.output(ledPin3, GPIO.LOW)
GPIO.setup(ledPin4, GPIO.OUT)
GPIO.output(ledPin4, GPIO.LOW)

# Led toggle on/off
def press_callback(obj):
	print("Button pressed,", obj.text)
	if obj.text == 'LED1':
		if obj.state == "down":
			print ("button on 1")
			GPIO.output(ledPin1, GPIO.HIGH)
		else:
			print ("button off 1")
			GPIO.output(ledPin1, GPIO.LOW)
	if obj.text == 'LED2':
		if obj.state == "down":
			print ("button on 2")
			GPIO.output(ledPin2, GPIO.HIGH)
		else:
			print ("button off 2")
			GPIO.output(ledPin2, GPIO.LOW)
	if obj.text == 'LED3':
		if obj.state == "down":
			print("button on 3")
			GPIO.output(ledPin3, GPIO.HIGH)
		else:
			print("button off 3")
			GPIO.output(ledPin3, GPIO.LOW)
	if obj.text == 'LED4':
		if obj.state == "down":
			print("button on 4")
			GPIO.output(ledPin4, GPIO.HIGH)
		else:
			print("button off 4")
			GPIO.output(ledPin4, GPIO.LOW)


class MyApp(App):

	def build(self):
		# Set up the layout:
		layout = GridLayout(cols=5, spacing=30, padding=30, row_default_height=150)

		# Make the background gray:
		with layout.canvas.before:
			Color(.2,.2,.2,1)
			self.rect = Rectangle(size=(800,600), pos=layout.pos)


		# Create the rest of the UI objects (and bind them to callbacks, if necessary):
		outputControl1 = ToggleButton(text="LED1")
		outputControl1.bind(on_press=press_callback)
		outputControl2 = ToggleButton(text="LED2")
		outputControl2.bind(on_press=press_callback)
		outputControl3 = ToggleButton(text="LED3")
		outputControl3.bind(on_press=press_callback)
		outputControl4 = ToggleButton(text="LED4")
		outputControl4.bind(on_press=press_callback)


		# Add the UI elements to the layout:
		layout.add_widget(outputControl1)
		layout.add_widget(outputControl2)
		layout.add_widget(outputControl3)
		layout.add_widget(outputControl4)

		return layout

if __name__ == '__main__':
	MyApp().run()
