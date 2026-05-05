from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import SoftwareFJError
from logger import registrar_evento, registrar_error


def ejecutar_operacion(num, descripcion, funcion):
    print(f"\n=== Operación {num}: {descripcion} ===")
    try:
        resultado = funcion()
    except SoftwareFJError as e:
        print(f"Error controlado: {e}")
        registrar_error(str(e))
    except Exception as e:
        print(f"Error inesperado: {e}")
        registrar_error("Error inesperado", e)
    else:
        print(resultado)
    finally:
        print("Fin de la operación")


# LISTAS DEL SISTEMA
clientes = []
servicios = []
reservas = []


# ===== OPERACIONES =====

def op1():
    c = Cliente("Carlos Perez", "1234567", "carlos@mail.com", "3001234567", 30)
    clientes.append(c)
    return c.mostrar_info()


def op2():
    return Cliente("", "1234567", "correo@mail.com", "3001234567", 30)


def op3():
    return Cliente("Ana", "ABC123", "correo@mail.com", "3001234567", 25)


def op4():
    s = ReservaSala("Sala VIP", 50000)
    servicios.append(s)
    return "Servicio creado"


def op5():
    s = AlquilerEquipo("Proyector", 40000)
    servicios.append(s)
    return "Servicio creado"


def op6():
    s = AsesoriaEspecializada("Consultoría", 80000)
    servicios.append(s)
    return "Servicio creado"


def op7():
    return ReservaSala("Sala barata", -1000)


def op8():
    r = Reserva(clientes[0], servicios[0], 2)
    reservas.append(r)
    return r.confirmar()


def op9():
    r = Reserva(clientes[0], servicios[1], 0)
    reservas.append(r)
    return r.confirmar()


def op10():
    s = AsesoriaEspecializada("Servicio apagado", 70000, disponible=False)
    r = Reserva(clientes[0], s, 2)
    return r.confirmar()


def op11():
    return reservas[0].cancelar()


def op12():
    return reservas[0].procesar()


# ===== EJECUCION =====

if __name__ == "__main__":
    registrar_evento("=== INICIO DEL SISTEMA ===")

    ejecutar_operacion(1, "Cliente válido", op1)
    ejecutar_operacion(2, "Cliente inválido (nombre vacío)", op2)
    ejecutar_operacion(3, "Cliente inválido (cédula)", op3)
    ejecutar_operacion(4, "Crear servicio sala", op4)
    ejecutar_operacion(5, "Crear servicio equipo", op5)
    ejecutar_operacion(6, "Crear servicio asesoría", op6)
    ejecutar_operacion(7, "Servicio con precio inválido", op7)
    ejecutar_operacion(8, "Reserva exitosa", op8)
    ejecutar_operacion(9, "Reserva inválida (cantidad)", op9)
    ejecutar_operacion(10, "Servicio no disponible", op10)
    ejecutar_operacion(11, "Cancelar reserva", op11)
    ejecutar_operacion(12, "Procesar reserva cancelada", op12)

    registrar_evento("=== FIN DEL SISTEMA ===")