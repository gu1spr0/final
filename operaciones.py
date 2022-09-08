from unittest import result
import psycopg2 as pg
import database as db
import constantes as c
from datetime import datetime

def insertar_estudiante(estudiante):
    conexion = db.conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO estudiantes (nombres, paterno, materno, edad, estatura, estado) VALUES (%s, %s, %s, %s, %s, %s);"
            resultado = cursor.execute(consulta, estudiante)
        conexion.commit()
        return resultado.fetchone()[0]
    except pg.Error as e:
        print(f'Ocurrió un error al insertar estudiante: {e}')
    finally:
        conexion.close()
def insertar_materia(materia):
    conexion = db.conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO materias (nombre, sigla, carga, estado) VALUES (%s, %s, %s, %s) RETURNING id_materia;"
            cursor.execute(consulta, materia)
            id = cursor.fetchone()[0]
        conexion.commit()
        return id
    except pg.Error as e:
        print(f'Ocurrió un error al insertar materia: {e}')
    finally:
        conexion.close()
def inscribir_estudiante(id_estudiante, id_materia):
    conexion = db.conectar()
    try:
        now = datetime.now()
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO estudiantes_materias (id_estudiante, id_materia, fecha) VALUES (%s, %s, %s);"
            resultado = cursor.execute(consulta, (str(id_estudiante), str(id_materia), now))
        conexion.commit()
        return resultado.fetchone()[0]
    except pg.Error as e:
        print(f'Ocurrió un error al insertar materia: {e}')
    finally:
        conexion.close()
def inscritos_por_materia(id_materia):
    listado = {}
    estudiantes = []
    conexion = db.conectar()
    try:
        codigo_materia, nombre, sigla, carga, estado = buscar_materia(id_materia)
        listado["codigo"] = codigo_materia
        listado["materia"] = nombre
        listado["sigla"] = sigla
        listado["carga"] = carga
        listado["estado"] = estado

        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM estudiantes_materias WHERE id_materia = %s;"
            cursor.execute(consulta, (id_materia,))
            inscritos = cursor.fetchall()

            for codigo_ins,id_estudiante,id_materia,fecha in inscritos:
                estudiante = buscar_estudiante(id_estudiante)
                if(estudiante != None):
                    estudiantes.append(estudiante)
            listado["estudiantes"] = estudiantes
        return listado
    except pg.Error as e:
        print(f'Ocurrió un error al insertar estudiante: {e}')
    finally:
        conexion.close()
def inscritos_por_estudiante(id_estudiante):
    listado = {}
    materias = []
    conexion = db.conectar()
    try:
        codigo_estudiante, nombres, paterno, materno, edad, estatura, estado = buscar_estudiante(id_estudiante)
        listado["codigo"] = codigo_estudiante
        listado["nombre"] = f'{nombres} {paterno} {materno}'
        listado["edad"] = edad
        listado["estatura"] = estatura
        listado["estado"] = estado

        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM estudiantes_materias WHERE id_estudiante = %s;"
            cursor.execute(consulta, (id_estudiante,))
            inscritos = cursor.fetchall()

            for codigo_ins,id_estudiante,id_materia,fecha in inscritos:
                materia = buscar_materia(id_materia)
                if(materia != None):
                    materias.append(materia)
            listado["materias"] = materias
        return listado
    except pg.Error as e:
        print(f'Ocurrió un error al insertar estudiante: {e}')
    finally:
        conexion.close()
def listar_estudiantes(estado='AC'):
    conexion = db.conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM estudiantes WHERE estado = %s;"
            cursor.execute(consulta, (estado,))
            estudiantes = cursor.fetchall()
            return estudiantes;
    except pg.Error as e:
        print(f'Ocurrió un error al insertar estudiante: {e}')
    finally:
        conexion.close()
def listar_materias(estado='AC'):
    conexion = db.conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM materias WHERE estado = %s;"
            cursor.execute(consulta, (estado,))
            materias = cursor.fetchall()
            return materias;
    except pg.Error as e:
        print(f'Ocurrió un error al insertar estudiante: {e}')
    finally:
        conexion.close()
def listar_inscripciones():
    conexion = db.conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM estudiantes_materias;"
            cursor.execute(consulta)
            inscripciones = cursor.fetchall()
            return inscripciones;
    except pg.Error as e:
        print(f'Ocurrió un error al insertar estudiante: {e}')
    finally:
        conexion.close()
def buscar_estudiante(id_estudiante):
    conexion = db.conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM estudiantes WHERE id_estudiante = %s;"
            cursor.execute(consulta, (id_estudiante,))
            estudiante = cursor.fetchone()
            return estudiante;
    except pg.Error as e:
        print(f'Ocurrió un error al buscar estudiante: {e}')
    finally:
        conexion.close()
def buscar_materia(id_materia):
    conexion = db.conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM materias WHERE id_materia = %s;"
            cursor.execute(consulta, (id_materia,))
            materia = cursor.fetchone()
            return materia;
    except pg.Error as e:
        print(f'Ocurrió un error al buscar materia: {e}')
    finally:
        conexion.close()