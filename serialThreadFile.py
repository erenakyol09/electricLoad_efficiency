import serial
from PyQt5.QtCore import pyqtSignal, QThread,QDateTime
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

    label = pyqtSignal(str)

    graph1  = pyqtSignal(list,list)
    graph2  = pyqtSignal(list,list)
    graph3  = pyqtSignal(list,list)
    graph4  = pyqtSignal(list,list)

    lcd     = pyqtSignal(str)
    lcd2    = pyqtSignal(str)


    def __init__(self, parent=None):
        super(serialThreadClass, self).__init__(parent)

        self.seriport = serial.Serial()
        self.seriport.baudrate = 1000
        self.seriport.port     = 'COM8'
        self.seriport.timeout  = 1000

        self.seriport.a        = 1
        self.seriport.run_data = 0

        self.seriport.Command = 0
        self.seriport.Mode    = 0
        self.seriport.Value   = 0

        self.seriport.second  = 0
        self.y       = [0]
        self.y2      = [0]
        self.y3      = [0]
        self.y4      = [0]

        self.sec     = [0]
        self.sec2    = [0]
        self.sec3    = [0]
        self.sec4    = [0]

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

        self.sendTime   = 1/4 # sine wave frequency is 50 Hz. So, that's bigger than 20 ms
        self.increase   = self.sendTime*4;
        self.C_sendTime = 1   # sine wave frequency is 50 Hz. So, that's bigger than 20 ms




    def run(self):

        self.label.emit("DEVICE CONNECTED")

        while self.seriport.a == 1:
            dataTime = QDateTime.currentDateTime()
            displayText = dataTime.toString('dd.MM.yyyy-hh:mm:ss')
            self.lcd.emit(displayText)

            # POWER GRAPH PLOTTER
            if self.seriport.Command == 'B' and self.seriport.Mode == 'P' and self.seriport.Value != 0:
                allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                print("sended packets:", allData)
                self.seriport.write(allData.encode())
                time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

            # VOLTAGE GRAPH PLOTTER
            if self.seriport.Command == 'B' and self.seriport.Mode == 'V' and self.seriport.Value != 0:
                allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                print("sended packets:", allData)
                self.seriport.write(allData.encode())
                time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

            # CURRENT GRAPH PLOTTER
            if self.seriport.Command == 'B' and self.seriport.Mode == 'I' and self.seriport.Value != 0:
                allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                print("sended packets:", allData)
                self.seriport.write(allData.encode())
                time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

            # RESISTOR GRAPH PLOTTER
            if self.seriport.Command == 'B' and self.seriport.Mode == 'R' and self.seriport.Value != 0:
                allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                print("sended packets:", allData)
                self.seriport.write(allData.encode())
                time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

            # C COMMAND GRAPH PLOTTER
            if self.seriport.Command == 'C':
                print("sended packets:", self.seriport.Command)
                self.seriport.write(self.seriport.Command.encode())
                time.sleep(self.C_sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms


            while self.seriport.in_waiting and self.seriport.a == 1:

                dataTime = QDateTime.currentDateTime()
                displayText = dataTime.toString('dd.MM.yyyy-hh:mm:ss')
                self.lcd.emit(displayText)

                readHex = self.seriport.readline()
                self.veri = readHex.decode()
                print("received packets:",self.veri)
                self.mesaj.emit(str(self.veri))
                ## A  command filter ##

                if self.veri[0] == 'A':
                    packet_size = int(self.veri[1]) * 10 + int(self.veri[2])
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
                    packet_size = int(self.veri[1]) * 10 + int(self.veri[2])
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

                        if len(self.packetB_P) != 0:
                            if self.seriport.run_data == 1:
                                self.y.append(float(self.packetB_P))
                                self.sec.append(self.seriport.second)
                                self.graph1.emit(self.sec, self.y)
                                del self.y[0]
                                del self.sec[0]
                                self.seriport.second = self.seriport.second + self.increase


                        # POWER GRAPH PLOTTER
                        if self.seriport.Command == 'B' and self.seriport.Mode == 'P' and self.seriport.Value != 0:
                            allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                            print("sended packets:", allData)
                            self.seriport.write(allData.encode())
                            time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

                        self.packetB_P = ""

                        if self.veri[3] == 'V':
                            for i in range(packet_size - 1):
                                self.packetB_V = self.packetB_V + self.veri[i + 4]
                        self.mesaj2.emit(str(self.packetB_V))

                        if len(self.packetB_V) != 0:
                            if self.seriport.run_data == 1:
                                self.y2.append(float(self.packetB_V))
                                self.sec2.append(self.seriport.second)
                                self.graph2.emit(self.sec2, self.y2)
                                del self.y2[0]
                                del self.sec2[0]

                        # VOLTAGE GRAPH PLOTTER
                        if self.seriport.Command == 'B' and self.seriport.Mode == 'V' and self.seriport.Value != 0:
                            allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                            print("sended packets:", allData)
                            self.seriport.write(allData.encode())
                            time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

                        self.packetB_V = ""

                        if self.veri[3] == 'I':
                            for i in range(packet_size - 1):
                                self.packetB_I = self.packetB_I + self.veri[i + 4]
                        self.mesaj3.emit(str(self.packetB_I))

                        if len(self.packetB_I) != 0:
                            if self.seriport.run_data == 1:
                                self.y3.append(float(self.packetB_I))
                                self.sec3.append(self.seriport.second)
                                self.graph3.emit(self.sec3, self.y3)
                                del self.y3[0]
                                del self.sec3[0]

                        # CURRENT GRAPH PLOTTER
                        if self.seriport.Command == 'B' and self.seriport.Mode == 'I' and self.seriport.Value != 0:
                            allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                            print("sended packets:", allData)
                            self.seriport.write(allData.encode())
                            time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

                        self.packetB_I = ""

                        if self.veri[3] == 'R':
                            for i in range(packet_size - 1):
                                self.packetB_R = self.packetB_R + self.veri[i + 4]
                        self.mesaj4.emit(str(self.packetB_R))

                        if len(self.packetB_R) != 0:
                            if self.seriport.run_data == 1:
                                self.y4.append(float(self.packetB_R))
                                self.sec4.append(self.seriport.second)
                                self.graph4.emit(self.sec4, self.y4)
                                del self.y4[0]
                                del self.sec4[0]

                        # RESISTOR GRAPH PLOTTER
                        if self.seriport.Command == 'B' and self.seriport.Mode == 'R' and self.seriport.Value != 0:
                            allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                            print("sended packets:", allData)
                            self.seriport.write(allData.encode())
                            time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

                        self.packetB_R = ""

                ## C  command filter ##

                if self.veri[0] == 'C':

                    packet_size = int(self.veri[1]) * 10 + int(self.veri[2])
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




