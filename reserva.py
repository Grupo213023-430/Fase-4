from excepciones import ReservaInvalidaError, EstadoReservaError
from logger import registrar_evento


class Reserva:
    def __init__(self, cliente, servicio, cantidad):
        if cliente is None:
            raise ReservaInvalidaError("Debe haber un cliente")
        if servicio is None:
            raise ReservaInvalidaError("Debe haber un servicio")
        if cantidad <= 0:
            raise ReservaInvalidaError("Cantidad inválida")

        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = "CREADA"
        self.total = 0

    def confirmar(self):
        if self.estado != "CREADA":
            raise EstadoReservaError("Solo se puede confirmar una reserva creada")

        self.servicio.validar_disponibilidad()
        self.total = self.servicio.calcular_costo(self.cantidad)
        self.estado = "CONFIRMADA"

        registrar_evento(f"Reserva confirmada -> Cliente: {self.cliente.nombre}, Total: {self.total}")
        return f"Reserva confirmada. Total: ${self.total}"

    def cancelar(self):
        if self.estado == "CANCELADA":
            raise EstadoReservaError("Ya está cancelada")
        self.estado = "CANCELADA"
        return "Reserva cancelada"

    def procesar(self):
        if self.estado != "CONFIRMADA":
            raise EstadoReservaError("Solo se procesan reservas confirmadas")
        self.estado = "PROCESADA"
        return "Reserva procesada"