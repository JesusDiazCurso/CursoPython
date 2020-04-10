SQL_INSERCION_JUEGO = "INSERT INTO `tabla_juegos` (`id`, `Tipo de Juego`, `Nombre de juego`, `Plataforma`, `Año de Salida`, `Precio`) VALUES (NULL, %s, %s, %s, %s, %s);"
SQL_SELECT_JUEGOS = "SELECT * FROM tabla_juegos" 
SQL_BORRAR_JUEGO = "DELETE FROM tabla_juegos WHERE id = %s ;"