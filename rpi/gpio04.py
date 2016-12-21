#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox as tm
import RPi.GPIO as GPIO
import time
import threading

class Gui:
	def __init__(self):
		self._poorten = [5,6,7,8,9,10,11,12,13]
		self._aan = ['#FF0000','#FFFF00','#00FF00','#FF0000','#FFFF00','#00FF00','#FF0000','#FFFF00','#00FF00']
		self._uit = '#666666'
		self._tel = -1
		self._richting = 1
		self._bezig = True
		self._loop = True
		self._slaap = 0.1
		self._hardware()
		self._interface()

		th = threading.Thread(target=self._goforit)
		th.start()
		self._venster.mainloop()

	def _interface(self):
		self._venster = tk.Tk()
		self._venster.title('GPIO04: WALKING LIGHT')
		self._led = []
		for i in range(len(self._poorten)):
			self._led.append(None)
			self._led[i] = tk.Label(self._venster, bg = self._uit,width=8, height =4)
			self._led[i].grid(row=0, column=i,padx=1, pady=1)

		tk.Scale(self._venster, from_=0.1, to=0.5, resolution=0.025, orient=tk.HORIZONTAL,command=self._snelheid).grid(row=1,columnspan=len(self._poorten),sticky=tk.W + tk.E,ipady=3)

		tk.Button(self._venster, text='start/stop',command=self._startstop).grid(row=2, columnspan=len(self._poorten), sticky=tk.W + tk.E, ipady=10)
		tk.Button(self._venster, text='afsluiten',command=self._afsluiten).grid(row=3, columnspan=len(self._poorten), sticky=tk.W + tk.E, ipady=10)

	def _snelheid(self, waarde):
		self._slaap = float(waarde)

	def _startstop(self):
		self._loop = not(self._loop)

	def _afsluiten(self):
		if tm.askyesno('Afsluiten !','Afsluiten ?'):
			self.__del__()

	def _goforit(self):
		while self._bezig:
			while self._loop:
				if self._tel >=0:
					self._led[self._tel].configure(bg=self._uit)
					GPIO.output(self._poorten[self._tel], GPIO.LOW)
				self._tel += self._richting
				if self._tel == len(self._poorten)-1:
					self._richting = -1
				elif self._tel == 0:
					self._richting =1
				self._led[self._tel].configure(bg=self._aan[self._tel])
				self._venster.update()
				GPIO.output(self._poorten[self._tel],GPIO.HIGH)
				time.sleep(self._slaap)

	def _hardware(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self._poorten, GPIO.OUT)
		GPIO.output(self._poorten, GPIO.LOW)


	def __del__(self):
		self._loop = False
		self._bezig = False
		GPIO.cleanup()
		self._venster.quit()


if __name__ == '__main__':
	Gui()
