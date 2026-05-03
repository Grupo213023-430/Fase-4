"""
cliente.py
==========
En este archivo tengo dos clases:
    - EntidadBase: clase abstracta de la que heredan todas las entidades
    - Cliente: hereda de EntidadBase y representa a un cliente

Aplico los pilares de la POO:
    - Abstraccion (clase abstracta con metodo abstracto)
    - Herencia (Cliente hereda de EntidadBase)
    - Encapsulacion (atributos privados con _ y properties)
    - Polimorfismo (mostrar_info se sobreescribe en cada subclase)

Autor: Sergio Esteban Duque Daza
CC: 1121930202
Correo: seduqued@unadvirtual.edu.co
Curso: Programacion Orientada a Objetos - Fase 4
Universidad Nacional Abierta y a Distancia (UNAD)
"""

# para hacer la clase abstracta
from abc import ABC, abstractmethod
# para la fecha de creacion
from datetime import datetime
# para validar el correo con expresion regular
import re
# para generar ids unicos automaticos
import uuid

# importo las excepciones que cree en excepciones.py
from excepciones import ClienteInvalidoError, CampoObligatorioError
# importo las funciones del logger
from logger import registrar_evento, registrar_error


# ===== CLASE ABSTRACTA =====
class EntidadBase(ABC):
    """
    Clase abstracta base. No se puede instanciar directamente.
    De aqui van a heredar Cliente, Servicio y demas entidades.
    """

    def __init__(self, id_entidad=None):
        # si no me pasan id, lo genero automatico con uuid
        # tomo solo los primeros 8 caracteres pa que no sea tan largo
        if id_entidad is None:
            id_entidad = str(uuid.uuid4())[:8]
        # atributos protegidos (con un _)
        self._id = id_entidad
        # guardo la fecha y hora exacta de cuando se creo
        self._fecha_creacion = datetime.now()

    # property para acceder al id desde afuera (solo lectura)
    @property
    def id(self):
        return self._id

    # property para la fecha de creacion (solo lectura)
    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    # metodo abstracto: cada subclase TIENE que implementarlo
    # si no lo hace, python no deja crear objetos de esa subclase
    @abstractmethod
    def mostrar_info(self):
        pass


