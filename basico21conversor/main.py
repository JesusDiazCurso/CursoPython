from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal
import sys


def convertir_de_pesos_a_euros():
    print("boton pulsado")
    introducido = ui.entrada_pesos.text().replace(",",".")
    introducido_float = float(introducido)
    euros = introducido_float * 0.014
    ui.label_resultado.setText("En euros: " + "{:.2f}".format(euros).replace(".",",") )

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_principal.Ui_MainWindow()
ui.setupUi(MainWindow)

#antes de mostrar ventana principal asigno el codigo a ejectar cuando 
#se haga click en el boton
ui.boton_convertir_a_euros.clicked.connect(convertir_de_pesos_a_euros)

MainWindow.show()
sys.exit(app.exec_())
