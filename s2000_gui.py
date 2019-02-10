# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 15:26:34 2019

@author: justRandom
"""

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import os
import random
import ooadc
import PyQt5.QtGui as qt
import time


pg.mkQApp()

## Define main window class from template
path = os.path.dirname(os.path.abspath(__file__))
uiFile = os.path.join(path, 'ooadcGui/ooadcGui.ui')
WindowTemplate, TemplateBaseClass = pg.Qt.loadUiType(uiFile)

ooS = ooadc.ooSpectro()


class MainWindow(TemplateBaseClass):  
    def __init__(self):
        TemplateBaseClass.__init__(self)
        self.setWindowTitle('pyqtgraph example: Qt Designer')
        
        # Create the main window
        self.ui = WindowTemplate()
        self.ui.setupUi(self)
        self.ui.PlotSpectrum.clicked.connect(self.plotGraph)
        self.ui.ConnectPort.clicked.connect(self.connectCom)
        self.ui.ResetDefaults.clicked.connect(self.resetDefaults)
        self.ui.ClearPlot.clicked.connect(self.clearPlot)
        
        self.ui.IntegrationTime.valueChanged.connect(self.setSpectrometer)
        self.ui.BoxcartWidth.valueChanged.connect(self.setSpectrometer)
        self.ui.Average.valueChanged.connect(self.setSpectrometer)
        self.ui.PlotFrom.valueChanged.connect(self.setSpectrometer)
        self.ui.PlotTo.valueChanged.connect(self.setSpectrometer)
        self.show()
        
    #Plotting the spectrum graph
    def plotGraph(self):
        X=[]
        for i in range(100):
            X.append(random.random())
        
        w = self.ui.graphicsView
        w.plot(X)
        

        
    #Clear old plots
    def clearPlot(self):
        self.ui.graphicsView.clear()
        return
        
        
    #Will trigger when spin box values change and will adjust spectrometer settings
    def setSpectrometer(self):
        ooS.setIntegrationTime(self.ui.IntegrationTime.value())
        ooS.setPixelBoxcardWidth(self.ui.BoxcartWidth.value())
        ooS.addScans(self.ui.Average.value())
        ooS.addScans(self.ui.PlotFrom.value())
        ooS.addScans(self.ui.APlotTo.value())
     
    #Connect com port, if it is open close the old one and reopen. If exception get popup
    def connectCom(self):
        port = self.ui.comPort.value()
        if(ooS.connectSpectrometer(port) == False):
            msg = qt.QMessageBox()
            msg.setIcon(qt.QMessageBox.Information)
            msg.setText("\n Serial COM" + str(port) + " could not be opened!\n ")
            msg.setWindowTitle("Serial Error")
            msg.exec_()
            
    def resetDefaults(self):
        #ooS.resetDefault
        self.ui.IntegrationTime.setValue(0)
        self.ui.BoxcartWidth.setValue(0)
        self.ui.Average.setValue(0)
        self.ui.PlotFrom.setValue(0)
        self.ui.PlotTo.setValue(2046)
        
        
win = MainWindow()


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

