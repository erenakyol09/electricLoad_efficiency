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
        with open("buffer.txt", "w") as file:
            file.write("")

        self.buffer = np.array([0, 0, 0, 0, 0, 0, 0,0])


    def run(self):
        while self.seriport.a == 1:
            veri  = int(self.seriport.readline().decode('ascii'))
            self.buffer[self.i] = veri

            if self.buffer[self.i] == np.int32(100):
                self.k = self.i

            self.mesaj.emit(str(veri))
            print(self.buffer[self.k])
            #NTC
            print(self.buffer[self.k - 1])
            self.mesaj7.emit(str(self.buffer[self.k - 1]))
            #DC VOLTAGE
            print(self.buffer[self.k - 2])
            self.mesaj6.emit(str(self.buffer[self.k - 2]))
            #DC CURRENT
            print(self.buffer[self.k - 3])
            self.mesaj5.emit(str(self.buffer[self.k - 3]))
            #AC VOLTAGE
            print(self.buffer[self.k - 4])
            self.mesaj4.emit(str(self.buffer[self.k - 4]))
            #AC CURRENT
            print(self.buffer[self.k - 5])
            self.mesaj3.emit(str(self.buffer[self.k - 5]))
            #DC VOLTAGE
            print(self.buffer[self.k - 6])
            self.mesaj2.emit(str(self.buffer[self.k - 6]))
            #DC CURRENT
            print(self.buffer[self.k - 7])
            self.mesaj1.emit(str(self.buffer[self.k - 7]))

            if self.i == 7:
                self.i = 0
            else:
                self.i = self.i + 1







