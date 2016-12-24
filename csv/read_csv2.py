#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek
#
# Title: read csv file                  Version: 1.0
# Date: 24-12-16                        Language: python3
# Description: het inlezen van een csv file en data beheren
#
###############################################################

import csv

with open ("pijn.csv") as csvfile:
    read_csv = csv.reader(csvfile, delimiter=",")
    datums = []
    tijden = []

    for row in read_csv:
        datum = row[0]
        tijd = row[1]

        datums.append(datum)
        tijden.append(tijd)

    print(datums)
    print(tijden)
