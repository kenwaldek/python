#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                           MIT-license
#
# Title: sqlite3_test2                  Version: 1.0
# Date: 27-12-16                        Language: python3
# Description: het maken van een .db in sqlite3 via def
# dynamic_data_entry loop for i in range(10) maal dus de loop
###############################################################
import sqlite3
import time
import datetime
import random


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuf_to_plot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_intry():
    c.execute("INSERT INTO stuf_to_plot VALUES(123, '20-16-2016', 'python',5 )")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuf_to_plot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()

create_table() # moet je maar 1X laten runnen voor het maken van je database .db
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)

c.close()
conn.close()
