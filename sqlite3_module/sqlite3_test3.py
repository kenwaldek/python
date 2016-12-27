#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek
#
# Title: sqlite3_test3                  Version: 1.0
# Date: 27-12-16                        Language: python3
# Description: het oproepen van een .db
#
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

def read_from_db():
    c.execute('SELECT * FROM stuf_to_plot WHERE value=8') # AND toevoegen om meerdere in te laden
    # c.execute('SELECT * FROM stuf_to_plot') # alles in data laden
    # data = c.fetchall() # command c.fetchall()is voor alles in data te laden
    # print(data)
    for row in c.fetchall(): # is een funktie die row uitleest
        print(row) # zijn alle rijen
        #print(row[0]) enkel de eerste rij uitprinten

read_from_db()
c.close()
conn.close()
