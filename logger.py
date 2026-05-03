"""
logger.py
=========
Modulo para configurar el sistema de logs del proyecto.
Uso la libreria logging que ya viene incluida en python.
Todo se guarda en logs.txt y tambien se muestra por consola.

Autor: Sergio Esteban Duque Daza
CC: 1121930202
Correo: seduqued@unadvirtual.edu.co
Curso: Programacion Orientada a Objetos - Fase 4
Universidad Nacional Abierta y a Distancia (UNAD)
"""

import logging
import os

# saco la ruta de la carpeta donde esta este archivo
# y armo la ruta completa al archivo logs.txt
CARPETA = os.path.dirname(os.path.abspath(__file__))
RUTA_LOG = os.path.join(CARPETA, "logs.txt")


def obtener_logger(nombre="SoftwareFJ"):
    # creo (o saco si ya existe) el logger con ese nombre
    logger = logging.getLogger(nombre)
    logger.setLevel(logging.DEBUG)

    # si ya tiene handlers no los vuelvo a agregar
    # porque si no se duplicarian los mensajes en cada llamada
    if not logger.handlers:
        # handler que escribe en el archivo
        # mode='a' es para que agregue al final y no sobreescriba lo anterior
        handler_archivo = logging.FileHandler(RUTA_LOG, mode='a', encoding='utf-8')
        handler_archivo.setLevel(logging.DEBUG)

        # handler que muestra en consola tambien
        handler_consola = logging.StreamHandler()
        handler_consola.setLevel(logging.INFO)

        # formato de cada linea: fecha, nivel, nombre, mensaje
        formato = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler_archivo.setFormatter(formato)
        handler_consola.setFormatter(formato)

        # agrego los dos handlers al logger
        logger.addHandler(handler_archivo)
        logger.addHandler(handler_consola)

    return logger


# funciones rapidas para no repetir codigo en todos lados

def registrar_evento(mensaje):
    # para cosas exitosas (cliente creado, reserva confirmada, etc)
    logger = obtener_logger()
    logger.info(mensaje)


def registrar_error(mensaje, excepcion=None):
    # para errores que se atraparon
    # si paso la excepcion, la incluyo en el mensaje
    logger = obtener_logger()
    if excepcion is not None:
        # agrego el tipo y el detalle de la excepcion
        mensaje_completo = f"{mensaje} | Tipo: {type(excepcion).__name__} | Detalle: {excepcion}"
    else:
        mensaje_completo = mensaje
    logger.error(mensaje_completo)


def registrar_advertencia(mensaje):
    # para warnings (cosas raras pero no criticas)
    obtener_logger().warning(mensaje)
