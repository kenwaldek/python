#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           GPL-license
#
# Title: pickle module                Version: 1.0
# Date: 12-01-17                      Language: python3
# Description: some code to use with the pickle module
# serialisation and deserialisation
###############################################################

# do something
import pickle

## pickle out to file
example_dict = {1:'2',2:'5',3:'f'}
pickle_out = open('dict.pickle','wb')  # wb= write byte
pickle.dump(example_dict, pickle_out)
pickle_out.close()

# read pickle file in to terminal
pickle_in = open('dict.pickle','rb') # rb= read byte
example_dict = pickle.load(pickle_in)
print(example_dict)

# dictionary is {} en list is [] niet vergeten