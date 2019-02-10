import pyqtgraph as pg
import numpy as np
import ooadc

ss = ooadc.ooSpectro()
print(ss.connectSpectrometer(15))




'''

spec1 = ooadc.ooSpectro(14)
#print(spec1.getSpectrum())n
ch = 0
spec1.setIntegrationTime(200)
#spec1.doDarkCompensation(ch)
yAxis = np.loadtxt('cal/H0X.txt') #Read array from file
pg.plot(yAxis, spec1.getCompensatedSpectrum(ch))
del spec1 


import serial 
import time
import matplotlib.pyplot as plt


s2000 = serial.Serial('COM10', 9600, timeout=1)
setToBinary = b'\x61\x41\x0D'
s2000.write(setToBinary)
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
print(len(rawStr))

for i in range(len(rawStr)-10):
    raw.append(int(rawStr[i+8]))
    
s2000.close() 
'''

    




