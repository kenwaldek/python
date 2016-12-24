#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek
#
# Title: read csv file                  Version: 1.0
# Date: 24-12-16                        Language: python3
# Description: het inlezen van een csv file en printen
#
###############################################################

import csv

with open ("pijn.csv") as csvfile:
    read_csv = csv.reader(csvfile, delimiter=",")
    for row in read_csv:

        #print(row[0])
        #print("#####")
        #print(row[0], row[1])
        print("#####")
        print(row[0], row[1], row[2])
        #######
