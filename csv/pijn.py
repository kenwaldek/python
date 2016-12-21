#! /usr/bin/env python3
#  -*- coding:utf-8 -*-

from tkinter import *
import csv # module om csv files te kunnen handelen
import time # module om tijdsweergave te hebben, nog niet nodig

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.output()

    def output(self):
        # tekst en textveld datum
        datum = Label(self, text='datum:')
        datum.grid(row=1, column=0, padx=5, pady=3)
        self.e = Entry(self, width=10) # de definitie van het kader waar je in kan typen
        self.e.grid(row=1,column=1, padx=5, pady=3) # definitie van de grote van de grid

        # tekst en textveld pijn
        pijn = Label(self, text='pijn-ervaring:')
        pijn.grid(row=1, column=2, padx=5, pady=3)
        self.e1 = Entry(self, width=50)
        self.e1.grid(row=1, column=3, padx=5, pady=3)

        # aanmaak van button sla op
        self.b = Button(root, text='Sla op', command=self.writeToFile)
        self.b.grid(row=0, column=4, padx=5, pady=3)

    # schrijven naar csv file
    def writeToFile(self):
        with open('pijn.csv', 'a') as f: # de 'a' staat voor append (toevoegen)
                w=csv.writer(f, delimiter=',')
                w.writerow([self.e.get(), self.e1.get()])

if __name__ == "__main__":
        root=Tk()
        root.title('Pijn Logger') # dit is de titel
        root.geometry('1000x100') # groote van het kader
        app=App(master=root) # het aanroepen van de class App
        app.mainloop() # runnen van de applicatie
        root.mainloop() # loop programma
