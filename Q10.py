# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 16:18:14 2019

@author: Hacker
"""

P = float(input("Enter principle value: "))
Time = int(input("Enter numbers of years for investment: "))
rate = float(input("Enter rate of interest in %: "))
d = 0
e = P * rate * 10
while d < Time:
    e += e * rate
    d += 1



print('After',Time,'year your principal amount',P,'over an interest rate of ',rate,'will be: ',e)