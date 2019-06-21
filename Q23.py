# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:10:41 2019

@author: Hacker
"""

n = int(input('Enter the number of raws: '))

for j in range(1, n+1):
    for i in range(1, j+1):
        print(j, end="")
        
    print()