#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                         GPL-license
#
# Title: decorators test              Version: 1.0
# Date:  07-01-2017                   Language: python3
# Description: werken met decorators, wrappers voorbeelden
#
###############################################################

def Params(oldfunc):
    def inside(*args, **kwargs):
        print('Params: ', args, kwargs)
        return oldfunc(*args, **kwargs)
    return inside

@Params
def Mult(x, y=10):
    print(x*y)

Mult(4,4)  # 4X4=16
Mult(3)  # 3XY=10
Mult(x=1,y=3)  # 1X3=3

### de @Params print telkens de statement voor de Mult zie terminal
### je kan je code dus veel meer inkorten door decorators te gebruiken
