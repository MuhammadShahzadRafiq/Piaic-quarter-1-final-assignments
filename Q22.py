# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:03:17 2019

@author: Hacker
"""
n = int(input('Enter numbers of raws: '))

for j in range(1, n+1):
    for i in range(1, j+1):
        print(i, end='')
    print()
 
    
    
for i in range(n-1, 0, -1):
    for j in range(1, i+1):
        print(j, end='')
    print()