#! /usr/bin/env python3
#  -*- coding:utf-8 -*-

from tkinter import * # module om gui te maken
import csv # module om csv files te kunnen handelen
from tkinter import ttk
import datetime
import time

t =  time.strftime("%x  %X") # gemakkelijkere manier
class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.output()

    def output(self):
        # tekst en textveld datum
        datum = Label(self, text= str(t))
        datum.grid(row=1, column=0, padx=5, pady=3)

        pijn = Label(self, text='pijn-ervaring:')
        pijn.grid(row=1, column=2, padx=5, pady=3)
        self.e1 = Entry(self, width=50)
        self.e1.grid(row=1, column=3, padx=5, pady=3)
        self.e1.focus_set() # deze regel is voor de cursor te plaatsen
        self.e1.bind("<Return>", self.writeToFile) # laat Enter key een functie uit te voeren
        # aanmaak van button sla op

        self.b = Button(root, text='Sla op of druk Enter', command=self.writeToFile)
        self.b.grid(row=0, column=4, padx=5, pady=3)



        self.b1 = Button(root, text='Nieuwe invoer ', command=self.output)
        self.b1.grid(row=2, column=0 )

        self.b2 = Button(root, text='AFSLUITEN ', command=self.Afsluiten)
        self.b2.grid(row=2, column=1 )



        # schrijven naar csv file
    def writeToFile(self, k=None):
        with open('pijn.csv', 'a') as f: # de 'a' staat voor append (toevoegen)
                w=csv.writer(f, delimiter=',')
                w.writerow([t, self.e1.get()])
    def Afsluiten(self):
        exit()
        # root.quit()

if __name__ == "__main__":
        root=Tk()
        root.title('Pijn Logger') # dit is de titel
        root.geometry('1000x100') # groote van het kader
        app=App(master=root) # het aanroepen van de class App
        app.mainloop() # runnen van de applicatie
        root.mainloop() # loop programma
