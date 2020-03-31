# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.entrada_euros = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_euros.setGeometry(QtCore.QRect(400, 120, 131, 31))
        self.entrada_euros.setText("")
        self.entrada_euros.setObjectName("entrada_euros")
        self.label_introduce_euros = QtWidgets.QLabel(self.centralwidget)
        self.label_introduce_euros.setGeometry(QtCore.QRect(210, 100, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_introduce_euros.setFont(font)
        self.label_introduce_euros.setObjectName("label_introduce_euros")
        self.boton_convertir_a_dolares = QtWidgets.QPushButton(self.centralwidget)
        self.boton_convertir_a_dolares.setGeometry(QtCore.QRect(90, 190, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.boton_convertir_a_dolares.setFont(font)
        self.boton_convertir_a_dolares.setObjectName("boton_convertir_a_dolares")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(240, 280, 431, 121))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_resultado.setFont(font)
        self.label_resultado.setText("")
        self.label_resultado.setObjectName("label_resultado")
        self.boton_convertir_a_yenes = QtWidgets.QPushButton(self.centralwidget)
        self.boton_convertir_a_yenes.setGeometry(QtCore.QRect(270, 190, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.boton_convertir_a_yenes.setFont(font)
        self.boton_convertir_a_yenes.setObjectName("boton_convertir_a_yenes")
        self.boton_convertir_a_yuanes = QtWidgets.QPushButton(self.centralwidget)
        self.boton_convertir_a_yuanes.setGeometry(QtCore.QRect(450, 190, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.boton_convertir_a_yuanes.setFont(font)
        self.boton_convertir_a_yuanes.setObjectName("boton_convertir_a_yuanes")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_introduce_euros.setText(_translate("MainWindow", "Introduce cantidad de euros:"))
        self.boton_convertir_a_dolares.setText(_translate("MainWindow", "Convertir a Dolares"))
        self.boton_convertir_a_yenes.setText(_translate("MainWindow", "Convertir a Yenes"))
        self.boton_convertir_a_yuanes.setText(_translate("MainWindow", "Convertir a Yuanes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
