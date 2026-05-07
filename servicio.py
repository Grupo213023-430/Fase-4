from abc import ABC, abstractmethod
from excepciones import (
    ServicioNoDisponibleError,
    ParametroServicioInvalidoError
)
from logger import registrar_evento


class Servicio(ABC):
    def __init__(self, nombre, precio_base, disponible=True):

        self._nombre = nombre
        self._precio_base = precio_base
        self._disponible = disponible

        if not nombre.strip():
            raise ParametroServicioInvalidoError(
                "El nombre del servicio no puede estar vacío"
            )

        if precio_base <= 0:
            raise ParametroServicioInvalidoError(
                "El precio base debe ser mayor a cero"
            )

    # Encapsulación con property
    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @property
    def disponible(self):
        return self._disponible

    @abstractmethod
    def calcular_costo(self, tiempo, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass


# ==========================================
# RESERVA DE SALA
# ==========================================

class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, capacidad):
        super().__init__(nombre, precio_base)

        self._capacidad = capacidad

    @property
    def capacidad(self):
        return self._capacidad

    def calcular_costo(self, horas, impuesto=0, descuento=0):

        try:

            if horas <= 0:
                raise ValueError("Las horas deben ser mayores a cero")

            costo = horas * self._precio_base

            costo += costo * impuesto
            costo -= costo * descuento

            registrar_evento(
                f"Cálculo exitoso de reserva de sala: {costo}"
            )

            return costo

        except ValueError as e:

            registrar_evento(
                f"Error al calcular reserva de sala: {e}"
            )

            raise ParametroServicioInvalidoError(
                "Error en cálculo de reserva de sala"
            ) from e

    def mostrar_info(self):

        return (
            f"Servicio: {self._nombre} | "
            f"Precio Base: {self._precio_base} | "
            f"Capacidad: {self._capacidad}"
        )


# ==========================================
# ALQUILER DE EQUIPOS
# ==========================================

class AlquilerEquipos(Servicio):

    def __init__(self, nombre, precio_base, tipo_equipo):
        super().__init__(nombre, precio_base)

        self._tipo_equipo = tipo_equipo

    @property
    def tipo_equipo(self):
        return self._tipo_equipo

    def calcular_costo(self, dias, impuesto=0, descuento=0):

        try:

            if dias <= 0:
                raise ValueError("Los días deben ser mayores a cero")

            costo = dias * self._precio_base

            costo += costo * impuesto
            costo -= costo * descuento

            registrar_evento(
                f"Cálculo exitoso alquiler equipo: {costo}"
            )

            return costo

        except ValueError as e:

            registrar_evento(
                f"Error alquiler equipo: {e}"
            )

            raise ParametroServicioInvalidoError(
                "Error en alquiler de equipos"
            ) from e

    def mostrar_info(self):

        return (
            f"Servicio: {self._nombre} | "
            f"Precio Base: {self._precio_base} | "
            f"Tipo Equipo: {self._tipo_equipo}"
        )


# ==========================================
# ASESORÍA ESPECIALIZADA
# ==========================================

class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio_base, especialidad):
        super().__init__(nombre, precio_base)

        self._especialidad = especialidad

    @property
    def especialidad(self):
        return self._especialidad

    def calcular_costo(self, horas, impuesto=0, descuento=0):

        try:

            if horas <= 0:
                raise ValueError("Las horas deben ser mayores a cero")

            costo = horas * self._precio_base

            costo += costo * impuesto
            costo -= costo * descuento

            registrar_evento(
                f"Cálculo exitoso asesoría: {costo}"
            )

            return costo

        except ValueError as e:

            registrar_evento(
                f"Error asesoría especializada: {e}"
            )

            raise ParametroServicioInvalidoError(
                "Error en asesoría especializada"
            ) from e

    def mostrar_info(self):

        return (
            f"Servicio: {self._nombre} | "
            f"Precio Base: {self._precio_base} | "
            f"Especialidad: {self._especialidad}"
        )
