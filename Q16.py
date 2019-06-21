# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:31:38 2019

@author: Hacker
"""

num = int(input("Enter a number in decimal "))

binary = bin(num)

print('Binary Representation of',num,'is',binary[2:])