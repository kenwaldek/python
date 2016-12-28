#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek
#
# Title: generator maken          Version:1.0
# Date: 28-12-16                           Language: python3
# Description: hier maken we onze eigen generatorr met de
# functie 'yield'
###############################################################
CORRECT_COMBO = (3, 6, 1)

# eerste manier om het te kunnen doen maar ingewikkelder
# en het programma loopt door tot alle cijfers overlopen zijn
# found_combo = False
# for c1 in range(10):
#     if found_combo:
#         break
#     for c2 in range(10):
#         if found_combo:
#             break
#     for c3 in range (101):
#         if (c1, c2, c3) == CORRECT_COMBO:
#             print('found combo: {}'.format((c1, c2, c3)))
#             found_combo = True
#             break
#         print(c1, c2, c3)

# beste manier is onderstaande we maken een generator met yield
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            yield (c1, c2, c3)

for (c11,  c2, c3) in combo_gen():
    print(c1, c2, c3 )
    if (c1, c2, c3) == CORRECT_COMBO:
        print('found the combo: {}'.format((c1, c2, c3)))
        break
    print(c1, c2, c3)














