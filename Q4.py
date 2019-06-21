# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 07:37:32 2019

@author: Hacker
"""

from datetime import date 
  
def numOfDays(date1, date2): 
    return (date2-date1).days 
      
# Driver program 
a=str(input("Enter a date in (dd/mm/yy) format:"))

b=str(input("Enter a date in (dd/mm/yy) format:"))
x = a.split("/")
my_ints = [int(l[0]) for l in x]
x=int(x)
date1 = date(2018, 12, 13) 
date2 = date(2019, 2, 25) 
print(numOfDays(date1, date2), "days")



dts = input("Enter a date in (dd/mm/yy) format: 12/12/2018")
dte = input("Enter a date in (dd/mm/yy) format: 16/12/2018")
x = int(dts[:2])
y = int(dte[:2])
res = y-x
print("There are "+str(res)+" days in between "+dts+" and "+dte)