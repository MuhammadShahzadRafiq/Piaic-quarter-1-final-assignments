# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:39:28 2019

@author: Hacker
"""

a = input("Enter Text: ")
b = 0;
c = 0;
for d in a:
    if d == 'A' or d == 'a' or d == 'E' or d == 'e' or d == 'I' or d == 'i' or d == 'O' or d == 'o' or d == 'U' or d == 'u':
        b+=1
    else:
        c+=1
print("Vowels:",b,"\nConsonants:",c)