# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:58:26 2019

@author: Hacker
"""

n = int(input('Enter the numbers of raws: '))

for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end=' ')
    print()



for i in range(n-1, 0, -1):
    for j in range(i, 0, -1):
        print('*', end=' ')
    print()