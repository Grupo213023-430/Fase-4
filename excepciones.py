"""
excepciones.py
==============
Modulo de excepciones personalizadas del sistema Software FJ.

Aqui defino la jerarquia de errores que se pueden lanzar en el sistema.
Todas las excepciones heredan de SoftwareFJError, asi puedo atraparlas
de forma especifica o todas juntas con un solo except.

Autor: Sergio Esteban Duque Daza
CC: 1121930202
Correo: seduqued@unadvirtual.edu.co
Curso: Programacion Orientada a Objetos - Fase 4
Universidad Nacional Abierta y a Distancia (UNAD)
"""


# clase padre de todas las excepciones del sistema
class SoftwareFJError(Exception):
    def __init__(self, mensaje="Error generico del sistema"):
        # guardo el mensaje
        self.mensaje = mensaje
        # llamo al constructor de Exception
        super().__init__(self.mensaje)


# ===== Excepciones del cliente =====

class ClienteInvalidoError(SoftwareFJError):
    # cuando los datos del cliente no son validos
    def __init__(self, mensaje="Datos de cliente invalidos"):
        super().__init__(mensaje)


class CampoObligatorioError(SoftwareFJError):
    # cuando falta un campo obligatorio (nombre, cedula, etc)
    def __init__(self, campo):
        # guardo el nombre del campo que fallo
        self.campo = campo
        mensaje = f"El campo '{campo}' no puede estar vacio"
        super().__init__(mensaje)


# ===== Excepciones de los servicios =====
# estas las van a usar los compañeros en servicio.py

class ServicioNoDisponibleError(SoftwareFJError):
    # cuando el servicio no esta disponible
    def __init__(self, mensaje="El servicio no esta disponible"):
        super().__init__(mensaje)


class ParametroServicioInvalidoError(SoftwareFJError):
    # cuando los parametros del servicio son invalidos
    def __init__(self, mensaje="Parametros del servicio invalidos"):
        super().__init__(mensaje)


# ===== Excepciones de las reservas =====

class ReservaInvalidaError(SoftwareFJError):
    # cuando la reserva no se puede crear bien
    def __init__(self, mensaje="La reserva no es valida"):
        super().__init__(mensaje)


class EstadoReservaError(SoftwareFJError):
    # cuando se intenta cambiar a un estado que no se puede
    # ej: confirmar una reserva ya cancelada
    def __init__(self, mensaje="Cambio de estado no permitido"):
        super().__init__(mensaje)


# ===== Excepcion de calculos =====

class CalculoInconsistenteError(SoftwareFJError):
    # cuando un calculo da un resultado raro (negativo, infinito, etc)
    def __init__(self, mensaje="Resultado del calculo inconsistente"):
        super().__init__(mensaje)
