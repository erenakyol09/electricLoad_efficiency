import sys
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication, QDialog
import electronic_load_last_python
from serialThreadFile import serialThreadClass
import time
import numpy as np

BAUDRATES = [
    1200,
    #            "1800",
    #            "2400",
    #            "4800",
    9600,
    38400,
    19200,
    57600,
    115200,
]

# Find Live Ports
ports = list(serial.tools.list_ports.comports())

class MainClass(QDialog, electronic_load_last_python.Ui_ELECTRONICLOAD):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.startButton)
        self.pushButton_2.clicked.connect(self.stopButton)
        self.pushButton_3.clicked.connect(self.sendData)
        self.pushButton_4.clicked.connect(self.sendCommand)
        self.pushButton_5.clicked.connect(self.sendMode)
        self.pushButton_6.clicked.connect(self.sendElvalue)
        self.mySerial = serialThreadClass()
        self.mySerial.mesaj.connect(self.textBrowser.append)
        self.mySerial.mesaj1.connect(self.textBrowser_2.append)
        self.mySerial.mesaj2.connect(self.textBrowser_3.append)
        self.mySerial.mesaj3.connect(self.textBrowser_4.append)
        self.mySerial.mesaj4.connect(self.textBrowser_5.append)
        self.mySerial.mesaj5.connect(self.textBrowser_6.append)
        self.mySerial.mesaj6.connect(self.textBrowser_7.append)
        self.mySerial.mesaj7.connect(self.textBrowser_8.append)

        self.crc_str = "";
        self.crc = 0
        self.dizi = []
        self.str_length = ""

    def startButton(self):

        text = str(self.comboBox.currentText())
        print(" ")
        print(text)
        print(" ")
        text2 = int(self.comboBox_2.currentText())
        print(" ")
        print(text2)
        print(" ")
        print(ports)
        for p in ports:
            print(p.device)
            for i in BAUDRATES:
                if text == p.device and text2 == i:
                    self.mySerial.seriport.port = text
                    self.mySerial.seriport.baudrate = text2
                    self.mySerial.seriport.open()
                    self.mySerial.start()
                    print("device connected")
                    self.mySerial.seriport.a = 1
                    break
                else:
                    print("device unconnected")
                    self.mySerial.seriport.close()
            break


    def stopButton(self):

        self.mySerial.seriport.a = 0
        print("device unconnected")

    def sendData(self):

        Tx_data = self.lineEdit.text()
        print(Tx_data.encode())
        time.sleep(1 / 100)

        if self.mySerial.seriport.a == 1:
            self.mySerial.seriport.write(Tx_data.encode())
            print("sended")


    def sendCommand(self):
        if self.mySerial.seriport.a == 1:

            text3 = str(self.comboBox_3.currentText())

            if text3 == 'A':
                self.mySerial.seriport.write(text3.encode())
            elif text3 == 'B':
                self.mySerial.seriport.write(text3.encode())
            else:
                self.mySerial.seriport.write(text3.encode())



    def sendMode(self):
        if self.mySerial.seriport.a == 1:
            text4 = str(self.comboBox_4.currentText())

            if text4 == "Constant Current":
                self.mySerial.seriport.write('I'.encode())
            elif text4 == "Constant Voltage":
                self.mySerial.seriport.write('V'.encode())
            elif text4 == "Constant Power":
                self.mySerial.seriport.write('P'.encode())
            else:
                self.mySerial.seriport.write('R'.encode())




    def sendElvalue(self):

        text5 = self.lineEdit_2.text()
        print(text5)
        print(type(text5))
        #for ele in text5:
        #    self.dizi.extend(hex(ord(num)) for num in ele)
        self.dizi = text5.encode()
        length = len(text5)

        if length < 10:
            self.str_length = '0' + str(length)
        if length >= 10:
            self.str_length = str(length)

        for i in range(length):
            self.crc = self.crc + self.dizi[i]

        crc_str = hex(self.crc)
        print(crc_str)
        crc_lentgh = len(crc_str)
        print(crc_lentgh)

        if crc_str[crc_lentgh - 3] == 'x':
            self.dizi = self.str_length + self.dizi.decode() + '0' + '0'
            self.dizi = self.dizi + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]

        if crc_str[crc_lentgh - 4] == 'x':
            self.dizi = self.str_length + self.dizi.decode() + '0' + crc_str[crc_lentgh - 3]
            self.dizi = self.dizi + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]

        if crc_str[crc_lentgh - 5] == 'x':
            self.dizi = self.str_length + self.dizi.decode() + crc_str[crc_lentgh - 4] + crc_str[crc_lentgh - 3]
            self.dizi = self.dizi + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]

        print(self.dizi)

        if self.mySerial.seriport.a == 1:
            for i in range(int(length + 2 + 4)):  # + 2 length - +2 crc low 2 byte
                self.mySerial.seriport.write(self.dizi[i].encode())
                time.sleep(1 / 1000)

        self.crc_str = "";
        self.crc = 0;
        self.dizi = "";




if __name__ == '__main__':
    uygulama = QApplication(sys.argv)
    pencere = MainClass()
    pencere.show()
    uygulama.exec_()
