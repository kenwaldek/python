#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek
#
# Title: multiprocessing                  Version: 1.0
# Date: 28-12-16                          Language: python3
# Description: multiprocessing dus  met meerdere cores te samen
#
###############################################################

import multiprocessing

def spawn():
    print('gebruik veel cores!')

if __name__ == "__main__":
    for i in range(20):
        p = multiprocessing.Process(target=spawn)
        p.start()
        p.join()  #deze brengt alle cores samen na uitvoering


### het programa oproepen in je terminal en uitvoeren
### je kan kijken naar je % van je processen als je wil
