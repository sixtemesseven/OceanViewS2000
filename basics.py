# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 23:11:49 2019

@author: justRandom
"""


import serial
s2000 = serial.Serial('COM9', 9600, timeout=100)
s2000.write('Aa\r')
s2000.write('H0')
s2000.write('I200')
s2000.write('S')

raw = []

while s2000.in_waiting:
    raw.append(s2000.read())
    
print(raw)
    




