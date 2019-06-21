# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:44:14 2019

@author: Hacker
"""

txt = input("Enter text: ")
alpa = num = spc = spe = 0

for e in range(len(txt)):
    if (txt[e].isalpha()):
        alpa = alpa + 1
    elif (txt[e].isdigit()):
        num = num + 1
    elif (txt[e] == " "):
        spc = spc + 1
    else:
        spe = spe + 1
print('numbers:',num)    
print('alphabats:',alpa)
print('Special Characters:',spe)
print('space:',spc)