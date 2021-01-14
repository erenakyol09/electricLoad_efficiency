import sys
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication, QDialog
import electronic_load_last_python
from serialThreadFile import serialThreadClass
import time
import pyqtgraph as pg
import pyqtgraph.exporters
import csv

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
        self.pushButton_7.clicked.connect(self.graph_select)
        self.pushButton_8.clicked.connect(self.oneGraph_save)
        self.pushButton_10.clicked.connect(self.draw_graphics)
        self.pushButton_11.clicked.connect(self.sendC_stop)
        self.pushButton_12.clicked.connect(self.refresh_history)
        self.pushButton_20.clicked.connect(self.twoGraph_draw)
        self.mySerial = serialThreadClass()


        self.mySerial.mesaj1.connect(self.textBrowser_10.append) # el - power
        self.mySerial.mesaj2.connect(self.textBrowser_11.append) # el - voltage
        self.mySerial.mesaj3.connect(self.textBrowser_12.append) # el - current


        self.mySerial.mesaj5.connect(self.textBrowser_3.append)
        self.mySerial.mesaj6.connect(self.textBrowser_4.append)
        self.mySerial.mesaj7.connect(self.textBrowser_5.append)
        self.mySerial.mesaj8.connect(self.textBrowser_6.append)
        self.mySerial.mesaj9.connect(self.textBrowser_7.append)
        self.mySerial.mesaj10.connect(self.textBrowser_8.append)
        self.mySerial.mesaj11.connect(self.textBrowser_9.append)

        self.mySerial.mesaj.connect(self.textBrowser.append)
        self.mySerial.mesaj12.connect(self.textBrowser_2.append)

        self.mySerial.lcd.connect(self.lcdNumber.display)


        self.mySerial.label.connect(self.label_10.setText)

        self.crc_str = ""
        self.crc = 0
        self.dizi = []
        self.str_length = ""

        styles = {'color': 'r', 'font-size': '20px'}

        self.graphicsView.setBackground('w')
        self.graphicsView.setXRange(min=0, max=1000, padding=0)
        self.graphicsView.setYRange(min=0, max=1000, padding=0)

        self.graphicsView_2.setBackground('w')
        self.graphicsView_2.setXRange(min=0, max=1000, padding=0)
        self.graphicsView_2.setYRange(min=0, max=1000, padding=0)


        self.twoGraphrow = [0,0,0]


    def draw_graphics(self):

        if self.mySerial.seriport.a == 1:
            self.mySerial.seriport.run_data = 1
            self.graphicsView.plotItem.clear()
            self.graphicsView_2.plotItem.clear()



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

        self.label_10.setText("DEVICE NOT CONNECT")
        self.mySerial.seriport.a = 0
        print("device unconnected")

    def sendData(self):

        Tx_data = self.lineEdit.text()
        print(Tx_data.encode())
        time.sleep(1 / 100)

        if self.mySerial.seriport.a == 1:
            self.mySerial.seriport.write(Tx_data.encode())
            print("sended")

    def graph_select(self):

        self.mySerial.seriport.txt_graph = str(self.comboBox_5.currentText())
        styles = {'color': 'r', 'font-size': '20px'}

        if self.mySerial.seriport.txt_graph == "I-V":
            self.graphicsView.setLabel('left', 'Current (A)', **styles)
            self.graphicsView.setLabel('bottom', 'Voltage (V)', **styles)
            self.graphicsView.setTitle("Current-Voltage Graph", color="r", size="15pt")

        if self.mySerial.seriport.txt_graph == "P-V":
            self.graphicsView.setLabel('left', 'Power (W)', **styles)
            self.graphicsView.setLabel('bottom', 'Voltage (V)', **styles)
            self.graphicsView.setTitle("Power-Voltage Graph", color="r", size="15pt")

        if self.mySerial.seriport.txt_graph == "η-P":
            self.graphicsView.setLabel('left', 'Efficiency (η)', **styles)
            self.graphicsView.setLabel('bottom', 'Power (W)', **styles)
            self.graphicsView.setTitle("Efficiency-Power Graph", color="r", size="15pt")

        if self.mySerial.seriport.txt_graph == "V-I":
            self.graphicsView.setLabel('left', 'Voltage (V)', **styles)
            self.graphicsView.setLabel('bottom', 'Current (A)', **styles)
            self.graphicsView.setTitle("Voltage-Current Graph", color="r", size="15pt")

        if self.mySerial.seriport.txt_graph == "cosφ-P":
            self.graphicsView.setLabel('left', 'cosφ', **styles)
            self.graphicsView.setLabel('bottom', 'Power (W)', **styles)
            self.graphicsView.setTitle("cosφ-Power Graph", color="r", size="15pt")

        self.graphicsView.setBackground('w')
        self.graphicsView.setXRange(min=0, max=1000, padding=0)
        self.graphicsView.setYRange(min=0, max=1000, padding=0)
        self.mySerial.graph1.connect(self.graphicsView.plotItem.plot)

    def oneGraph_save(self):

        graphName = self.lineEdit_3.text()
        graphName = graphName + ".csv"
        exporter = pg.exporters.CSVExporter(self.graphicsView.plotItem)
        exporter.export(graphName)

    def twoGraph_draw(self):

        name1 = self.lineEdit_6.text()
        name2 = self.lineEdit_7.text()
        name1 = name1 + ".csv"
        name2 = name2 + ".csv"

        print(name1)
        print(name2)

        self.plot(name1,(255,0,0))
        self.plot(name2,(100, 0, 0))

        styles = {'color': 'r', 'font-size': '20px'}

        if self.mySerial.seriport.txt_graph == "I-V":
            self.graphicsView_2.setLabel('left', 'Current (A)', **styles)
            self.graphicsView_2.setLabel('bottom', 'Voltage (V)', **styles)
            self.graphicsView_2.setTitle("Current-Voltage Graph", color="r", size="15pt")

        if self.mySerial.seriport.txt_graph == "P-V":
            self.graphicsView_2.setLabel('left', 'Power (W)', **styles)
            self.graphicsView_2.setLabel('bottom', 'Voltage (V)', **styles)
            self.graphicsView_2.setTitle("Power-Voltage Graph", color="r", size="15pt")

        if self.mySerial.seriport.txt_graph == "η-P":
            self.graphicsView_2.setLabel('left', 'Efficiency (η)', **styles)
            self.graphicsView_2.setLabel('bottom', 'Power (W)', **styles)
            self.graphicsView_2.setTitle("Efficiency-Power Graph", color="r", size="15pt")

        if self.mySerial.seriport.txt_graph == "V-I":
            self.graphicsView_2.setLabel('left', 'Voltage (V)', **styles)
            self.graphicsView_2.setLabel('bottom', 'Current (A)', **styles)
            self.graphicsView_2.setTitle("Voltage-Current Graph", color="r", size="15pt")

        if self.mySerial.seriport.txt_graph == "cosφ-P":
            self.graphicsView_2.setLabel('left', 'cosφ', **styles)
            self.graphicsView_2.setLabel('bottom', 'Power (W)', **styles)
            self.graphicsView_2.setTitle("cosφ-Power Graph", color="r", size="15pt")

        self.graphicsView_2.setBackground('w')
        self.graphicsView_2.setXRange(min=0, max=1000, padding=0)
        self.graphicsView_2.setYRange(min=0, max=1000, padding=0)

    def plot(self, name, color):

        with open(name, 'r') as file:
            reader = csv.reader(file)
            index = 0
            for row in reader:
                self.twoGraphrow[index] = row
                index += 1

            print(self.twoGraphrow[0])
            print(self.twoGraphrow[1])
            print(self.twoGraphrow[2])

            length = len(self.twoGraphrow[1])

            del self.twoGraphrow[1][length - 1]
            del self.twoGraphrow[2][length - 1]

            plotX1 = []
            plotY1 = []

            for item in self.twoGraphrow[1]:
                plotX1.append(float(item))
            for item in self.twoGraphrow[2]:
                plotY1.append(float(item))
            for i in range(2):
                print(i)
                del plotX1[0]
                del plotY1[-1]

            print(plotX1)
            print(plotY1)

            pen = pg.mkPen(color=color, width=10)
            self.graphicsView_2.plot(plotX1,plotY1, pen=pen)

    def sendCommand(self):

        if self.mySerial.seriport.a == 1:

            text3 = str(self.comboBox_3.currentText())

            if text3 == 'A':
                self.mySerial.seriport.Command = 'A'
                self.mySerial.seriport.write("AAAAAAAAAAAAAA".encode())
                time.sleep(5 / 1000)
            elif text3 == 'B':
                self.mySerial.seriport.Command = 'B'
            else:
                self.mySerial.seriport.Command = 'C'

    def sendMode(self):

        if self.mySerial.seriport.a == 1:
            text4 = str(self.comboBox_4.currentText())

            if text4 == "Constant Current":
                self.mySerial.seriport.Mode = 'I'
            elif text4 == "Constant Voltage":
                self.mySerial.seriport.Mode = 'V'
            elif text4 == "Constant Power":
                self.mySerial.seriport.Mode = 'P'
            else:
                self.mySerial.seriport.Mode = 'R'

    def sendC_stop(self):

        self.mySerial.seriport.Mode     = 0
        self.mySerial.seriport.Command  = 0
        self.mySerial.seriport.Value    = 0
        self.mySerial.seriport.run_data = 0

        self.mySerial.seriport.write("!!!!!!!!!!!!!!".encode())
        print("STOP PUSHED")

    def sendElvalue(self):

        text5 = self.lineEdit_2.text()

        if len(text5) == 6:
            self.dizi = text5.encode()
            length = len(text5)

            if length < 10:
                self.str_length = '0' + str(length)
            if length >= 10:
                self.str_length = str(length)

            for i in range(length):
                self.crc = self.crc + self.dizi[i]

            crc_str = hex(self.crc)
            crc_lentgh = len(crc_str)

            if crc_str[crc_lentgh - 3] == 'x':
                self.dizi = self.str_length + self.dizi.decode() + '0' + '0'
                self.dizi = self.dizi + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]

            if crc_str[crc_lentgh - 4] == 'x':
                self.dizi = self.str_length + self.dizi.decode() + '0' + crc_str[crc_lentgh - 3]
                self.dizi = self.dizi + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]

            if crc_str[crc_lentgh - 5] == 'x':
                self.dizi = self.str_length + self.dizi.decode() + crc_str[crc_lentgh - 4] + crc_str[crc_lentgh - 3]
                self.dizi = self.dizi + crc_str[crc_lentgh - 2] + crc_str[crc_lentgh - 1]

            self.mySerial.seriport.Value = self.dizi

        self.crc_str = ""
        self.crc = 0
        self.dizi = ""

    def refresh_history(self):

        self.mySerial.seriport.run_data = 0

        self.graphicsView.plotItem.clear()
        self.graphicsView_2.plotItem.clear()

        self.lineEdit_2.clear()

        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.textBrowser_3.clear()
        self.textBrowser_4.clear()
        self.textBrowser_5.clear()
        self.textBrowser_6.clear()
        self.textBrowser_7.clear()
        self.textBrowser_8.clear()
        self.textBrowser_9.clear()
        self.textBrowser_10.clear()
        self.textBrowser_11.clear()
        self.textBrowser_12.clear()

        self.mySerial.seriport.x = [0]
        self.mySerial.seriport.y = [0]

        self.mySerial.seriport.y2 = [0]
        self.mySerial.seriport.y3 = [0]
        self.mySerial.seriport.y4 = [0]
        self.mySerial.seriport.y5 = [0]




if __name__ == '__main__':
    uygulama = QApplication(sys.argv)
    pencere = MainClass()
    pencere.show()
    uygulama.exec_()