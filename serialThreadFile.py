import serial
from PyQt5.QtCore import pyqtSignal, QThread
import time


class serialThreadClass(QThread):

    mesaj  = pyqtSignal(str)
    mesaj1 = pyqtSignal(str)
    mesaj2 = pyqtSignal(str)
    mesaj3 = pyqtSignal(str)
    mesaj4 = pyqtSignal(str)

    mesaj5  = pyqtSignal(str)
    mesaj6  = pyqtSignal(str)
    mesaj7  = pyqtSignal(str)
    mesaj8  = pyqtSignal(str)
    mesaj9  = pyqtSignal(str)
    mesaj10 = pyqtSignal(str)
    mesaj11 = pyqtSignal(str)

    mesaj12 = pyqtSignal(str)


    def __init__(self, parent=None):
        super(serialThreadClass, self).__init__(parent)
        self.seriport = serial.Serial()
        self.seriport.baudrate = 1000
        self.seriport.port     = 'COM8'
        self.seriport.timeout  = 1
        self.seriport.a        = 1

        self.receiveCrc = 0
        self.crc        = ""
        self.veri       = ""


        self.packetB_P = ""
        self.packetB_V = ""
        self.packetB_I = ""
        self.packetB_R = ""

        self.packetC_P = ""
        self.packetC_U = ""
        self.packetC_J = ""
        self.packetC_p = ""
        self.packetC_f = ""
        self.packetC_V = ""
        self.packetC_I = ""

        self.packetA   = ""


    def run(self):

        while self.seriport.a == 1:
            while self.seriport.in_waiting:
                readHex = self.seriport.readline()
                self.veri = readHex.decode()
                print(self.veri)
                time.sleep(1 / 100) # 10 ms waiting
                self.mesaj.emit(str(self.veri))

                ## A  command filter ##

                if self.veri[0] == 'A':
                    packet_size = int(self.veri[1])*10 + int(self.veri[2])
                    for i in range(packet_size):
                        self.receiveCrc = self.receiveCrc + readHex[i + 3]

                    crc_str = hex(self.receiveCrc)
                    self.receiveCrc = 0
                    crc_lentgh = len(crc_str)

                    if crc_str[crc_lentgh - 3] == 'x':
                        self.crc = '0' + '0' + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]
                    if crc_str[crc_lentgh - 4] == 'x':
                        self.crc = '0' + crc_str[crc_lentgh - 3] + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]
                    if crc_str[crc_lentgh - 5] == 'x':
                        self.crc = crc_str[crc_lentgh - 4] + crc_str[crc_lentgh - 3] + crc_str[crc_lentgh - 2]
                        self.crc = self.crc + crc_str[crc_lentgh - 1]

                    veri_length = len(self.veri)
                    msg_Checksum = self.veri[3 + packet_size - veri_length] + self.veri[4 + packet_size - veri_length]
                    msg_Checksum = msg_Checksum + self.veri[5 + packet_size - veri_length]
                    msg_Checksum = msg_Checksum + self.veri[6 + packet_size - veri_length]


                    # checkSum control
                    if msg_Checksum == self.crc:
                        for i in range(packet_size):
                            self.packetA = self.packetA + self.veri[i + 3]
                    self.mesaj12.emit(str(self.packetA))
                    self.packetA = ""




                ## B  command filter ##

                if self.veri[0] == 'B':
                    packet_size = int(self.veri[1])*10 + int(self.veri[2])
                    for i in range(packet_size):
                        self.receiveCrc = self.receiveCrc + readHex[i + 3]

                    crc_str = hex(self.receiveCrc)
                    self.receiveCrc = 0
                    crc_lentgh = len(crc_str)


                    if crc_str[crc_lentgh - 3] == 'x':
                        self.crc = '0' + '0' + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]
                    if crc_str[crc_lentgh - 4] == 'x':
                        self.crc = '0' + crc_str[crc_lentgh - 3] + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]
                    if crc_str[crc_lentgh - 5] == 'x':
                        self.crc = crc_str[crc_lentgh - 4] + crc_str[crc_lentgh - 3] + crc_str[crc_lentgh - 2]
                        self.crc = self.crc + crc_str[crc_lentgh - 1]

                    veri_length = len(self.veri)
                    msg_Checksum = self.veri[3 + packet_size - veri_length] + self.veri[4 + packet_size - veri_length]
                    msg_Checksum = msg_Checksum + self.veri[5 + packet_size - veri_length]
                    msg_Checksum = msg_Checksum + self.veri[6 + packet_size - veri_length]

                    # checkSum control
                    if msg_Checksum == self.crc:

                            if self.veri[3] == 'P':
                                for i in range(packet_size - 1):
                                    self.packetB_P = self.packetB_P + self.veri[i + 4]
                            self.mesaj1.emit(str(self.packetB_P))
                            self.packetB_P = ""

                            if self.veri[3] == 'V':
                                for i in range(packet_size - 1):
                                    self.packetB_V = self.packetB_V + self.veri[i + 4]
                            self.mesaj2.emit(str(self.packetB_V))
                            self.packetB_V = ""

                            if self.veri[3] == 'I':
                                for i in range(packet_size - 1):
                                    self.packetB_I = self.packetB_I + self.veri[i + 4]
                            self.mesaj3.emit(str(self.packetB_I))
                            self.packetB_I = ""

                            if self.veri[3] == 'R':
                                for i in range(packet_size - 1):
                                    self.packetB_R = self.packetB_R + self.veri[i + 4]
                            self.mesaj4.emit(str(self.packetB_R))
                            self.packetB_R = ""



                ## C  command filter ##

                if self.veri[0] == 'C':

                    packet_size = 0
                    crc_str = ""


                    packet_size = int(self.veri[1])*10 + int(self.veri[2])
                    for i in range(packet_size):
                        self.receiveCrc = self.receiveCrc + readHex[i + 3]

                    crc_str = hex(self.receiveCrc)
                    self.receiveCrc = 0
                    crc_lentgh = len(crc_str)

                    if crc_str[crc_lentgh - 3] == 'x':
                        self.crc = '0' + '0' + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]
                    if crc_str[crc_lentgh - 4] == 'x':
                        self.crc = '0' + crc_str[crc_lentgh - 3] + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]
                    if crc_str[crc_lentgh - 5] == 'x':
                        self.crc = crc_str[crc_lentgh - 4] + crc_str[crc_lentgh - 3] + crc_str[crc_lentgh - 2]
                        self.crc = self.crc + crc_str[crc_lentgh - 1]

                    veri_length = len(self.veri)
                    msg_Checksum = self.veri[3 + packet_size - veri_length] + self.veri[4 + packet_size - veri_length]
                    msg_Checksum = msg_Checksum + self.veri[5 + packet_size - veri_length]
                    msg_Checksum = msg_Checksum + self.veri[6 + packet_size - veri_length]

                    # checkSum control
                    if msg_Checksum == self.crc:

                        if self.veri[3] == 'P':
                            for i in range(packet_size - 1):
                                self.packetC_P = self.packetC_P + self.veri[i + 4]
                        self.mesaj5.emit(str(self.packetC_P))
                        self.packetC_P = ""

                        if self.veri[3] == 'U':
                            for i in range(packet_size - 1):
                                self.packetC_U = self.packetC_U + self.veri[i + 4]
                        self.mesaj6.emit(str(self.packetC_U))
                        self.packetC_U = ""

                        if self.veri[3] == 'J':
                             for i in range(packet_size - 1):
                                self.packetC_J = self.packetC_J + self.veri[i + 4]
                        self.mesaj7.emit(str(self.packetC_J))
                        self.packetC_J = ""

                        if self.veri[3] == 'p':
                            for i in range(packet_size - 1):
                                self.packetC_p = self.packetC_p + self.veri[i + 4]
                        self.mesaj8.emit(str(self.packetC_p))
                        self.packetC_p = ""

                        if self.veri[3] == 'f':
                            for i in range(packet_size - 1):
                                self.packetC_f = self.packetC_f + self.veri[i + 4]
                        self.mesaj9.emit(str(self.packetC_f))
                        self.packetC_f = ""

                        if self.veri[3] == 'V':
                             for i in range(packet_size - 1):
                                self.packetC_V = self.packetC_V + self.veri[i + 4]
                        self.mesaj10.emit(str(self.packetC_V))
                        self.packetC_V = ""

                        if self.veri[3] == 'I':
                            for i in range(packet_size - 1):
                                self.packetC_I = self.packetC_I + self.veri[i + 4]
                        self.mesaj11.emit(str(self.packetC_I))
                        self.packetC_I = ""


































