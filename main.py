"""
main.py
=======
Archivo principal del sistema Software FJ.

Desde aquí se ejecutan las pruebas del sistema:
- Clientes
- Servicios
- Reservas
- Manejo de excepciones
- Logs
- Integración completa del proyecto

Se realizan operaciones válidas e inválidas
para demostrar el manejo robusto del sistema.

Autor: Alan Correa
Curso: Programación Orientada a Objetos - Fase 4
Universidad Nacional Abierta y a Distancia (UNAD)
"""

from cliente import Cliente

from servicio import (
    ReservaSala,
    AlquilerEquipos,
    AsesoriaEspecializada
)

from reserva import Reserva

from excepciones import SoftwareFJError

from logger import (
    registrar_evento,
    registrar_error
)


# ==========================================
# LISTAS DEL SISTEMA
# ==========================================

clientes = []
servicios = []
reservas = []


# ==========================================
# FUNCIÓN GENERAL DE EJECUCIÓN
# ==========================================

def ejecutar_operacion(numero, descripcion, funcion):

    print(f"\n{'=' * 60}")
    print(f"OPERACIÓN {numero}: {descripcion}")
    print(f"{'=' * 60}")

    try:

        resultado = funcion()

    except SoftwareFJError as e:

        print(f"Error controlado: {e}")

        registrar_error(
            "Error controlado",
            e
        )

    except Exception as e:

        print(f"Error inesperado: {e}")

        registrar_error(
            "Error inesperado",
            e
        )

    else:
        print(resultado)

    finally:
        print("Fin de la operación")


# ==========================================
# OPERACIÓN 1
# Cliente válido
# ==========================================

def op1():

    c = Cliente(
        "Carlos Perez",
        "1234567",
        "carlos@mail.com",
        "3001234567",
        30
    )

    clientes.append(c)

    return c.mostrar_info()


# ==========================================
# OPERACIÓN 2
# Cliente inválido (nombre vacío)
# ==========================================

def op2():

    return Cliente(
        "",
        "1234567",
        "correo@mail.com",
        "3001234567",
        30
    )


# ==========================================
# OPERACIÓN 3
# Cliente inválido (cédula incorrecta)
# ==========================================

def op3():

    return Cliente(
        "Ana",
        "ABC123",
        "correo@mail.com",
        "3001234567",
        25
    )


# ==========================================
# OPERACIÓN 4
# Crear reserva de sala
# ==========================================

def op4():

    s = ReservaSala(
        "Sala VIP",
        50000,
        20
    )

    servicios.append(s)

    return s.mostrar_info()


# ==========================================
# OPERACIÓN 5
# Crear alquiler de equipos
# ==========================================

def op5():

    s = AlquilerEquipos(
        "Proyector",
        40000,
        "Video Beam"
    )

    servicios.append(s)

    return s.mostrar_info()


# ==========================================
# OPERACIÓN 6
# Crear asesoría especializada
# ==========================================

def op6():

    s = AsesoriaEspecializada(
        "Consultoría",
        80000,
        "Python"
    )

    servicios.append(s)

    return s.mostrar_info()


# ==========================================
# OPERACIÓN 7
# Servicio inválido
# ==========================================

def op7():

    return ReservaSala(
        "Sala barata",
        -1000,
        10
    )


# ==========================================
# OPERACIÓN 8
# Reserva exitosa
# ==========================================

def op8():

    r = Reserva(
        clientes[0],
        servicios[0],
        2
    )

    reservas.append(r)

    return r.confirmar()


# ==========================================
# OPERACIÓN 9
# Reserva inválida
# ==========================================

def op9():

    r = Reserva(
        clientes[0],
        servicios[1],
        0
    )

    reservas.append(r)

    return r.confirmar()


# ==========================================
# OPERACIÓN 10
# Servicio no disponible
# ==========================================

def op10():

    s = AsesoriaEspecializada(
        "Servicio apagado",
        70000,
        "IA",
        disponible=False
    )

    r = Reserva(
        clientes[0],
        s,
        2
    )

    return r.confirmar()


# ==========================================
# OPERACIÓN 11
# Cancelar reserva
# ==========================================

def op11():

    return reservas[0].cancelar()


# ==========================================
# OPERACIÓN 12
# Procesar reserva cancelada
# ==========================================

def op12():

    return reservas[0].procesar()


# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================

if __name__ == "__main__":

    registrar_evento(
        "=== INICIO DEL SISTEMA ==="
    )

    ejecutar_operacion(
        1,
        "Cliente válido",
        op1
    )

    ejecutar_operacion(
        2,
        "Cliente inválido (nombre vacío)",
        op2
    )

    ejecutar_operacion(
        3,
        "Cliente inválido (cédula incorrecta)",
        op3
    )

    ejecutar_operacion(
        4,
        "Crear reserva de sala",
        op4
    )

    ejecutar_operacion(
        5,
        "Crear alquiler de equipos",
        op5
    )

    ejecutar_operacion(
        6,
        "Crear asesoría especializada",
        op6
    )

    ejecutar_operacion(
        7,
        "Servicio inválido",
        op7
    )

    ejecutar_operacion(
        8,
        "Reserva exitosa",
        op8
    )

    ejecutar_operacion(
        9,
        "Reserva inválida",
        op9
    )

    ejecutar_operacion(
        10,
        "Servicio no disponible",
        op10
    )

    ejecutar_operacion(
        11,
        "Cancelar reserva",
        op11
    )

    ejecutar_operacion(
        12,
        "Procesar reserva cancelada",
        op12
    )

    registrar_evento(
        "=== FIN DEL SISTEMA ==="
    )