# ===== CLASE CLIENTE =====
class Cliente(EntidadBase):
    """
    Representa a un cliente de Software FJ.
    Tiene encapsulacion (atributos privados) y validaciones en cada setter.
    """

    # patron para validar el correo
    # acepta letras, numeros y algunos simbolos antes y despues del @
    PATRON_CORREO = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
    # patron para el nombre: solo letras, espacios y vocales con tilde
    PATRON_NOMBRE = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$")

    def __init__(self, nombre, cedula, correo, telefono, edad):
        # llamo al constructor del padre para que asigne id y fecha
        super().__init__()

        # asigno los datos usando los setters (asi se ejecutan las validaciones)
        # si alguno falla se lanza la excepcion y el objeto no se crea
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo
        self.telefono = telefono
        self.edad = edad

        # si llego hasta aqui es porque todo paso bien
        # registro el evento en el log
        registrar_evento(
            f"Cliente creado correctamente -> id={self.id}, "
            f"nombre={self._nombre}, cedula={self._cedula}"
        )

    # ---------- NOMBRE ----------
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        # primero verifico que no sea None ni vacio
        if valor is None or str(valor).strip() == "":
            registrar_error("Intento de crear cliente con nombre vacio")
            raise CampoObligatorioError("nombre")
        # quito espacios al inicio y al final
        valor_limpio = str(valor).strip()
        # debe tener al menos 3 caracteres
        if len(valor_limpio) < 3:
            registrar_error(f"Nombre muy corto: '{valor_limpio}'")
            raise ClienteInvalidoError(
                f"El nombre debe tener al menos 3 caracteres: '{valor_limpio}'"
            )
        # verifico que solo tenga letras y espacios
        if not self.PATRON_NOMBRE.match(valor_limpio):
            registrar_error(f"Nombre con caracteres raros: '{valor_limpio}'")
            raise ClienteInvalidoError(
                f"El nombre solo puede tener letras y espacios: '{valor_limpio}'"
            )
        # si todo bien, lo guardo
        self._nombre = valor_limpio

    # ---------- CEDULA ----------
    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        # verifico campo obligatorio
        if valor is None or str(valor).strip() == "":
            registrar_error("Intento de crear cliente con cedula vacia")
            raise CampoObligatorioError("cedula")
        valor_limpio = str(valor).strip()
        # solo debe tener numeros
        if not valor_limpio.isdigit():
            registrar_error(f"Cedula con letras: '{valor_limpio}'")
            raise ClienteInvalidoError(
                f"La cedula solo puede tener numeros: '{valor_limpio}'"
            )
        # entre 6 y 10 digitos (rango normal en colombia)
        if not (6 <= len(valor_limpio) <= 10):
            registrar_error(f"Cedula muy corta o muy larga: '{valor_limpio}'")
            raise ClienteInvalidoError(
                f"La cedula debe tener entre 6 y 10 digitos: '{valor_limpio}'"
            )
        self._cedula = valor_limpio

    # ---------- CORREO ----------
    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if valor is None or str(valor).strip() == "":
            registrar_error("Intento de crear cliente con correo vacio")
            raise CampoObligatorioError("correo")
        # quito espacios y paso a minusculas
        # los correos no diferencian mayus/minus
        valor_limpio = str(valor).strip().lower()
        # uso el patron para validar el formato
        if not self.PATRON_CORREO.match(valor_limpio):
            registrar_error(f"Correo mal escrito: '{valor_limpio}'")
            raise ClienteInvalidoError(
                f"Formato de correo invalido: '{valor_limpio}'"
            )
        self._correo = valor_limpio

    # ---------- TELEFONO ----------
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if valor is None or str(valor).strip() == "":
            registrar_error("Intento de crear cliente con telefono vacio")
            raise CampoObligatorioError("telefono")
        valor_limpio = str(valor).strip()
        # solo numeros
        if not valor_limpio.isdigit():
            registrar_error(f"Telefono con letras: '{valor_limpio}'")
            raise ClienteInvalidoError(
                f"El telefono solo puede tener numeros: '{valor_limpio}'"
            )
        # longitud entre 7 y 10
        if not (7 <= len(valor_limpio) <= 10):
            registrar_error(f"Telefono con longitud rara: '{valor_limpio}'")
            raise ClienteInvalidoError(
                f"El telefono debe tener entre 7 y 10 digitos: '{valor_limpio}'"
            )
        self._telefono = valor_limpio

    # ---------- EDAD ----------
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        # no puede ser None
        if valor is None:
            registrar_error("Intento de crear cliente con edad vacia")
            raise CampoObligatorioError("edad")
        # intento convertir a entero
        # si me mandan algo como "treinta" va a fallar
        try:
            edad_int = int(valor)
        except (ValueError, TypeError) as error_original:
            registrar_error(f"Edad no se puede convertir a numero: '{valor}'", error_original)
            # aqui hago encadenamiento de excepciones con "from"
            # asi se conserva el error original para depurar despues
            raise ClienteInvalidoError(
                f"La edad debe ser un numero valido: '{valor}'"
            ) from error_original
        # rango logico (mayoria de edad para contratar servicios)
        if not (18 <= edad_int <= 120):
            registrar_error(f"Edad fuera del rango: {edad_int}")
            raise ClienteInvalidoError(
                f"La edad debe estar entre 18 y 120 años. Recibido: {edad_int}"
            )
        self._edad = edad_int

    # ---------- IMPLEMENTACION DEL METODO ABSTRACTO ----------
    def mostrar_info(self):
        # devuelvo un string con todos los datos del cliente
        return (
            f"[Cliente id={self._id}] "
            f"Nombre: {self._nombre} | "
            f"Cedula: {self._cedula} | "
            f"Correo: {self._correo} | "
            f"Telefono: {self._telefono} | "
            f"Edad: {self._edad} | "
            f"Registrado: {self._fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"
        )

    # esto es lo que se muestra cuando hago print(cliente)
    def __str__(self):
        return self.mostrar_info()

    # representacion mas tecnica (para debug)
    def __repr__(self):
        return f"Cliente(id='{self._id}', cedula='{self._cedula}')"
