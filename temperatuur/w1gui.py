#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                           MIT-license
#
# Title: w1gui                          Version: 1.0
# Date: 27-12-16                        Language: python3
# Description: maken van een tkinter frame met kaders in
#
###############################################################

# bestand importeren, moet in dezelfde map stand
import ds18b20

# importeer tkinter als tk
import tkinter as tk
# importeer uit tkinter(grafische ondersteuning) ttk = grafisch nog beter
from tkinter import ttk
from tkinter import messagebox as tm


class Temp:
	def __init__(self):
		self._sensor  = ds18b20.DS18B20()
		self._tijd = 10
		self._gui()

	#methode definieren
	def _gui(self):
		#venster THERMOMETER opmaken
		self._venster = tk.Tk()
		self._venster.title('THERMOMETER')

		# variable toekennen aan veld temp
		self._temp = tk.DoubleVar()
		# waarde 0 toekennen, maar wordt direct overschreven door de temp waarde
		self._temp.set(0)
		# variable toekennen aan veld tmin
		self._tmin = tk.DoubleVar()
		# waarde 1000 toekennen
		self._tmin.set(1000)
		# variable toekennen aan veld tmax
		self._tmax = tk.DoubleVar()
		# waarde -1000 toekennen
		self._tmax.set(-1000)

		#EERSTE RIJ
		# label maken op eerste rij, anchor=uitlijnen naar rechts=E, grid=  labelcoordinaat
		tk.Label(self._venster, text= 'temp', font=('arial', 40), width=7, anchor=tk.E).grid(row=0, column=0)
		# temp aanduiding venster,andere kleur voor tempwaarde=bg='#cc0000', fg='#ffffff'
		tk.Label(self._venster, textvariable=self._temp,font=('arial', 40), width=5, bg='#cc0000', fg='#ffffff', anchor=tk.E).grid(row=0, column=1)
		# °C toevoeging venster
		tk.Label(self._venster, text='°C',font=('arial', 20), width=4, anchor=tk.E).grid(row=0, column=2)
		# horizontale lijn toevoegen, ook toekennen als venster
		ttk.Separator(self._venster).grid(row=1, columnspan=3)

		#TWEEDE RIJ
		# label maken op 2de rij, anchor=uitlijnen naar rechts=E, grid=  labelcoordinaat/ om colombreedte voorgaande overnemen > width=10 verwijderen & sticky=tk.E+tk.W toevoegen
		tk.Label(self._venster, text= 'min', font=('arial', 20), width=7, anchor=tk.E).grid(row=2, column=0)
		# min aanduiding venster,andere kleur voor tempwaarde=bg='#cc0000', fg='#ffffff'
		tk.Label(self._venster, textvariable=self._tmin,font=('arial', 20), bg='#6666cc', fg='#ffffff').grid(sticky=tk.E+tk.W,row=2, column=1)
		# °C toevoeging venster
		tk.Label(self._venster, text='°C',font=('arial', 20), width=4, anchor=tk.E).grid(row=2, column=2)
		# horizontale lijn toevoegen, ook toekennen als venster
		ttk.Separator(self._venster).grid(row=3, columnspan=3)

		#DERDE RIJ
		# label maken op 3de rij, anchor=uitlijnen naar rechts=E, grid=  labelcoordinaat
		tk.Label(self._venster, text= 'max', font=('arial', 20), width=7, anchor=tk.E).grid(row=4, column=0)
		# min aanduiding venster,andere kleur voor tempwaarde=bg='#cc0000', fg='#ffffff'
		tk.Label(self._venster, textvariable=self._tmax,font=('arial', 20), width=10, bg='#6666cc', fg='#ffffff').grid(row=4, column=1)
		# °C toevoeging venster
		tk.Label(self._venster, text='°C',font=('arial', 20), width=4, anchor=tk.E).grid(row=4, column=2)
		# horizontale lijn toevoegen, ook toekennen als venster
		ttk.Separator(self._venster).grid(row=5, columnspan=3)

		#VIERDE RIJ
		#button AFSLUITEN MAKEN
		tk.Button(self._venster, text='AFSLUITEN', command=self._afsluiten).grid(row=6,column=0, columnspan=3, sticky=tk.W+tk.E, ipady=8, padx=5, pady=4)

		self._meet()

		self._venster.mainloop()

	#tempwaarde meten in een loop
	def _meet(self):
		self._temp.set(float(self._sensor.meet()))
		# min waarde bijhouden en vgl met huidige waarde, en indien lager overschrijven
		self._tmin.set(min(self._tmin.get(), self._temp.get()))
		# min waarde bijhouden en vgl met huidige waarde, en indien hoger overschrijven
		self._tmax.set(max(self._tmax.get(), self._temp.get()))
		#meten om de 10 seconden
		self._venster.after(100 * self._tijd, self._meet)


	#knop afsluiten configureren
	def _afsluiten(self):
		if tm.askyesno('Afsluiten','Ben je zeker dat je wil afsluiten'):
			self._venster.quit()


if __name__ == '__main__':
	Temp()
