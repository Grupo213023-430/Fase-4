"""
servicio.py
===========
Clases de servicios del sistema Software FJ.

Este módulo contiene:
- Clase abstracta Servicio
- ReservaSala
- AlquilerEquipos
- AsesoriaEspecializada

Se aplican conceptos de:
- Abstracción
- Herencia
- Encapsulación
- Polimorfismo
- Manejo avanzado de excepciones
- Sobrecarga de métodos
- Integración con logger

Autor: Alan Correa
Curso: Programación Orientada a Objetos - Fase 4
Universidad Nacional Abierta y a Distancia (UNAD)
"""

from abc import abstractmethod

from cliente import EntidadBase

from excepciones import (
    ServicioNoDisponibleError,
    ParametroServicioInvalidoError
)

from logger import (
    registrar_evento,
    registrar_error
)


# ==========================================
# CLASE ABSTRACTA SERVICIO
# ==========================================

class Servicio(EntidadBase):

    def __init__(self, nombre, precio_base, disponible=True):

        super().__init__()

        self._nombre = nombre
        self._precio_base = precio_base
        self._disponible = disponible

        self.validar_parametros()

    # ======================================
    # ENCAPSULACIÓN
    # ======================================

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @property
    def disponible(self):
        return self._disponible

    # ======================================
    # MÉTODOS ABSTRACTOS
    # ======================================

    @abstractmethod
    def calcular_costo(
        self,
        tiempo,
        impuesto=0,
        descuento=0
    ):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass

    # ======================================
    # DISPONIBILIDAD
    # ======================================

    def validar_disponibilidad(self):

        if not self._disponible:

            registrar_error(
                f"Servicio no disponible: {self._nombre}"
            )

            raise ServicioNoDisponibleError(
                f"El servicio '{self._nombre}' no está disponible"
            )


# ==========================================
# RESERVA DE SALA
# ==========================================

class ReservaSala(Servicio):

    def __init__(
        self,
        nombre,
        precio_base,
        capacidad,
        disponible=True
    ):

        self._capacidad = capacidad

        super().__init__(
            nombre,
            precio_base,
            disponible
        )

    @property
    def capacidad(self):
        return self._capacidad

    def validar_parametros(self):

        if not self._nombre.strip():

            raise ParametroServicioInvalidoError(
                "El nombre del servicio no puede estar vacío"
            )

        if self._precio_base <= 0:

            raise ParametroServicioInvalidoError(
                "El precio base debe ser mayor a cero"
            )

        if self._capacidad <= 0:

            raise ParametroServicioInvalidoError(
                "La capacidad debe ser mayor a cero"
            )

    def describir(self):

        return (
            f"Reserva de sala con capacidad "
            f"para {self._capacidad} personas"
        )

    def calcular_costo(
        self,
        horas,
        impuesto=0,
        descuento=0
    ):

        try:

            if horas <= 0:
                raise ValueError(
                    "Las horas deben ser mayores a cero"
                )

            costo = horas * self._precio_base

            costo += costo * impuesto

            costo -= costo * descuento

            registrar_evento(
                f"Cálculo exitoso reserva sala: {costo}"
            )

            return costo

        except ValueError as e:

            registrar_error(
                "Error cálculo reserva sala",
                e
            )

            raise ParametroServicioInvalidoError(
                "Error en reserva de sala"
            ) from e

    def mostrar_info(self):

        return (
            f"[Servicio id={self.id}] "
            f"Nombre: {self._nombre} | "
            f"Precio Base: {self._precio_base} | "
            f"Capacidad: {self._capacidad}"
        )

    def __str__(self):

        return self.mostrar_info()


# ==========================================
# ALQUILER DE EQUIPOS
# ==========================================

class AlquilerEquipos(Servicio):

    def __init__(
        self,
        nombre,
        precio_base,
        tipo_equipo,
        disponible=True
    ):

        self._tipo_equipo = tipo_equipo

        super().__init__(
            nombre,
            precio_base,
            disponible
        )

    @property
    def tipo_equipo(self):
        return self._tipo_equipo

    def validar_parametros(self):

        if not self._nombre.strip():

            raise ParametroServicioInvalidoError(
                "El nombre del servicio no puede estar vacío"
            )

        if self._precio_base <= 0:

            raise ParametroServicioInvalidoError(
                "El precio base debe ser mayor a cero"
            )

        if not self._tipo_equipo.strip():

            raise ParametroServicioInvalidoError(
                "Debe indicar un tipo de equipo"
            )

    def describir(self):

        return (
            f"Alquiler de equipos tipo "
            f"{self._tipo_equipo}"
        )

    def calcular_costo(
        self,
        dias,
        impuesto=0,
        descuento=0
    ):

        try:

            if dias <= 0:
                raise ValueError(
                    "Los días deben ser mayores a cero"
                )

            costo = dias * self._precio_base

            costo += costo * impuesto

            costo -= costo * descuento

            registrar_evento(
                f"Cálculo exitoso alquiler equipos: {costo}"
            )

            return costo

        except ValueError as e:

            registrar_error(
                "Error alquiler equipos",
                e
            )

            raise ParametroServicioInvalidoError(
                "Error en alquiler de equipos"
            ) from e

    def mostrar_info(self):

        return (
            f"[Servicio id={self.id}] "
            f"Nombre: {self._nombre} | "
            f"Precio Base: {self._precio_base} | "
            f"Tipo Equipo: {self._tipo_equipo}"
        )

    def __str__(self):

        return self.mostrar_info()


# ==========================================
# ASESORÍA ESPECIALIZADA
# ==========================================

class AsesoriaEspecializada(Servicio):

    def __init__(
        self,
        nombre,
        precio_base,
        especialidad,
        disponible=True
    ):

        self._especialidad = especialidad

        super().__init__(
            nombre,
            precio_base,
            disponible
        )

    @property
    def especialidad(self):
        return self._especialidad

    def validar_parametros(self):

        if not self._nombre.strip():

            raise ParametroServicioInvalidoError(
                "El nombre del servicio no puede estar vacío"
            )

        if self._precio_base <= 0:

            raise ParametroServicioInvalidoError(
                "El precio base debe ser mayor a cero"
            )

        if not self._especialidad.strip():

            raise ParametroServicioInvalidoError(
                "Debe indicar una especialidad"
            )

    def describir(self):

        return (
            f"Asesoría especializada en "
            f"{self._especialidad}"
        )

    def calcular_costo(
        self,
        horas,
        impuesto=0,
        descuento=0
    ):

        try:

            if horas <= 0:
                raise ValueError(
                    "Las horas deben ser mayores a cero"
                )

            costo = horas * self._precio_base

            costo += costo * impuesto

            costo -= costo * descuento

            registrar_evento(
                f"Cálculo exitoso asesoría: {costo}"
            )

            return costo

        except ValueError as e:

            registrar_error(
                "Error asesoría especializada",
                e
            )

            raise ParametroServicioInvalidoError(
                "Error en asesoría especializada"
            ) from e

    def mostrar_info(self):

        return (
            f"[Servicio id={self.id}] "
            f"Nombre: {self._nombre} | "
            f"Precio Base: {self._precio_base} | "
            f"Especialidad: {self._especialidad}"
        )

    def __str__(self):

        return self.mostrar_info()