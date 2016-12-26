#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek
#
# Title: tkinter_image                Version: 1.0
# Date: 26-12-16                      Language: python3
# Description: tkinter inladen van image en text via menubar
#
###############################################################

from tkinter import Tk
from PIL import Image, ImageTk


class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('gui')
        self.pack(fill=BOTH, expand=1)
        # voegt een quit knop toe aan het frame
#       quit_button = Button(self, text='quit', command=self.client_exit)
#       quit_button.place(x=0, y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Exit', command= self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Show image', command=self.show_img)
        edit.add_command(label='Show txt', command=self.show_txt)
        menu.add_cascade(label='Edit', menu=edit)


    def client_exit(self):
        exit()

    def show_img(self):
        load = Image.open('pic.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def show_txt(self):
        text = Label(self, text='hello world from kenny')
        text.pack() # anders komt het niet op het scherm dus pack()


root = Tk()
root.geometry('400x300')
app = Window(root)
root.mainloop()
