# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 23:11:49 2019

@author: justRandom
"""


import ooadc

spec1 = ooadc.ooSpectro(10)
print(spec1.getSpectrum())

del spec1 





'''
import serial 
import time
import matplotlib.pyplot as plt


s2000 = serial.Serial('COM10', 9600, timeout=1)
setToBinary = b'\x61\x41\x0D'
s2000.write(setToBinary)
time.sleep(0.1)
s2000.write(b'H0\x0D')
time.sleep(0.1)
s2000.write(b'I200\x0D')
time.sleep(0.1)
s2000.reset_output_buffer()
s2000.reset_input_buffer()
s2000.write(b'S\x0D')
rawStr = []
raw = []
rawStr = s2000.readline().decode("utf-8").split(" ")

for i in range(len(rawStr)-10):
    raw.append(int(rawStr[i+8]))
    
s2000.close() 

plt.plot(raw)
plt.show()
    

'''

    




