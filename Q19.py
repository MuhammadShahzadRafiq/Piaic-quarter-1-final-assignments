# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:41:56 2019

@author: Hacker
"""


t = input("Enter Text: ")
t = t.casefold()
rev_txt = reversed(t)

if list(t) == list(rev_txt):
    print('Text',t,'is Palindrome')
else:
    print('Text',t,'is not Palindrome')