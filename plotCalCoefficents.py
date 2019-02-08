# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 00:31:28 2019

@author: justRandom
"""
import pyqtgraph as pg

I = 615.7191657

C1 = -2.529997169

C2 = 0.003911803

C3 = -1.52398E-06


pTw = []

for i in range(2048):
    pTw.append(I+i*C1+i**2*C2+i**3*C3)
    
pg.plot(pTw)
pg.QtGui.QApplication.exec_()
    


