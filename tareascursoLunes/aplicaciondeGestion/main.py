'''
Created on 31 mar. 2020

@author: Jesus
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas01 import ventana_principal, ventana_listado_juegos , ventana_registrar_juegos
import sys

#inicio definicion funciones

def mostar_registro_juegos():
    ui_registrar_juego.setupUi(MainWindow)
    
def mostrar_listado_juegos():
    ui_listar_juego.setupUi(MainWindow)
    
def mostrar_inicio():
    ui.setupUi(MainWindow)
    ui.submenu_insertar_juego.triggered.connect(mostar_registro_juegos)
    ui.submenu_listar_juegos.triggered.connect(mostrar_listado_juegos)
    ui.submenu_inicio.triggered.connect(mostrar_inicio)
    
#fin definicion funciones

#inicio aplicacion principal

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ventana_principal.Ui_MainWindow()

ui_registrar_juego = ventana_registrar_juegos.Ui_MainWindow()
ui_listar_juego = ventana_listado_juegos.Ui_MainWindow()

ui.setupUi(MainWindow)

ui.submenu_insertar_juego.triggered.connect(mostar_registro_juegos)
ui.submenu_listar_juegos.triggered.connect(mostrar_listado_juegos)
ui.submenu_inicio.triggered.connect(mostrar_inicio)


                      
MainWindow.show()
sys.exit(app.exec_())