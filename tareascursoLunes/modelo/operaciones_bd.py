import mysql.connector
from modelo import constantes_sql

def conectar():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "bd_videojuegos"
        
        
        )
    return conexion

def registro_juego(juego):
    sql = constantes_sql.SQL_INSERCION_JUEGO
    conexion = conectar()
    cursor = conexion.cursor()
    valores_a_insertar = (juego.tipodejuego , juego.nombrejuego , juego.plataforma , juego.añosalida , juego.precio)
    cursor.execute(sql , valores_a_insertar)
    conexion.commit()
    conexion.disconnect()
    
def obtener_juegos():
    sql = constantes_sql.SQL_SELECT_JUEGOS
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(sql)
    lista_resultado = cursor.fetchall()
    conexion.disconnect
    return lista_resultado
    
def borrar_juego(id_juego):
    sql = constantes_sql.SQL_BORRAR_JUEGO
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id_juego,)
    cursor.execute(sql,val)
    conexion.commit()
    conexion.disconnect()
    
    
    
    