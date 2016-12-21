#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import alfabetmorse
import time
import tkinter as tk
import RPi.GPIO as GPIO


class Led:
	def __init__(self, poort):
		self._poort = poort
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self._poort,GPIO.OUT)
		GPIO.output(self._poort, GPIO.LOW)

	def __del__(self):
		GPIO.output(self._poort, GPIO.LOW)
		GPIO.cleanup()

	def schakel(self, status=0):
		status = GPIO.HIGH if status==1 else GPIO.LOW
		GPIO.output(self._poort,status)


class Morse:
	def __init__(self,poort=1, dot=1):
		self._dot = dot
		self._led = Led(poort)
		self._interface()

	def _interface(self):
		self._venster = tk.Tk()
		self._venster.title('MORSE')
		self._venster.resizable(0,0)

		self._ledon = tk.PhotoImage(file='led-on.gif')
		self._ledoff = tk.PhotoImage(file='led-off.gif')

		self._letter = tk.StringVar()

		tk.Label(self._venster,textvariable = self._letter, font=('Helvetica' ,48)).grid(row=0, column =0, pady=12, sticky=tk.E+tk.W)


		self._lblLed = tk.Label(self._venster, image=self._ledoff)
		self._lblLed.grid (row=0, column=1, pady=12,sticky=tk.E+tk.W)

		self._teken = tk.StringVar()
		self._teken.set('_.._')
		tk.Label(self._venster,textvariable=self._teken, font=('Helvetica' ,48)).grid(row=1, columnspan=2, pady=2, sticky=tk.E+tk.W)

		tk.Label(self._venster,text='Tik hier uw bootschap ..',anchor=tk.W).grid(row=2, columnspan=2, pady=2, sticky=tk.E+tk.W)

		self._tekst = tk.StringVar()
		self._tv = tk.Entry(self._venster, textvariable=self._tekst, width=40,font=('Helvetica',24))

		self._tv.bind("<Return>", self._verstuur)
		self._tv.grid(row=3, columnspan=2)
		self._tv.focus_set()

		self._bnVerstuur = tk.Button(self._venster, text='Verstuur', command=self._verstuur)
		self._bnVerstuur.grid(row=4, column=0 ,sticky=tk.E+tk.W, ipady=8)

		self._bnSluit= tk.Button(self._venster, text='Afsluiten', command=self._afsluiten)
		self._bnSluit.grid(row=4, column=1 ,sticky=tk.E+tk.W, ipady=8)

		self._venster.mainloop()

	def _afsluiten(self):
		del self._led
		self._venster.quit()


	def _verstuur(self, k=None):
		self._elementen()
		tekst = self._tekst.get().strip().upper()
		if len(tekst) > 0:
			self._verstuurTekst(tekst)

		self._letter.set('')
		self._teken.set('')
		self._tekst.set('')
		self._elementen(tk.NORMAL)
		self._tv.focus_set()


	def _verstuurTekst(self, tekst=''):
		for letter in tekst:
			if letter == '':
				time.sleep(3 * self._dot)
			else:
				try:
					tekens = alfabetmorse.alfabet[letter]
					self._letter.set(letter)
					dotstreep =''
					for teken in tekens:
						dotstreep += '__ ' if teken == '1' else' . '
					self._teken.set(dotstreep)
					#self._venster.update()
					for teken in tekens:
						tijd = self._dot if teken == '0' else 3 * self._dot
						self._lblLed.configure(image=self._ledon)
						self._venster.update()
						self._led.schakel(1)
						time.sleep(tijd)
						self._lblLed.configure(image=self._ledoff)
						self._venster.update()
						self._led.schakel(0)
						time.sleep(self._dot)

				except KeyError:
					pass

	def _elementen(self,status=tk.DISABLED):
		self._tv.configure(state=status)
		self._bnVerstuur.configure(state=status)
		self._bnSluit.configure(state=status)


if __name__ == '__main__':
	Morse(poort=23, dot=0.05)
