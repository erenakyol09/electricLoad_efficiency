import sys
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication, QDialog
import electronic_load_last_python

from serialThreadFile import serialThreadClass



ports = serial.tools.list_ports.comports()

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


class MainClass(QDialog, electronic_load_last_python.Ui_ELECTRONICLOAD):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.startButton)
        self.pushButton_2.clicked.connect(self.stopButton)
        self.pushButton_3.clicked.connect(self.sendData)
        self.mySerial = serialThreadClass()
        self.mySerial.mesaj.connect(self.textBrowser.append)
        self.mySerial.mesaj1.connect(self.textBrowser_2.append)
        self.mySerial.mesaj2.connect(self.textBrowser_3.append)
        self.mySerial.mesaj3.connect(self.textBrowser_4.append)
        self.mySerial.mesaj4.connect(self.textBrowser_5.append)
        self.mySerial.mesaj5.connect(self.textBrowser_6.append)
        self.mySerial.mesaj6.connect(self.textBrowser_7.append)
        self.mySerial.mesaj7.connect(self.textBrowser_8.append)


    def startButton(self):

        text = str(self.comboBox.currentText())
        print(" ")
        print(text)
        print(" ")
        text2 = int(self.comboBox_2.currentText())
        print(" ")
        print(text2)
        print(" ")
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
                else:
                    self.mySerial.seriport.close()
                    print("device unconnected")


    def stopButton(self):
        self.mySerial.seriport.a = 0
        #print("device unconnected")

    def sendData(self):
        if self.mySerial.seriport.a == 1:
            Tx_data = self.lineEdit.text()
            self.mySerial.seriport.write(Tx_data.encode())
            print("sended")
        else:
            self.mySerial.seriport.close()



if __name__ == '__main__':
    uygulama = QApplication(sys.argv)
    pencere = MainClass()
    pencere.show()
    uygulama.exec_()
