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
import matplotlib as plt
from matplotlib.widgets import Cursor
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)


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
        self.setMouseTracking(True)
        self.ui.MplWidget.setMouseTracking(True)
        self.ui.MplWidget.installEventFilter(self)
        self.addToolBar(NavigationToolbar(self.ui.MplWidget.canvas, self))
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
        for i in range(100):
            X.append(random.randint(0,1000))
        
        ##TODO -- TEST Matplotlib
        #self.ui.spectrumGraph.canvas.plot(X)
        #self.ui.spectrumGraph.canvas.draw()
        
        
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(X)
        self.ui.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        self.ui.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        cursor = Cursor(self.ui.MplWidget.canvas.axes, useblit=True, color='red', linewidth=2)
        self.ui.MplWidget.canvas.draw()
   

        
    #Clear old plots
    def clearPlot(self):
        self.ui.graphicsView.clear()
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
        
win = MainWindow()


if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

