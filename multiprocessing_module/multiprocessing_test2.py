#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                             MIT-license
#
# Title: multiprocessing 2                Version: 1.0
# Date: 30-12-16                          Language: python3
# Description: multiprocessing dus  met meerdere cores te samen
#
###############################################################

from multiprocessing import Pool

def job(num):
    return num * 2

if __name__ == '__main__':
    p = Pool(processes=20)
    data = p.map(job, range(20))
    p.close()
    print(data)


