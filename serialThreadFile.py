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

    lcd     = pyqtSignal(str)
    lcd2    = pyqtSignal(str)


    def __init__(self, parent=None):
        super(serialThreadClass, self).__init__(parent)

        self.seriport = serial.Serial()
        self.seriport.baudrate = 1000
        self.seriport.port     = 'COM8'
        self.seriport.timeout  = 1

        self.seriport.a          = 1
        self.seriport.txt_graph  = ""
        self.seriport.run_data   = 0

        self.seriport.Command = 0
        self.seriport.Mode    = 0
        self.seriport.Value   = 0

        self.seriport.x  = [0,0]
        self.seriport.y  = [0,0]

        self.seriport.x2 = [0,0]
        self.seriport.y2 = [0,0]


        self.seriport.y3      = [0]
        self.seriport.y4      = [0]
        self.seriport.y5      = [0]

        self.receiveCrc = 0
        self.crc        = ""

        self.power   = ""
        self.voltage = ""
        self.current = ""

        self.packetC_P = ""
        self.packetC_U = ""
        self.packetC_J = ""
        self.packetC_p = ""
        self.packetC_f = ""
        self.packetC_V = ""
        self.packetC_I = ""

        self.packetA   = ""

        self.increase = 0
        self.sendTime   = 1/50   # sine wave frequency is 50 Hz. So, that's bigger than 20 ms
        self.C_sendTime = 0   # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

        self.readHex = ['','','','','','','','','','',]
        self.veri    = ['','','','','','','','','','',]





    def run(self):

        self.label.emit("DEVICE CONNECTED")

        while self.seriport.a == 1:

            dataTime = QDateTime.currentDateTime()
            displayText = dataTime.toString('dd.MM.yyyy-hh:mm:ss')
            self.lcd.emit(displayText)

            # POWER GRAPH PLOTTER
            if self.seriport.Command == 'B' and self.seriport.Mode == 'P' and self.seriport.Value != 0:
                allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                #print("sended packets:", allData)
                self.seriport.write(allData.encode())
                time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

            # VOLTAGE GRAPH PLOTTER
            if self.seriport.Command == 'B' and self.seriport.Mode == 'V' and self.seriport.Value != 0:
                allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                #print("sended packets:", allData)
                self.seriport.write(allData.encode())
                time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

            # CURRENT GRAPH PLOTTER
            if self.seriport.Command == 'B' and self.seriport.Mode == 'I' and self.seriport.Value != 0:
                allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                #print("sended packets:", allData)
                self.seriport.write(allData.encode())
                time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

            # RESISTOR GRAPH PLOTTER
            if self.seriport.Command == 'B' and self.seriport.Mode == 'R' and self.seriport.Value != 0:
                allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                #print("sended packets:", allData)
                self.seriport.write(allData.encode())
                time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

            # C COMMAND GRAPH PLOTTER
            if self.seriport.Command == 'C':
                #print("sended packets:", self.seriport.Command)
                self.seriport.write(self.seriport.Command.encode())
                time.sleep(self.C_sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms
            dataTime = QDateTime.currentDateTime()
            displayText = dataTime.toString('dd.MM.yyyy-hh:mm:ss')
            self.lcd.emit(displayText)

            while self.seriport.in_waiting:

                dataTime = QDateTime.currentDateTime()
                displayText = dataTime.toString('dd.MM.yyyy-hh:mm:ss')
                self.lcd.emit(displayText)

                index = 0
                while 1:
                    self.readHex[index] = self.seriport.readline()
                    self.veri[index] = self.readHex[index].decode()
                    self.mesaj.emit(str(self.veri[index]))
                    if len((self.veri[index])) == 0:
                        break
                    index = index + 1
                print(index)
                print(self.veri[0])
                print(self.veri[1])
                print(self.veri[2])

                ## A  command filter ##
                for i in range(index):

                    if self.veri[i][0] == 'A':
                        packet_size = int(self.veri[i][1]) * 10 + int(self.veri[i][2])
                        for l in range(packet_size):
                            self.receiveCrc = self.receiveCrc + self.readHex[i][l + 3]

                        crc_str = hex(self.receiveCrc)
                        self.receiveCrc = 0
                        crc_lentgh = len(crc_str)

                        if crc_str[crc_lentgh - 3] == 'x':
                            self.crc = '0' + '0' + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]
                        if crc_str[crc_lentgh - 4] == 'x':
                            self.crc = '0' + crc_str[crc_lentgh - 3] + crc_str[crc_lentgh - 2] + crc_str[
                                crc_lentgh - 1]
                        if crc_str[crc_lentgh - 5] == 'x':
                            self.crc = crc_str[crc_lentgh - 4] + crc_str[crc_lentgh - 3] + crc_str[crc_lentgh - 2]
                            self.crc = self.crc + crc_str[crc_lentgh - 1]

                        veri_length = len(self.veri[i])
                        msg_Checksum = self.veri[i][3 + packet_size - veri_length] + self.veri[i][
                            4 + packet_size - veri_length]
                        msg_Checksum = msg_Checksum + self.veri[i][5 + packet_size - veri_length]
                        msg_Checksum = msg_Checksum + self.veri[i][6 + packet_size - veri_length]

                        # checkSum control
                        if msg_Checksum == self.crc:
                            for k in range(packet_size):
                                self.packetA = self.packetA + self.veri[i][k + 3]
                        self.mesaj12.emit(str(self.packetA))

                        self.packetA = ""

                ## B  command filter ##
                for i in range(index):
                    if self.veri[i][0] == 'B':
                        packet_size = int(self.veri[i][2]) * 10 + int(self.veri[i][3])
                        for l in range(packet_size):
                            self.receiveCrc = self.receiveCrc + self.readHex[i][l + 3]

                        crc_str = hex(self.receiveCrc)
                        self.receiveCrc = 0
                        crc_lentgh = len(crc_str)

                        if crc_str[crc_lentgh - 3] == 'x':
                            self.crc = '0' + '0' + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]
                        if crc_str[crc_lentgh - 4] == 'x':
                            self.crc = '0' + crc_str[crc_lentgh - 3] + crc_str[crc_lentgh - 2] + crc_str[
                                crc_lentgh - 1]
                        if crc_str[crc_lentgh - 5] == 'x':
                            self.crc = crc_str[crc_lentgh - 4] + crc_str[crc_lentgh - 3] + crc_str[
                                crc_lentgh - 2]
                            self.crc = self.crc + crc_str[crc_lentgh - 1]

                        veri_length = len(self.veri[i])
                        msg_Checksum = self.veri[i][3 + packet_size - veri_length] + self.veri[i][
                            4 + packet_size - veri_length]
                        msg_Checksum = msg_Checksum + self.veri[i][5 + packet_size - veri_length]
                        msg_Checksum = msg_Checksum + self.veri[i][6 + packet_size - veri_length]

                        # checkSum control
                        if msg_Checksum == self.crc:

                            if self.veri[i][1] == 'P':
                                for k in range(packet_size - 1):
                                    self.power = str(self.power + self.veri[i][k + 4])
                            self.mesaj1.emit(self.power)

                            if self.veri[i][1] == 'V':
                                for k in range(packet_size - 1):
                                    self.voltage = str(self.voltage + self.veri[i][k + 4])
                            self.mesaj2.emit(self.voltage)

                            if self.veri[i][1] == 'I':
                                for k in range(packet_size - 1):
                                    self.current = str(self.current + self.veri[i][k + 4])
                            self.mesaj3.emit(self.current)

                print(self.power)
                print(self.voltage)
                print(self.current)

                if self.seriport.txt_graph == "I-V" and self.seriport.run_data == 1:

                    self.seriport.y[1] = float(self.current)
                    self.seriport.x[1] = float(self.voltage)
                    self.seriport.y.append(float(self.current))
                    self.seriport.x.append(float(self.voltage))
                    self.seriport.x2[0],self.seriport.x2[1] = self.seriport.x[0],self.seriport.x[1]
                    self.seriport.y2[0], self.seriport.y2[1] = self.seriport.y[0], self.seriport.y[1]
                    self.graph1.emit(self.seriport.x2, self.seriport.y2)
                    del self.seriport.x[0]
                    del self.seriport.y[0]


                if self.seriport.txt_graph == "P-V" and self.seriport.run_data == 1:

                    self.seriport.y[1] = float(self.power)
                    self.seriport.x[1] = float(self.voltage)
                    self.seriport.y.append(float(self.power))
                    self.seriport.x.append(float(self.voltage))
                    self.seriport.x2[0], self.seriport.x2[1] = self.seriport.x[0], self.seriport.x[1]
                    self.seriport.y2[0], self.seriport.y2[1] = self.seriport.y[0], self.seriport.y[1]
                    self.graph1.emit(self.seriport.x2, self.seriport.y2)
                    del self.seriport.x[0]
                    del self.seriport.y[0]

                if self.seriport.txt_graph == "V-I" and self.seriport.run_data == 1:

                    self.seriport.y[1] = float(self.voltage)
                    self.seriport.x[1] = float(self.current)
                    self.seriport.y.append(float(self.voltage))
                    self.seriport.x.append(float(self.current))
                    self.seriport.x2[0], self.seriport.x2[1] = self.seriport.x[0], self.seriport.x[1]
                    self.seriport.y2[0], self.seriport.y2[1] = self.seriport.y[0], self.seriport.y[1]
                    self.graph1.emit(self.seriport.x2, self.seriport.y2)
                    del self.seriport.x[0]
                    del self.seriport.y[0]


                self.power = ""
                self.voltage = ""
                self.current = ""


                # CURRENT GRAPH PLOTTER
                if self.seriport.Command == 'B' and self.seriport.Mode == 'I' and self.seriport.Value != 0:
                    allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                    #print("sended packets:", allData)
                    self.seriport.write(allData.encode())
                    time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

                # POWER GRAPH PLOTTER
                if self.seriport.Command == 'B' and self.seriport.Mode == 'P' and self.seriport.Value != 0:
                    allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                    #print("sended packets:", allData)
                    self.seriport.write(allData.encode())
                    time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

                # VOLTAGE GRAPH PLOTTER
                if self.seriport.Command == 'B' and self.seriport.Mode == 'V' and self.seriport.Value != 0:
                    allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                    #print("sended packets:", allData)
                    self.seriport.write(allData.encode())
                    time.sleep(self.sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms

                if self.seriport.Command == 'B' and self.seriport.Mode == 'R' and self.seriport.Value != 0:
                    allData = self.seriport.Command + self.seriport.Mode + self.seriport.Value
                    #print("sended packets:", allData)
                    self.seriport.write(allData.encode())
                    time.sleep(self.sendTime)

                # C COMMAND GRAPH PLOTTER
                if self.seriport.Command == 'C':
                    #print("sended packets:", self.seriport.Command)
                    self.seriport.write("CCCCCCCCCCCCCC".encode())
                    time.sleep(self.C_sendTime)  # sine wave frequency is 50 Hz. So, that's bigger than 20 ms




