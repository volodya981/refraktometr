# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 00:09:23 2022

@author: ierus
"""

a=int(input("Renta:"))
b=int(input("current finances:"))
c=int(input("year payment:"))
val=a*12*10*pow(1.07, 25)
print (val)
q=b*1.10
print(q)
time=0
while q<=val:
        q=(q+c)*1.10
        time=time+1
print(time)