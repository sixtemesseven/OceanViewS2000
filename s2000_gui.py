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
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from serial import SerialException
import serial
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

pg.mkQApp()

## Define main window class from template
path = os.path.dirname(os.path.abspath(__file__))
uiFile = os.path.join(path, 'ooadcGui/ooadcGui.ui')
WindowTemplate, TemplateBaseClass = pg.Qt.loadUiType(uiFile)








class MainWindow(TemplateBaseClass):  
    plotNr = 1
    channelActive = 0
    
    def __del__(self):
        self.ooS.__del__
        
    def __init__(self):
        #Set up main ui winows (goes first!)
        TemplateBaseClass.__init__(self)
        self.setWindowTitle('pyqtgraph example: Qt Designer')    
        
        # Create the main window
        self.ui = WindowTemplate()
        self.ui.setupUi(self)
        #Setup Serial Port
        self.ooS = ooadc.ooSpectro()
        self.portInput()
        #Get the calData for default Port(0) - Will be updated once channel is changed
        self.setChannel() 
        #Buttons
        self.ui.WriteCal.clicked.connect(self.updateCalData)
        self.ui.PlotSpectrum.clicked.connect(self.plotGraph)
        self.ui.Channel.clicked.connect(self.setChannel)
        self.ui.ResetDefaults.clicked.connect(self.resetDefaults)
        self.ui.ClearPlot.clicked.connect(self.clearPlot)
        self.ui.GetDarkMeasurment.clicked.connect(self.darkComp)
        self.ui.PlotCalCurve.clicked.connect(self.plotCalData) 
        #Spin Boxes on value changed
        self.ui.IntegrationTime.valueChanged.connect(self.setSpectrometer)
        self.ui.BoxcartWidth.valueChanged.connect(self.setSpectrometer)
        self.ui.Average.valueChanged.connect(self.setSpectrometer)
        self.ui.PlotFrom.valueChanged.connect(self.setSpectrometer)
        self.ui.PlotTo.valueChanged.connect(self.setSpectrometer)
        self.show()
    
    def updateCalData(self):
        #TODO Strong Warning before updating
        #TODO Change Cal Values
        return
    
    def portInput(self):
        PORT, okPressed = QInputDialog.getInt(None,"Get ADC1000 Serial Port","COM PORT:", 1, 0, 100, 1)
        if okPressed:
            if(self.ooS.connectCom(PORT)==False):
                msg = qt.QMessageBox()
                msg.setIcon(qt.QMessageBox.Information)
                msg.setText("\n Serial COM" + str(PORT) + " could not be opened! Check Port or Reboot\n ")
                msg.setWindowTitle("Serial Error")
                msg.exec_()
                print("COM Port not found error, exit program")
                sys.exit()
        
    def darkComp(self):
        self.ooS.getDarkCompensation(self.channelActive)
        
    #Sets Channel
    def setChannel(self):
        #Get the channel to be activated from the input spin box
        self.channelActive = self.ui.SingleChannel.value()
        #Set the new globaly active channel
        self.ooS.setChannel(self.channelActive)
        #get new cal data from eeprom
        self.calData = self.ooS.getCalData(self.channelActive)
        #calculate new Y axis range
        self.XScaleList = self.ooS.calculateXScale(self.calData)
        #Update cal value box
        self.ui.IValue.setValue(self.calData[0])
        self.ui.C0Value.setValue(self.calData[1])
        self.ui.C1Value.setValue(self.calData[2])
        self.ui.C2Value.setValue(self.calData[3])
        
    #Plotting the spectrum graph
    def plotGraph(self):
        if(self.ui.ApplyDarkMeasurment.isChecked()):
            Y = self.ooS.getSpectrum()
        else:
            Y = self.ooS.getCompdensatedSpectrum(self.channelActive)          
        X = self.XScaleList  
        
        #TODO -- TEST Matplotlib
        self.plotMatWidget.canvas.ax.plot(X, Y)
        self.plotMatWidget.canvas.draw()
        
        self.ui.graphicsView.plot(X,Y,name = " Nr: "+str(self.plotNr),pen=self.plotNr)       
        if(self.ui.ChangeColors.isChecked()):
            self.plotNr = self.plotNr + 1
            print(self.plotNr)
        
    #Clear old plots
    def clearPlot(self):
        self.ui.graphicsView.clear()
        self.plotNr = 1
        return
    
    '''
    Takes the current values of the cal data boxes and plots the fitting curve for checking
    '''    
    def plotCalData(self):
        I=self.ui.IValue.value() 
        C0=self.ui.C0Value.value()
        C1=self.ui.C1Value.value()
        C2=self.ui.C2Value.value()
        X = []
        for i in range(2046):
            X.append(I + i*C0 + i*C1*C1 + i*C2*C2*C2)
        w = self.ui.graphicsView.plot(X, name='Cal Coeff Curve', pen=self.plotNr)
        w.addLegend(offset=(60, 30))
        
            
                
        
    #Will trigger when spin box values change and will adjust spectrometer settings
    def setSpectrometer(self):
        self.ooS.setIntegrationTime(self.ui.IntegrationTime.value())
        self.ooS.setPixelBoxcardWidth(self.ui.BoxcartWidth.value())
        self.ooS.addScans(self.ui.Average.value())
        self.ooS.addScans(self.ui.PlotFrom.value())
        self.ooS.addScans(self.ui.APlotTo.value())
            
    def resetDefaults(self):
        #ooS.resetDefault
        self.ui.IntegrationTime.setValue(0)
        self.ui.BoxcartWidth.setValue(0)
        self.ui.Average.setValue(0)
        self.ui.PlotFrom.setValue(0)
        self.ui.PlotTo.setValue(2046)
        
        
win = MainWindow()


if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

