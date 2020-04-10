# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_table_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(908, 560)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabla_juegos = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_juegos.setGeometry(QtCore.QRect(10, 70, 891, 491))
        self.tabla_juegos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabla_juegos.setObjectName("tabla_juegos")
        self.tabla_juegos.setColumnCount(7)
        self.tabla_juegos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setKerning(True)
        item.setFont(font)
        self.tabla_juegos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        item.setFont(font)
        self.tabla_juegos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_juegos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_juegos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_juegos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_juegos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_juegos.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 30, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tabla_juegos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tabla_juegos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TIPO  JUEGO"))
        item = self.tabla_juegos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "       NOMBRE JUEGO      "))
        item = self.tabla_juegos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PLATAFORMA"))
        item = self.tabla_juegos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "AÑO"))
        item = self.tabla_juegos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "PRECIO"))
        item = self.tabla_juegos.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "BORRAR"))
        self.label.setText(_translate("MainWindow", "LISTADO JUEGOS TABLET WIDGET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
