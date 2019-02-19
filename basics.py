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
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from colour import Color
from matplotlib.colors import LinearSegmentedColormap

pg.mkQApp()

## Define main window class from template
path = os.path.dirname(os.path.abspath(__file__))
uiFile = os.path.join(path, 'ooadcGui/ooadcGui.ui')
WindowTemplate, TemplateBaseClass = pg.Qt.loadUiType(uiFile)



class MainWindow(TemplateBaseClass):  
    plotNr = 1
    channelActive = 0
    
    def __del__(self):
        return
        
    def __init__(self):
        #Set up main ui winows (goes first!)
        TemplateBaseClass.__init__(self)
        self.setWindowTitle('pyqtgraph example: Qt Designer')    
        
        # Create the main window
        self.ui = WindowTemplate()
        self.ui.setupUi(self)
        #Buttons
        self.ui.PlotSpectrum.clicked.connect(self.plotGraph)
        self.setMouseTracking(False)
        self.ui.MplWidget.setMouseTracking(False)
        self.ui.MplWidget.installEventFilter(self)
        self.addToolBar(NavigationToolbar(self.ui.MplWidget.canvas, self))
        self.ui.ClearPlot.clicked.connect(self.clearPlot)
        self.show()
        
    def eventFilter(self, object, event):
        if (event.type() == QtCore.QEvent.MouseMove):
            pos = event.pos()
            print("%d, %d" % (pos.x(), pos.y()))
        return QtGui.QWidget.eventFilter(self, object, event)

    def mouseMoveEvent(self, event):
        print("Moved")
        
    def updateCalData(self):
        return
    
    def portInput(self):
        return
        
    def darkComp(self):
        return
        
    #Sets Channel
    def setChannel(self):
        return
        
    #Plotting the spectrum graph
    def plotGraph(self):
        X = []
        Y = []
        for i in range(1000):
            Y.append(random.randint(0,1000))
            X.append(i)
        
        ##TODO -- TEST Matplotlib
        #self.ui.spectrumGraph.canvas.plot(X)
        #self.ui.spectrumGraph.canvas.draw()
        
        self.ui.MplWidget.canvas.axes.clear()
        
        self.ui.MplWidget.canvas.axes.plot(X,Y)
        #self.ui.MplWidget.canvas.axes.plot_cmap('summer',20)
        
        self.ui.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        self.ui.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.ui.MplWidget.canvas.draw()
        
    #Clear old plots
    def clearPlot(self):
        self.ui.MplWidget.canvas.axis.clear
        self.plotNr = 1
        return
    
    '''
    Takes the current values of the cal data boxes and plots the fitting curve for checking
    '''    
    def plotCalData(self):
        return                
        
    #Will trigger when spin box values change and will adjust spectrometer settings
    def setSpectrometer(self):
        return
            
    def resetDefaults(self):
        return
    
    
    def wavelengthToRgbCmap(self, startW, stopW, gamma=0.8):
        cList = []
        for i in range(stopW-startW):  
            wavelength = float(startW+i)
            if wavelength >= 380 and wavelength <= 440:
                attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
                R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
                G = 0.0
                B = (1.0 * attenuation) ** gamma
            elif wavelength >= 440 and wavelength <= 490:
                R = 0.0
                G = ((wavelength - 440) / (490 - 440)) ** gamma
                B = 1.0
            elif wavelength >= 490 and wavelength <= 510:
                R = 0.0
                G = 1.0
                B = (-(wavelength - 510) / (510 - 490)) ** gamma
            elif wavelength >= 510 and wavelength <= 580:
                R = ((wavelength - 510) / (580 - 510)) ** gamma
                G = 1.0
                B = 0.0
            elif wavelength >= 580 and wavelength <= 645:
                R = 1.0
                G = (-(wavelength - 645) / (645 - 580)) ** gamma
                B = 0.0
            elif wavelength >= 645 and wavelength <= 750:
                attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
                R = (1.0 * attenuation) ** gamma
                G = 0.0
                B = 0.0
            #Cannot be displayed, show as grey
            else:
                R = 0.3
                G = 0.3
                B = 0.3
            cList.append(Color(rgb=(R,G,B)))
        cmap = LinearSegmentedColormap('spectrumColor', cList)
        return(cmap)

win = MainWindow()


if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

