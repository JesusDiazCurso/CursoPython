# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_registrar_juegos.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 15pt \"MV Boli\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 100, 111, 16))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 11pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.entrada_nombre_juego = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_nombre_juego.setGeometry(QtCore.QRect(290, 100, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entrada_nombre_juego.setFont(font)
        self.entrada_nombre_juego.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entrada_nombre_juego.setObjectName("entrada_nombre_juego")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 210, 47, 13))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 11pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.entrada_precio_juego = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_precio_juego.setGeometry(QtCore.QRect(290, 210, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entrada_precio_juego.setFont(font)
        self.entrada_precio_juego.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entrada_precio_juego.setText("")
        self.entrada_precio_juego.setObjectName("entrada_precio_juego")
        self.boton_resgistrar_juego = QtWidgets.QPushButton(self.centralwidget)
        self.boton_resgistrar_juego.setGeometry(QtCore.QRect(260, 440, 151, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.boton_resgistrar_juego.setFont(font)
        self.boton_resgistrar_juego.setStyleSheet("font: 10pt \"MV Boli\";")
        self.boton_resgistrar_juego.setObjectName("boton_resgistrar_juego")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 140, 91, 16))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 11pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.entrada_tipo_plataforma = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_tipo_plataforma.setGeometry(QtCore.QRect(290, 140, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entrada_tipo_plataforma.setFont(font)
        self.entrada_tipo_plataforma.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entrada_tipo_plataforma.setText("")
        self.entrada_tipo_plataforma.setObjectName("entrada_tipo_plataforma")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 70, 111, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 11pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.entrada_tipo_juego = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_tipo_juego.setGeometry(QtCore.QRect(290, 70, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entrada_tipo_juego.setFont(font)
        self.entrada_tipo_juego.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entrada_tipo_juego.setText("")
        self.entrada_tipo_juego.setObjectName("entrada_tipo_juego")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 170, 51, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 11pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.entrada_anio_juego = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_anio_juego.setGeometry(QtCore.QRect(290, 170, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entrada_anio_juego.setFont(font)
        self.entrada_anio_juego.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entrada_anio_juego.setText("")
        self.entrada_anio_juego.setObjectName("entrada_anio_juego")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(290, 260, 131, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 11pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")
        self.checkbox_digital = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_digital.setGeometry(QtCore.QRect(270, 260, 21, 17))
        self.checkbox_digital.setText("")
        self.checkbox_digital.setChecked(True)
        self.checkbox_digital.setObjectName("checkbox_digital")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 320, 61, 16))
        self.label_3.setStyleSheet("font: 11pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.combo_edicion = QtWidgets.QComboBox(self.centralwidget)
        self.combo_edicion.setGeometry(QtCore.QRect(310, 320, 69, 22))
        self.combo_edicion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.combo_edicion.setObjectName("combo_edicion")
        self.combo_edicion.addItem("")
        self.combo_edicion.addItem("")
        self.combo_edicion.addItem("")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(220, 360, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font: 11pt \"MV Boli\";")
        self.label_11.setObjectName("label_11")
        self.radio_tarjeta_credito = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_tarjeta_credito.setGeometry(QtCore.QRect(350, 360, 111, 17))
        self.radio_tarjeta_credito.setStyleSheet("font: 10pt \"MV Boli\";")
        self.radio_tarjeta_credito.setObjectName("radio_tarjeta_credito")
        self.radio_paypal = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_paypal.setGeometry(QtCore.QRect(350, 380, 82, 17))
        self.radio_paypal.setStyleSheet("font: 10pt \"MV Boli\";")
        self.radio_paypal.setObjectName("radio_paypal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Introduce datos del Juego:"))
        self.label_2.setText(_translate("MainWindow", "Nombre Juego:"))
        self.label_5.setText(_translate("MainWindow", "Precio:"))
        self.boton_resgistrar_juego.setText(_translate("MainWindow", "REGISTRAR JUEGOS"))
        self.label_6.setText(_translate("MainWindow", "Plataforma:"))
        self.label_7.setText(_translate("MainWindow", "Tipo de Juego:"))
        self.label_8.setText(_translate("MainWindow", "Año:"))
        self.label_9.setText(_translate("MainWindow", "Digital Disponible"))
        self.label_3.setText(_translate("MainWindow", "Edicion:"))
        self.combo_edicion.setItemText(0, _translate("MainWindow", "Standar"))
        self.combo_edicion.setItemText(1, _translate("MainWindow", "Gold"))
        self.combo_edicion.setItemText(2, _translate("MainWindow", "De Luxe"))
        self.label_11.setText(_translate("MainWindow", "Opción de pago:"))
        self.radio_tarjeta_credito.setText(_translate("MainWindow", "Tarjeta Credito"))
        self.radio_paypal.setText(_translate("MainWindow", "Paypal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
