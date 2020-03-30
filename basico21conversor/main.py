from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal
import sys

#tareas sobre el conversor:
# 1- Crear una nueva aplicacion que permita la conversion de euros a un tipo de moneda
#    a elegir por el programador
# 2- Sobre dicha aplicacion, agregar dos botones mas para poder transformar a otros dos 
#    tipos de moneda
# 3- Buscar en internet una solucion para poder 
#    agregar un icono a cada boton representando el tipo de moneda

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
