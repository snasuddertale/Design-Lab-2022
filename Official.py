import ctypes
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import serial


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def main():
    if is_admin():

        s = serial.Serial(port="COM6", baudrate=115200)

    else:

        s = serial.Serial(port="COM6", baudrate=115200)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


    s.write(b"1\n")
    while True:
        text = s.readline()
        if b'MicroPython' not in text:
            print(text.decode())
            with open("terminal_data.csv", "a") as terminal:
                terminal.write(str(text.decode()))
                terminal.close()
        s.write(b"next\n")
        if b'MicroPython' in text:
            break
    return s


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Design Laboratory"
        self.left = 500  # odległośc od lewej krawędzi ekranu w pixelach
        self.top = 150  # odległośc od górnej krawędzi ekranu w pixelach
        self.width = 300  # szerokośc okna
        self.height = 400  # wysokość okna

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: white;")

        self.b11 = QtWidgets.QLabel("DESIGN LABORATORY", self)
        self.b11.move(100, 45)
        self.b11.resize(150, 40)
        self.b11.setStyleSheet("color: black;")

        self.b2 = QtWidgets.QLabel("Aplikacja", self)
        self.b2.move(130, 70)
        self.b2.resize(150, 30)
        self.b2.setStyleSheet("color: black;")


        self.Open = QtWidgets.QPushButton("Wybierz Plik", self)
        self.Open.move(55, 200)
        self.Open.resize(200, 60)
        self.Open.setStyleSheet("border: 3px solid black;")
        self.Open.clicked.connect(self.OpenFile)


        self.wykres1 = QtWidgets.QPushButton("Narysuj Wykresy", self)
        self.wykres1.move(55, 270)
        self.wykres1.resize(200, 60)
        self.wykres1.setStyleSheet("border: 3px solid black;")
        self.wykres1.clicked.connect(self.plot)

        self.wyg = QtWidgets.QLabel("######################################", self)
        self.wyg.move(0, 360)
        self.wyg.resize(300, 20)
        self.wyg.setStyleSheet("color: black;")

        self.wyg1 = QtWidgets.QLabel("######################################", self)
        self.wyg1.move(0, 20)
        self.wyg1.resize(300, 20)
        self.wyg1.setStyleSheet("color: black;")

        self.file_path = None

    def OpenFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                             "CSV Files (*.csv);;All Files (*)", options=options)
        if file_name:
            self.file_path = file_name
            print("File selected:", self.file_path)
            self.basename = os.path.basename(file_name)
            return self.basename

    def plot(self):
        COOy = []
        COy = []
        CH4y = []
        CO2y = []
        Ty = []
        Hy = []

        with open(f'{self.basename}', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=';')
            for row in plots:
                if row:  # check if the row is not empty

                    if row[0]:  # check if the value of the first column is not empty
                        CH4y.append(float(row[0]))
                    else:
                        CH4y.append(float('nan'))  # if the value is empty, append NaN
                    if row[1]:  # check if the value of the second column is not empty
                        COy.append(float(row[1]))
                    else:
                        COy.append(float('nan'))  # if the value is empty, append NaN
                    if row[2]:  # check if the value of the third column is not empty
                        COOy.append(float(row[2]))
                    else:
                        COOy.append(float('nan'))  # if the value is empty, append NaN
                    if row[3]:  # check if the value of the fourth column is not empty
                        CO2y.append(float(row[3]))
                    else:
                        CO2y.append(float('nan'))  # if the value is empty, append NaN
                    if row[4]:  # check if the value of the fifth column is not empty
                        Ty.append(float(row[4]))
                    else:
                        Ty.append(float('nan'))  # if the value is empty, append NaN
                    try:
                        Hy.append(float(row[5]))
                    except ValueError:
                        Hy.append(float('nan'))  # if the value is empty, append NaN

            # Create the x axis with range of 0 to the number of rows in the CSV file
            x = list(range(0,len(CH4y),5))

        fig, axs = plt.subplots(3, 2)
        axs[0, 0].plot(x, CH4y)
        axs[0, 0].set_title("CH4")
        axs[1, 0].plot(x, COy)
        axs[1, 0].set_title("CO")
        axs[0, 1].plot(x, COOy)
        axs[0, 1].set_title("COO")
        axs[1, 1].plot(x, CO2y)
        axs[1, 1].set_title("CO2")
        axs[2, 0].plot(x, Ty)
        axs[2, 0].set_title("Temperature")
        axs[2, 1].plot(x, Hy)
        axs[2, 1].set_title("Humidity")
        axs[2, 1].set_yticks(np.arange(40, max(Hy), 1))
        fig.tight_layout()

        for ax in axs.flat:
            ax.set(xlabel='Index', ylabel='Value')

        plt.show()


ser = main()
if ser is not None:
    print("Urzadzenie znalezione")
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
else:
    print("Urzadzenie nie znalezione")