#ejercicio basico conversor de monedas

from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal
import sys

def convertir_de_euros_a_dolares():
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    dolares = introducido_float * 0.91
    ui.label_resultado.setText("En dolares: " + "{:.2f}".format(dolares).replace(".",",") )
    
def convertir_de_euros_a_yenes():
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)    
    yenes = introducido_float * 119.06
    ui.label_resultado.setText("En Yenes: " + "{:.2f}".format(yenes).replace(".",",") )
    
def convertir_de_euros_a_yuanes():
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)    
    yuanes = introducido_float * 7.79
    ui.label_resultado.setText("En Yuanes: " + "{:.2f}".format(yuanes).replace(".",",") )
    
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_principal.Ui_MainWindow()
ui.setupUi(MainWindow)

ui.boton_convertir_a_dolares.setIcon(QtGui.QIcon("dolar.png"))
ui.boton_convertir_a_yenes.setIcon(QtGui.QIcon("japon.png"))
ui.boton_convertir_a_yuanes.setIcon(QtGui.QIcon("china.png"))

ui.boton_convertir_a_dolares.clicked.connect(convertir_de_euros_a_dolares)
ui.boton_convertir_a_yenes.clicked.connect(convertir_de_euros_a_yenes)
ui.boton_convertir_a_yuanes.clicked.connect(convertir_de_euros_a_yuanes)
MainWindow.show()
sys.exit(app.exec_())
