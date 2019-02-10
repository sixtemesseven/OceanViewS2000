# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 00:31:28 2019

@author: justRandom
"""
import pyqtgraph as pg

I = 1.80E+02


C1 = 3.74E-01


C2 = -1.20E-05


C3 = -2.82E-09



pTw = []

for i in range(2048):
    pTw.append(I+i*C1+i**2*C2+i**3*C3)
    
pg.plot(pTw)
pg.QtGui.QApplication.exec_()
    


