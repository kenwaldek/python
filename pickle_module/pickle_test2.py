#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           GPL-license
#
# Title: pickle module 2              Version: 1.0
# Date: 12-01-17                      Language: python3
# Description: some code to use with the pickle module
# serialisation and deserialisation
###############################################################

# do something
import pickle

data = ("kenny")
data2 = [1,2,3]
data3 = 100
## schrijven naar een file
# output_file = open('pickledb.pk1', 'wb') # je kan je bestand noemen wat je wil alsook de extensie
# pickle.dump(data, output_file)
# pickle.dump(data2, output_file)
# pickle.dump(data3, output_file)
#
# output_file.close()

## uitlezen van pickle file
input_file = open('pickledb.pk1', 'rb')
data = pickle.load(input_file)
data2 = pickle.load(input_file)
data3 = pickle.load(input_file)
input_file.close()
print(str(data)) # string print gewoon omdat het kan
print(data2)
print(data3)
