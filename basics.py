from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
import pyqtgraph as pg
import numpy as np
import ooadc
import serial
import serial.tools.list_ports



ssO = ooadc.ooSpectro()
ssO.connectCom(14)
print(ssO.getCalData(0))
ssO.__del__



'''
serial.tools.list_ports.comports()
ser = serial.Serial()
ser.baud = 9600
print(ser.is_open)
ser.port = 'COM14'
ser.open()
print(ser.is_open)
ser.close()
print(ser.is_open)
'''





'''

spec1 = ooadc.ooSpectro(14)
#print(spec1.getSpectrum())
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

    




