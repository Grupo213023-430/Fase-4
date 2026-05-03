# Fase 4 - Software FJ

Trabajo de la fase 4 del curso de Programacion Orientada a Objetos de la UNAD.

Es un sistema en python para gestionar clientes, servicios y reservas de la empresa Software FJ. No usa base de datos, todo se maneja con objetos, listas y archivos (logs.txt para los errores y eventos).

## Integrantes del grupo

- Sergio Esteban Duque Daza -  (lider)
- Irma Leticia Coello Angarita
- Alan Correa Mendes

## Como dividimos el trabajo

- Sergio: clase abstracta EntidadBase, clase Cliente, excepciones y logger
- Irma: clase abstracta Servicio y las 3 clases hijas (salas, equipos, asesorias)
- Alan: clase Reserva, main.py y la simulacion de las 10 operaciones

## Archivos del proyecto

```
cliente.py        -> EntidadBase y Cliente
servicio.py       -> Servicio y subclases
reserva.py        -> Reserva
excepciones.py    -> excepciones personalizadas
logger.py         -> configuracion de logs
main.py           -> archivo principal con la simulacion
logs.txt          -> aqui se guardan los eventos y errores
```

## Lo que aplica el codigo

- Abstraccion (clases abstractas con ABC)
- Herencia
- Encapsulacion (atributos privados con _ y properties)
- Polimorfismo (metodos sobreescritos)
- Manejo de excepciones (try/except, try/except/else, try/except/finally)
- Excepciones personalizadas
- Encadenamiento de excepciones (raise ... from ...)
- Sobrecarga de metodos (con parametros opcionales)
- Manejo de archivos (logs.txt)

## Como ejecutar

```
python main.py
```

Despues se puede revisar el archivo logs.txt para ver lo que paso.

## Ramas del repo

Cada uno trabaja en su propia rama y abre un Pull Request al terminar:

- feature/cliente-base (Sergio)
- feature/servicios (Irma)
- feature/reservas (Alan)
