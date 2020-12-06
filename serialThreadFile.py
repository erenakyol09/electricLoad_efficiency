import serial
from PyQt5.QtCore import pyqtSignal, QThread,QTimer,QTime,QDateTime
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

    graph1  = pyqtSignal(list,list)
    graph2  = pyqtSignal(list,list)
    lcd     = pyqtSignal(str)
    lcd2    = pyqtSignal(str)


    def __init__(self, parent=None):
        super(serialThreadClass, self).__init__(parent)

        self.seriport = serial.Serial()
        self.seriport.baudrate = 1000
        self.seriport.port     = 'COM8'
        self.seriport.timeout  = 1

        self.seriport.a        = 1
        self.seriport.run_data = 0

        self.seriport.y    = [0]
        self.seriport.y2   = [0]

        self.seriport.sec  = [0]
        self.seriport.sec2 = [0]

        self.seriport.secP = [0]
        self.seriport.secV = [0]

        self.seriport.count = 0
        self.seriport.count2 = 0

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
            dataTime = QDateTime.currentDateTime()
            displayText = dataTime.toString('dd.MM.yyyy-hh:mm:ss')
            self.lcd.emit(displayText)
            while self.seriport.in_waiting:
                readHex = self.seriport.readline()
                self.veri = readHex.decode()
                print(self.veri)
                #time.sleep(1 / 100) # 10 ms waiting
                self.mesaj.emit(str(self.veri))

                currentTime = QTime.currentTime()
                sn = currentTime.second()

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

                            self.seriport.count = self.seriport.count + 1
                            if self.veri[3] == 'P':
                                for i in range(packet_size - 1):
                                    self.packetB_P = self.packetB_P + self.veri[i + 4]

                            self.mesaj1.emit(str(self.packetB_P))

                            if len(self.packetB_P) != 0:

                                if self.seriport.run_data == 1:

                                    self.seriport.sec.append(sn)

                                    if self.seriport.sec[1] != 0:
                                        self.seriport.count = self.seriport.sec[1] - self.seriport.sec[0]
                                        if self.seriport.count <= 1:
                                            self.seriport.secP.append(self.seriport.secP[0] + self.seriport.count)
                                    else:
                                        self.seriport.count = self.seriport.sec[0] - self.seriport.sec[1]
                                        self.seriport.secP.append(self.seriport.secP[0] + self.seriport.count)
                                        if self.seriport.count == 59:
                                            self.seriport.secP.append(self.seriport.secP[0] + 1)
                                            del self.seriport.secP[1]

                                    print(self.seriport.count)
                                    print(self.seriport.secP)
                                    self.seriport.y.append(float(self.packetB_P))
                                    self.graph1.emit(self.seriport.secP, self.seriport.y)
                                    del self.seriport.y[0]
                                    del self.seriport.sec[0]
                                    if self.seriport.count <= 1 or self.seriport.count == 59:
                                        del self.seriport.secP[0]

                            self.packetB_P = ""

                            if self.veri[3] == 'V':
                                for i in range(packet_size - 1):
                                    self.packetB_V = self.packetB_V + self.veri[i + 4]
                            self.mesaj2.emit(str(self.packetB_V))

                            if len(self.packetB_V) != 0:

                                if self.seriport.run_data == 1:

                                    self.seriport.sec2.append(sn)

                                    if self.seriport.sec2[1] != 0:
                                        self.seriport.count2 = self.seriport.sec2[1] - self.seriport.sec2[0]
                                        if self.seriport.count2 <= 1:
                                            self.seriport.secV.append(self.seriport.secV[0] + self.seriport.count2)
                                    else:
                                        self.seriport.count2 = self.seriport.sec2[0] - self.seriport.sec2[1]
                                        self.seriport.secV.append(self.seriport.secV[0] + self.seriport.count2)
                                        if self.seriport.count2 == 59:
                                            self.seriport.secV.append(self.seriport.secV[0] + 1)
                                            del self.seriport.secV[1]

                                    self.seriport.y2.append(float(self.packetB_V))
                                    self.graph2.emit(self.seriport.secV, self.seriport.y2)
                                    del self.seriport.y2[0]
                                    del self.seriport.sec2[0]
                                    if self.seriport.count2 <= 1 or self.seriport.count2 == 59:
                                        del self.seriport.secV[0]


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






























