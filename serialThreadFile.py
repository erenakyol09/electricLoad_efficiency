import serial
from PyQt5.QtCore import pyqtSignal,QTime,QThread,QDateTime
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
        self.seriport.timeout  = 10000000000000

        self.seriport.a        = 1
        self.seriport.b        = 1
        self.seriport.run_data = 0

        self.seriport.Command = 0
        self.seriport.Mode    = 0
        self.seriport.Value   = 0

        self.seriport.second1 = 0
        self.seriport.second2 = 0
        self.seriport.second3 = 0

        self.seriport.y       = [0]
        self.seriport.y2      = [0]
        self.seriport.y3      = [0]
        self.seriport.y4      = [0]
        self.seriport.y5      = [0]

        self.seriport.sec1 = [0]
        self.seriport.sec2 = [0]
        self.seriport.sec3 = [0]

        self.receiveCrc = 0
        self.crc        = ""
        self.veri       = ""

        self.power   = ""
        self.voltage = ""
        self.current = ""

        # for current-voltage graph values
        self.cur     = ""
        self.volt    = ""

        self.packetC_P = ""
        self.packetC_U = ""
        self.packetC_J = ""
        self.packetC_p = ""
        self.packetC_f = ""
        self.packetC_V = ""
        self.packetC_I = ""

        self.packetA   = ""

        self.increase = 0
        self.sendTime   = 1/20 # sine wave frequency is 50 Hz. So, that's bigger than 20 ms
        self.C_sendTime = 1/50   # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

        self.xx = 0 #',' detector number for B'X'




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

                currentTime = QTime.currentTime()
                sn1 = currentTime.msec()
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
                    packet_size = int(self.veri[2]) * 10 + int(self.veri[3])
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

                        if self.veri[1] == 'P':
                            for i in range(packet_size - 1):
                                self.power = str(self.power + self.veri[i + 4])
                        self.mesaj1.emit(self.power)

                        if self.seriport.run_data == 1 and len(self.power) != 0:

                            self.seriport.second1 = self.seriport.second1 + self.increase
                            self.seriport.second1 = round(self.seriport.second1, 3)
                            self.seriport.y.append(float(self.power))
                            self.seriport.sec1.append(self.seriport.second1)
                            self.lcd2.emit(str(self.seriport.second1))
                            self.graph1.emit(self.seriport.sec1, self.seriport.y)
                            del self.seriport.y[0]
                            del self.seriport.sec1[0]

                        self.power = ""

                        if self.veri[1] == 'V':
                            for i in range(packet_size - 1):
                                self.voltage = str(self.voltage + self.veri[i + 4])
                        self.mesaj2.emit(self.voltage)

                        if len(self.voltage) != 0 and self.seriport.run_data == 1:

                            self.seriport.second2 = self.seriport.second2 + self.increase
                            self.seriport.second2 = round(self.seriport.second2, 3)
                            self.seriport.y2.append(float(self.voltage))
                            self.seriport.sec2.append(self.seriport.second2)
                            self.graph2.emit(self.seriport.sec2, self.seriport.y2)
                            del self.seriport.y2[0]
                            del self.seriport.sec2[0]

                        self.voltage = ""

                        if self.veri[1] == 'I':
                            for i in range(packet_size - 1):
                                self.current = str(self.current + self.veri[i + 4])
                        self.mesaj3.emit(self.current)

                        if len(self.current) != 0 and self.seriport.run_data == 1:

                            self.seriport.second3= self.seriport.second3 + self.increase
                            self.seriport.second3 = round(self.seriport.second3, 3)
                            self.seriport.y3.append(float(self.current))
                            self.seriport.sec3.append(self.seriport.second3)
                            self.graph3.emit(self.seriport.sec3, self.seriport.y3)
                            del self.seriport.y3[0]
                            del self.seriport.sec3[0]

                        self.current = ""


                        if self.veri[1] == 'X':
                            for i in range(packet_size - 1):
                                if self.veri[i + 4] == ',':
                                    self.xx = i
                                    break
                                self.cur = str(self.cur + self.veri[i + 4])
                            for i in range(packet_size - 1-len(self.cur)-1):
                                self.volt = str(self.volt + self.veri[i + 5 + self.xx])

                        if len(self.cur) != 0 and self.seriport.run_data == 1:

                            self.seriport.y4.append(float(self.cur))
                            self.seriport.y5.append(float(self.volt))
                            #self.graph4.emit(self.seriport.y4, self.seriport.y5)
                            #print(self.seriport.y4, self.seriport.y5)
                            del self.seriport.y4[0]
                            del self.seriport.y5[0]

                        self.cur  = ""
                        self.volt = ""

                        # CURRENT GRAPH PLOTTER
                        if self.seriport.Command == 'B' and self.seriport.Mode == 'I' and self.seriport.Value != 0:
                            allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                            #print("sended packets:", allData)
                            self.seriport.write(allData.encode())
                            time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms
                            currentTime5 = QTime.currentTime()
                            sn5 = currentTime5.msec()
                            self.increase = (sn5 - sn1)
                            print(self.increase)

                        # POWER GRAPH PLOTTER
                        if self.seriport.Command == 'B' and self.seriport.Mode == 'P' and self.seriport.Value != 0:
                            allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                            #print("sended packets:", allData)
                            self.seriport.write(allData.encode())
                            time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms
                            currentTime5 = QTime.currentTime()
                            sn5 = currentTime5.msec()
                            self.increase = abs(sn5 - sn1) / 1000
                            print(self.increase)

                        # VOLTAGE GRAPH PLOTTER
                        if self.seriport.Command == 'B' and self.seriport.Mode == 'V' and self.seriport.Value != 0:
                            allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                            #print("sended packets:", allData)
                            self.seriport.write(allData.encode())
                            time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms
                            currentTime5 = QTime.currentTime()
                            sn5 = currentTime5.msec()
                            self.increase = abs(sn5 - sn1) / 1000
                            print(self.increase)

                        if self.seriport.Command == 'B' and self.seriport.Mode == 'R' and self.seriport.Value != 0:
                            allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                            #print("sended packets:", allData)
                            self.seriport.write(allData.encode())
                            time.sleep(self.sendTime)
                            currentTime5 = QTime.currentTime()
                            sn5 = currentTime5.msec()
                            self.increase = abs(sn5 - sn1) / 1000
                            print(self.increase)


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

