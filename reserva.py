"""
reserva.py
==========
Clase Reserva del sistema Software FJ.

Esta clase permite gestionar las reservas realizadas por los clientes
para los diferentes servicios ofrecidos por la empresa.

Se aplican conceptos de:
- Encapsulación
- Manejo de excepciones
- Integración con logger
- Validaciones
- Polimorfismo
- Manejo de estados

Autor: Alan Correa
Curso: Programación Orientada a Objetos - Fase 4
Universidad Nacional Abierta y a Distancia (UNAD)
"""

from excepciones import (
    ReservaInvalidaError,
    EstadoReservaError
)

from logger import (
    registrar_evento,
    registrar_error
)


class Reserva:

    def __init__(self, cliente, servicio, cantidad):

        if cliente is None:
            raise ReservaInvalidaError(
                "Debe existir un cliente"
            )

        if servicio is None:
            raise ReservaInvalidaError(
                "Debe existir un servicio"
            )

        if cantidad <= 0:
            raise ReservaInvalidaError(
                "La cantidad debe ser mayor a cero"
            )

        # Encapsulación
        self._cliente = cliente
        self._servicio = servicio
        self._cantidad = cantidad

        self._estado = "CREADA"
        self._total = 0

        registrar_evento(
            f"Reserva creada -> Cliente: {self._cliente.nombre}"
        )

    # ==============================
    # PROPERTIES
    # ==============================

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def estado(self):
        return self._estado

    @property
    def total(self):
        return self._total

    # ==============================
    # MÉTODOS
    # ==============================

    def confirmar(self):

        try:

            if self._estado != "CREADA":

                raise EstadoReservaError(
                    "Solo se puede confirmar una reserva creada"
                )

            # valida si el servicio está disponible
            self._servicio.validar_disponibilidad()

            # cálculo con impuesto y descuento
            self._total = self._servicio.calcular_costo(
                self._cantidad,
                impuesto=0.19,
                descuento=0.05
            )

            self._estado = "CONFIRMADA"

            registrar_evento(
                f"Reserva confirmada -> "
                f"Cliente: {self._cliente.nombre}, "
                f"Total: {self._total}"
            )

            return (
                f"Reserva confirmada. "
                f"Total: ${self._total}"
            )

        except Exception as e:

            registrar_error(
                "Error al confirmar reserva",
                e
            )

            raise EstadoReservaError(
                "No fue posible confirmar la reserva"
            ) from e

    def cancelar(self):

        if self._estado == "CANCELADA":

            raise EstadoReservaError(
                "La reserva ya fue cancelada"
            )

        self._estado = "CANCELADA"

        registrar_evento(
            f"Reserva cancelada -> "
            f"Cliente: {self._cliente.nombre}"
        )

        return "Reserva cancelada"

    def procesar(self):

        if self._estado != "CONFIRMADA":

            raise EstadoReservaError(
                "Solo se procesan reservas confirmadas"
            )

        self._estado = "PROCESADA"

        registrar_evento(
            f"Reserva procesada -> "
            f"Cliente: {self._cliente.nombre}"
        )

        return "Reserva procesada"

    # ==============================
    # POLIMORFISMO
    # ==============================

    def mostrar_info(self):

        return (
            f"[Reserva] "
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | "
            f"Cantidad: {self._cantidad} | "
            f"Estado: {self._estado} | "
            f"Total: {self._total}"
        )

    def __str__(self):

        return self.mostrar_info()

    def __repr__(self):

        return (
            f"Reserva("
            f"cliente='{self._cliente.nombre}', "
            f"estado='{self._estado}', "
            f"total={self._total}"
            f")"
        )