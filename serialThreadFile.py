import serial
from PyQt5.QtCore import pyqtSignal, QThread
import numpy as np

class serialThreadClass(QThread):

    mesaj = pyqtSignal(str)
    mesaj1 = pyqtSignal(str)
    mesaj2 = pyqtSignal(str)
    mesaj3 = pyqtSignal(str)
    mesaj4 = pyqtSignal(str)
    mesaj5 = pyqtSignal(str)
    mesaj6 = pyqtSignal(str)
    mesaj7 = pyqtSignal(str)


    def __init__(self, parent=None):
        super(serialThreadClass, self).__init__(parent)
        self.seriport = serial.Serial()
        self.seriport.baudrate = 9600
        self.seriport.port = 'COM8'
        self.seriport.timeout = 1
        self.seriport.a = 1

        self.i = 0
        self.k = 0
        self.z = 0

        self.buffer     = np.array([0, 0, 0, 0, 0, 0, 0, 0])
        self.firstCycle = np.array([0, 0, 0, 0, 0, 0, 0, 0])


    def run(self):

        self.z = 0
        self.i = 0

        #first cycle
        for self.k in range(0, 8):
            data = int(self.seriport.readline().decode('ascii'))
            self.firstCycle[self.k] = data
            if self.firstCycle[self.k] == int(7):
                break

        while self.seriport.a == 1:

            veri = int(self.seriport.readline().decode('ascii'))

            self.buffer[self.z] = veri

            #cycle

            # DC CURRENT
            self.mesaj1.emit(str(self.buffer[self.i]))
            # DC VOLTAGE
            self.mesaj2.emit(str(self.buffer[self.i + 1]))
            # AC CURRENT
            self.mesaj3.emit(str(self.buffer[self.i + 2]))
            # AC VOLTAGE
            self.mesaj4.emit(str(self.buffer[self.i + 3]))
            # DC CURRENT
            self.mesaj5.emit(str(self.buffer[self.i + 4]))
            # DC VOLTAGE
            self.mesaj6.emit(str(self.buffer[self.i + 5]))
            # NTC
            self.mesaj7.emit(str(self.buffer[self.i + 6]))

            if self.z == 7:
                self.z = 0
            else:
                self.z = self.z + 1

            self.mesaj.emit(str(veri))






