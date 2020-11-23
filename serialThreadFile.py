import serial
from PyQt5.QtCore import pyqtSignal, QThread
import time
import numpy as np

class serialThreadClass(QThread):

    mesaj  = pyqtSignal(str)
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
        self.seriport.baudrate = 1000
        self.seriport.port = 'COM8'
        self.seriport.timeout = 1
        self.seriport.a = 1
        self.veri = 0

    def run(self):

        while self.seriport.a == 1:
            self.veri = self.seriport.readline().decode('ascii')
            time.sleep(1/100)
            self.mesaj.emit(str(self.veri))


