#! /usr/bin/env python3
#  -*- coding:utf-8 -*-

import tkinter as tk
import tkinter.messagebox as tm
import RPi.GPIO as GPIO

leds = {'rood': [8, '#FF0000', '#990000'],
		'geel': [7, '#FFFF00', '#999900'],
		'groen': [9, '#00FF00', '#009900']}

class Gui:
	def __init__(self):
		self._no = -1 #welke led brand 0, 1 of 2

		self._venster = tk.Tk()
		self._venster.title('RPi GPIO 03')

		self._gpio()

		tk.Button(self._venster, text='PUSH', command=self._push).grid(row=1, column=0, columnspan=3, sticky=tk.W+tk.E, ipady=10, padx=5, pady=5)
		tk.Button(self._venster, text='EXIT', command=self._push).grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E, ipady=10, padx=5, pady=5)

		self._venster.mainloop()

	def _gpio(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		self._rood = tk.Label(self._venster, bg=leds['rood'][2], width=12, height=8)
		self._rood.grid(row=0, column=0, padx=5, pady=5)
		GPIO.setup(leds['rood'][0], GPIO.OUT)
		GPIO.output(leds['rood'][0], GPIO.LOW)

		self._geel = tk.Label(self._venster, bg=leds['geel'][2], width=12, height=8)
		self._geel.grid(row=0, column=1, padx=5, pady=5)
		GPIO.setup(leds['geel'][0], GPIO.OUT)
		GPIO.output(leds['geel'][0], GPIO.LOW)

		self._groen = tk.Label(self._venster, bg=leds['groen'][2], width=12, height=8)
		self._groen.grid(row=0, column=2, padx=5, pady=5)
		GPIO.setup(leds['groen'][0], GPIO.OUT)
		GPIO.output(leds['groen'][0], GPIO.LOW)

	def _push(self):
		pass

	def _afsluiten(self):
		if tk.Button('AFSLUITEN','Ben je zeker dat je wil afsluiten?'):
			GPIO.cleanup()
			venster.quit()

if __name__ == '__main__':
	Gui()
