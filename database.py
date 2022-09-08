import psycopg2 as pg
import constantes as cs

def conectar():
    try:
        conexion = pg.connect(dbname=cs.BD, user=cs.USER, password=cs.PASSWORD, host=cs.HOST, port=cs.PORT)
        return conexion
    except pg.Error as e:
        print(f'Ocurrió un error al conectar a Postgresql: {e}')

