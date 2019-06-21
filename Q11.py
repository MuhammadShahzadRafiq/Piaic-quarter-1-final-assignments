# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 16:39:30 2019

@author: Hacker
"""

x1 = int(input("Enter value of x1: "))
y1 = int(input("Enter value of y1: "))
x2 = int(input("Enter value of x2: "))
y2 = int(input("Enter value of y2: "))
e = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print('The distance between two points (',x1,',',y1,') and (',x2,',',y2,') is: ',e )