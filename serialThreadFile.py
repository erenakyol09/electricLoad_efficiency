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

        self.receiveCrc = 0
        self.crc = ""
        self.veri = ""



    def run(self):

        while self.seriport.a == 1:
            while self.seriport.in_waiting:
                readHex = self.seriport.readline()
                self.veri = readHex.decode()
                print(self.veri)
                time.sleep(1 / 100) # 1 ms waiting
                self.mesaj.emit(str(self.veri))

                # B  command filter
                if self.veri[0] == 'B':
                    packet_size  = int(self.veri[1]) + int(self.veri[2])
                    for i in range(packet_size):
                        self.receiveCrc = self.receiveCrc + readHex[i+3]

                    crc_str = hex(self.receiveCrc)
                    self.receiveCrc = 0
                    crc_lentgh = len(crc_str)

                    if crc_str[crc_lentgh - 3] == 'x':
                        self.crc = '0' + '0' + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]
                    if crc_str[crc_lentgh - 4] == 'x':
                        self.crc = '0' + crc_str[crc_lentgh - 3] + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]
                    if crc_str[crc_lentgh - 5] == 'x':
                        self.crc = crc_str[crc_lentgh - 4] + crc_str[crc_lentgh - 3] + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]

                    print(self.crc[crc_lentgh-4])
                    data_length = len(self.veri)
                    print(self.veri[data_length-packet_size-3])


                    # checkSum control
                    if self.veri[-1] == self.crc[-1] and self.veri[-2] == self.crc[-2] and self.veri[-3] == self.crc[-3] and self.veri[-4] == self.crc[-4]:
                        print("eren")

                    self.crc = ""


















