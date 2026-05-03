"""
prueba_base.py
==============
Script para probar mi parte antes de subir al git.
Pruebo la clase Cliente con casos validos e invalidos
para asegurarme que las excepciones funcionan bien.

NOTA: Esto es solo para mis pruebas, no se entrega.
El main.py final lo va a hacer el compañero Alan cuando integre todo.

Autor: Sergio Esteban Duque Daza
CC: 1121930202
Correo: seduqued@unadvirtual.edu.co
Curso: Programacion Orientada a Objetos - Fase 4
Universidad Nacional Abierta y a Distancia (UNAD)
"""

from cliente import Cliente
from excepciones import ClienteInvalidoError, CampoObligatorioError, SoftwareFJError
from logger import registrar_evento


def imprimir_separador(titulo):
    # solo para que la salida en consola se vea ordenada
    print("\n" + "=" * 60)
    print(f" {titulo}")
    print("=" * 60)


if __name__ == "__main__":
    # registro el inicio en el log
    registrar_evento("=== INICIO DE PRUEBAS DE LA BASE ===")

    # ===== PRUEBA 1: cliente valido (uso mis datos reales) =====
    imprimir_separador("PRUEBA 1: Cliente valido")
    try:
        cliente_ok = Cliente(
            nombre="Sergio Esteban Duque Daza",
            cedula="1121930202",
            correo="seduqued@unadvirtual.edu.co",
            telefono="3001234567",
            edad=28,
        )
        print("Cliente creado bien:")
        print(cliente_ok.mostrar_info())
    except SoftwareFJError as e:
        print(f"Error inesperado: {e}")

    # ===== PRUEBA 2: nombre vacio =====
    imprimir_separador("PRUEBA 2: Nombre vacio (debe fallar)")
    try:
        Cliente(nombre="", cedula="1234567", correo="a@b.com",
                telefono="3001234567", edad=25)
    except CampoObligatorioError as e:
        # esta excepcion la espero porque el nombre esta vacio
        print(f"OK - excepcion atrapada: {e}")

    # ===== PRUEBA 3: cedula con letras =====
    imprimir_separador("PRUEBA 3: Cedula con letras (debe fallar)")
    try:
        Cliente(nombre="Irma Coello Angarita", cedula="ABC123",
                correo="irma@mail.com", telefono="3001234567", edad=30)
    except ClienteInvalidoError as e:
        print(f"OK - excepcion atrapada: {e}")

    # ===== PRUEBA 4: correo mal escrito =====
    imprimir_separador("PRUEBA 4: Correo invalido (debe fallar)")
    try:
        Cliente(nombre="Alan Correa Mendes", cedula="9876543",
                correo="correo-malo", telefono="3009876543", edad=22)
    except ClienteInvalidoError as e:
        print(f"OK - excepcion atrapada: {e}")

    # ===== PRUEBA 5: edad menor =====
    imprimir_separador("PRUEBA 5: Edad menor a 18 (debe fallar)")
    try:
        Cliente(nombre="Carlos Ruiz", cedula="1122334", correo="c@x.com",
                telefono="3201112233", edad=15)
    except ClienteInvalidoError as e:
        print(f"OK - excepcion atrapada: {e}")

    # ===== PRUEBA 6: edad no numerica (encadenamiento) =====
    imprimir_separador("PRUEBA 6: Edad no numerica")
    try:
        Cliente(nombre="Diana Mora", cedula="5566778", correo="d@y.com",
                telefono="3151112233", edad="treinta")
    except ClienteInvalidoError as e:
        print(f"OK - excepcion atrapada: {e}")
        # __cause__ me muestra la excepcion original que se encadeno
        print(f"Causa original: {e.__cause__}")

    # ===== PRUEBA 7: el sistema sigue activo =====
    imprimir_separador("PRUEBA 7: Sistema sigue funcionando")
    try:
        # creo otro cliente valido para mostrar que despues de
        # los errores el sistema no se cayo
        cliente_ok_2 = Cliente(
            nombre="Maria Gomez",
            cedula="9988776",
            correo="maria.gomez@correo.com",
            telefono="3151234567",
            edad=35,
        )
        print("El sistema sigue activo. Otro cliente creado:")
        print(cliente_ok_2.mostrar_info())
    except SoftwareFJError as e:
        print(f"Error inesperado: {e}")

    registrar_evento("=== FIN DE PRUEBAS ===")
    print("\nListo. Revisa logs.txt para ver el registro completo.")
