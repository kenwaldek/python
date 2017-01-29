#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license
#
# Title: kivy start                   Version: 1.0
# Date: 29-01-2017                    Language: python3
# Description: het begin programma om verder op te bouwen
#
###############################################################
# Share if you care, do something
import kivy

kivy.require('1.0.6')  # replace with your current kivy version !
from kivy.uix.boxlayout import BoxLayout  # je kan andere layouts gebruiken
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.button import Label

# groote van je kader
Config.set('graphics', 'width', '650')
Config.set('graphics', 'height', '400')


# hieronder kan je je kivy stuctuur plaatsen of op een andere file
Builder.load_string('''


''')

class Programma(BoxLayout):
    def __init__(self, **kwargs):
        super(Programma, self).__init__(**kwargs)

        self.add_widget(Label(text='did something'))


class Applicatie(App):
    def build(self):
        return Programma()


if __name__ == "__main__":
    Applicatie().run()
