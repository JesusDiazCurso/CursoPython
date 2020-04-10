'''
Created on 31 mar. 2020

@author:Jesus
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas01 import ventana_principal, ventana_listado_juegos, ventana_registrar_juegos,\
    ventana_list_widget, ventana_table_widget
import sys
from modelo.clases import Juego
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidgetItem, QPushButton
from _functools import partial



lista_resultado = None

#inicio definicion funciones

def registrar_juego():
    juego = Juego
    juego.tipodejuego = ui_registrar_juego.entrada_tipo_juego.text()
    juego.nombrejuego = ui_registrar_juego.entrada_nombre_juego.text()
    juego.plataforma = ui_registrar_juego.entrada_tipo_plataforma.text()
    juego.añosalida = ui_registrar_juego.entrada_anio_juego.text()
    juego.precio = ui_registrar_juego.entrada_precio_juego.text()
    operaciones_bd.registro_juego(juego)
    QMessageBox.about(MainWindow,"Info","Registro juego OK")
    
def mostrar_registro_juegos():
    ui_registrar_juego.setupUi(MainWindow)
    ui_registrar_juego.boton_resgistrar_juego.clicked.connect(registrar_juego)
    
def mostrar_listado_juegos():
    ui_listar_juego.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_juegos()
    texto = ""
    for l in lista_resultado:
        texto += "id: " + str(l[0]) + " Tipo de Juego:  " + l[1] + " Nombre Juego: " + l[2] + " Plataforma: " + l[3] + " Año: " + str(l[4]) + " Precio: " + str(l[5]) + "\n"  
    ui_listar_juego.listado_juegos.setText(texto)
    
def mostrar_list_widget():
    ui_ventana_list_widget.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_juegos()
    for l in lista_resultado:
        ui_ventana_list_widget.list_widget_juegos.addItem(str(l[0]) + " Tipo de Juego: " + str(l[1]) + " Nombre Juego: " + str(l[2]) + " Plataforma: " + str(l[3]) + " Año: " + str(l[4]) + " Precio:" + str(l[5]))
    ui_ventana_list_widget.list_widget_juegos.itemClicked.connect(mostrar_registro)
    
def mostrar_registro():
    indice_seleccionado = ui_ventana_list_widget.list_widget_juegos.currentRow()
    texto = ""
    texto += " Tipo de Juego" + lista_resultado[indice_seleccionado][1] + "\n"
    texto += " Nombre Juego: " + lista_resultado[indice_seleccionado][2] + "\n"
    texto += " Plataforma: " + lista_resultado[indice_seleccionado][3] + "\n"
    texto += " Año: " + str(lista_resultado[indice_seleccionado][4]) + "\n"
    texto += " Precio: " + str(lista_resultado[indice_seleccionado][5])
    QMessageBox.about(MainWindow,"Info", texto)
    
def mostrar_table_widget():
    ui_ventana_table_widget.setupUi(MainWindow)
    juegos = operaciones_bd.obtener_juegos()
    fila = 0
    for l in juegos:
        ui_ventana_table_widget.tabla_juegos.insertRow(fila)
        #para añadir las celdas correspondientes
        columna_indice = 0
        for valor in l:
            celda = QTableWidgetItem(str(valor))
            ui_ventana_table_widget.tabla_juegos.setItem(fila,columna_indice,celda)
            columna_indice += 1
        #para meter boton de borrar
        boton_borrar = QPushButton("Borrar")
        boton_borrar.clicked.connect(partial(borrar_juego,l[0]))
        ui_ventana_table_widget.tabla_juegos.setCellWidget(fila,6,boton_borrar)
        fila += 1
def borrar_juego(id):
    res = QMessageBox.question(MainWindow,"Info","Vas a borrar un registro de ID: " +str(id))
    if res == QMessageBox.Yes:
        operaciones_bd.borrar_juego(id)
        mostrar_table_widget()
    
        
def mostrar_inicio():
    ui.setupUi(MainWindow)
    
    
#fin definicion funciones

#inicio aplicacion principal

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ventana_principal.Ui_MainWindow()

ui_registrar_juego = ventana_registrar_juegos.Ui_MainWindow()
ui_listar_juego = ventana_listado_juegos.Ui_MainWindow()
ui_ventana_list_widget = ventana_list_widget.Ui_MainWindow()
ui_ventana_table_widget = ventana_table_widget.Ui_MainWindow()

ui.setupUi(MainWindow)

ui.submenu_insertar_juego.triggered.connect(mostrar_registro_juegos)
ui.submenu_listar_juegos.triggered.connect(mostrar_listado_juegos)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
ui.submenu_list_widget_juegos.triggered.connect(mostrar_list_widget)
ui.submenu_table_widget_juegos.triggered.connect(mostrar_table_widget)



                      
MainWindow.show()
sys.exit(app.exec_())