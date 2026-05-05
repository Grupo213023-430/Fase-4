from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponibleError, ParametroServicioInvalidoError
from logger import registrar_evento


class Servicio(ABC):
    def __init__(self, nombre, precio_base, disponible=True):
        if not nombre:
            raise ParametroServicioInvalidoError("El nombre del servicio es obligatorio")
        if precio_base <= 0:
            raise ParametroServicioInvalidoError("El precio debe ser mayor a 0")

        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = disponible

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError(f"{self.nombre} no está disponible")

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass


# ===== SERVICIOS =====

class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        if horas <= 0:
            raise ParametroServicioInvalidoError("Horas inválidas")
        return self.precio_base * horas


class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias):
        if dias <= 0:
            raise ParametroServicioInvalidoError("Días inválidos")
        seguro = 10000
        return (self.precio_base * dias) + seguro


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones):
        if sesiones <= 0:
            raise ParametroServicioInvalidoError("Sesiones inválidas")
        tarifa_extra = 20000
        return (self.precio_base * sesiones) + tarifa_extra