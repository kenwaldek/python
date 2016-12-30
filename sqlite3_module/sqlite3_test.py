#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                           GPL-license
#
# Title: sqlite3_test                   Version: 1.0
# Date: 27-12-16                        Language: python3
# Description: het maken van een .db in sqlite3
#
###############################################################
import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuf_to_plot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_intry():
    c.execute("INSERT INTO stuf_to_plot VALUES(123, '20-16-2016', 'python',5 )")
    conn.commit()
    c.close()
    conn.close()

# create_table() # dit moet je maar 1x runnen omdat table al gemaakt is
data_intry()

