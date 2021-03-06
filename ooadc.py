# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:50:11 2019

@author: justRandom

Wrapper class for all the RS232 functionality of the ADC1000 board from ocean optics
"""

#TODO Get a popup window on connect to open serial port 

import serial
import time
import numpy as np
from serial import SerialException

class ooSpectro:
        
        def __init__(self):
            self.s2000 = serial.Serial()
            
            
        def __del__(self):
            if(self.s2000.is_open == True):
                self.s2000.close()
            del self.s2000
            
        '''
        Connect to com port with 
        '''
        def connectCom(self, port):
            self.s2000.baud = 9600
            self.s2000.timeout = 10
            self.s2000.port = 'COM'+str(port)
            try:
                self.s2000.open()
            except SerialException:
                return False

            self.setAsciiMode()
            self.resetDefault()
            time.sleep(0.1)
            return True
        
        '''
        Sums up number of readings (1-15)
        '''
        def addScans(self, scans):
            self.s2000.write(b'A'+str(scans)+'\x0D')
            time.sleep(0.1)
        
        '''
        Sets number of pixels to sum together
        n specifies n to the right and n to the left
        n > 3 will slow things down
        '''                
        def setPixelBoxcardWidth(self, n):
            self.s2000.write(("B"+str(n)+"\x0D").encode())
            time.sleep(0.1)
        
        '''
        Sets data compression on or off
        Accepts 0 or 1
        '''            
        def setDataCompression(self, status):
            if(status == 0):
                self.s2000.write(b'G0\x0D')
            if(status == 1):
                self.s2000.write(b"G0!\x0D")
            else:
                print("setDataCompression out of range")
            time.sleep(0.1)
            
        '''
        Can be set to read one single adc channel at a time (0-7) 
        Or to use a rotator feature
        Rotator is active if chan > 255
        '''
        def setChannel(self, chan): 
            self.s2000.write(("H"+str(chan)+"\x0D").encode())
            time.sleep(0.1)
            
        '''
        Set integration time in milliseconds, range 5-65535
        '''
        def setIntegrationTime(self, intTime):
           self.s2000.write(('I'+str(intTime)+'\x0D').encode())
           time.sleep(0.1)
            
        '''
        TODO Lamp
        '''
        def setlamp(self):
            return
            
        '''
        TODO Baud rate
        '''            
        def changeBaudRate(self, time):
            return

        '''
        Sets which pixels are transmitted
        mode:
            0   2048
            1   Every nTh pixel 
            3   From x to y every nTh pixel
            4   10 selectable pixels, TODO
            
        '''
        def partialPixelMode(self, mode, n, x, y):
            if(mode == 0):
                self.s2000.write(b'P0\x0D')
            if(mode == 1):
                self.s2000.write(('P1'+str(n)+'\x0D').encode())
            if(mode == 3):
                self.s2000.write(('P3'+str(x)+str(y)+str(n)+'\x0D').encode())
            else:
                print("Partial Pixel Mode out of range")   
            time.sleep(0.1)
         
        '''
        Reset to default
        '''
        def resetDefault(self):
            self.s2000.write(b'Q\x0D')
            time.sleep(0.1)
            
        '''
        Returns list with measurments as set up before
        '''
        def getSpectrum(self):
            rawStr = []
            self.s2000.reset_output_buffer()
            self.s2000.reset_input_buffer()
            time.sleep(0.1)
            self.s2000.write(b'S\x0D')
            rawStr = self.s2000.readline().decode("utf-8").split(" ")          
            del rawStr[len(rawStr)-1]
            time.sleep(0.1) #Interesting, why???
            del rawStr[len(rawStr)-1]

            del rawStr[0:8]
            raw=[]
            for i in range(len(rawStr)):
                raw.append(int(rawStr[i]))
            return raw 
    
        '''
        Set trigger mode
        mode:
            0    Normal, continious
            1    Software trigger (?)
            2    External sync trigger (?)
            3    External hardware trigger
        '''
        def setTriggerMode(self, mode):
            self.s2000.write(b'T'+str(mode)+'\x0D')
            time.sleep(0.1)
            
        '''
        Set to ascii mode
        Should be called first (done at init)
        '''
        def setAsciiMode(self):
            setToBinary = b'\x61\x41\x0D'
            self.s2000.write(setToBinary)
            time.sleep(1)
    
        '''
        TODO
        '''
        def setBinaryMode(self, time):
            return

        '''
        TODO set strobe
        '''
        def setContiniousStrobeRate(self, time):
            return
            
        '''
        TODO Implement Checksum
        '''
        def setChecksumMode(self, time):
            self.s2000d.write(b'A\x0D')
            time.sleep(0.1)
        
        '''
        TODO version querry
        '''
        def queryVersion(self, time):
            return
            
        '''
        TODO Calibration 
        '''            
        def setCalCoeffiecents(self, time):
            return
        
        '''
        TODO identidy check
        '''
        def identify(self, time):
            return
            
        def getDarkCompensation(self, channel):
            self.setChannel(channel)
            dark = self.getSpectrum()
            np.savetxt('cal\darkComp_Channel'+str(channel)+'.txt', dark) #Save array to file
            return(dark)
            
            
        def getCompensatedSpectrum(self, channel):
            self.setChannel(channel)
            compensated = []
            measured = self.getSpectrum()
            dark = np.loadtxt('cal\darkComp_Channel'+str(channel)+'.txt') #Read array from file
            if(len(measured) != len(dark)):
                print("Lenghts of dark compensation does not match")
                return
            else:
                for i in range(len(dark)):
                    compensated.append(measured[i] - dark[i])
                return compensated
            
        def getCalData(self, channel):
            calVal = []
            for i in range(4):     
                eepromSlot = channel + 2 + i
                self.s2000.reset_output_buffer()
                self.s2000.reset_input_buffer()
                time.sleep(0.1)
                self.s2000.write(('?x'+str(eepromSlot)+'\x0D').encode())
                time.sleep(1)
                raw = self.s2000.read_until(b'>')
                raw = raw.replace(b"\x20", b"")
                raw = raw.replace(b"\r", b"")
                raw = raw.replace(b"\n", b"")
                raw = raw.replace(b"\x3E", b"")
                raw = raw.replace(b"\x06", b"")
                raw = raw.replace(("?x"+str(eepromSlot)).encode(), b"")  
                raw = raw.decode('utf-8')
                raw = float(raw)
                calVal.append(raw)
            return calVal
        
        def calculateXScale(self, calList):
            XScale = []
            for i in range(2047):
                XScale.append(calList[0] + i*calList[1] + i*calList[2]*calList[2] + i*calList[3]*calList[3]*calList[3])
            return XScale
            
            