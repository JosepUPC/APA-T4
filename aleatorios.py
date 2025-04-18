'''
0. Nombre y Apellido

Josep Esquerrà Bayo

1. Descripción

Este documnento contiene una clase para la generación de números aleatorios usando el algoritmo LGC.
Dentro de la clase se pueden apreciar unas funciones de clase que generan los números alratorios usando la clase.
Ademas, dicha clase continen un función para poder generar numeros aleatorios.
Finalmente, se ha añadido unos test en la cadena de texto con la función verbosa.

2. Clase Aleat

    -Contenido

Conjunto de métodos para definir una variable como un objeto y una funcion que poder ejecutar directamente

    -Métodos

método init() por default de la clase junto con atributos definidios con variables fijas (a, c, m, x0)
método next() para poder iterar el siguiente objeto de la clase
método call() para poder modificar la variable x y modificar la aletoriedad del valor de salida

    -Pruebas unitarias de Aleat

        Comprobación del funcionamiento de Aleat

>>> rand = Aleat(m=32, a=9, c=13, x0=11)
>>> for _ in range(4):
...     print(next(rand))
...
16
29
18
15

        Comprobación del reinicio de Aleat

>>> rand(29)
>>> for _ in range(4):
...     print(next(rand))
...
18
15
20
1

3. funcion aleat

    -Contenido

funcion que da un valor aleatorio por cada iteracion que se la de. Puede usarse la funcion send para poder variar la variable de entrada x

    -I/O

Mismas variables de inicio que en la función __init__(), función yield para pausar el bucle i tener un valor por cada llamada de al función. Comprovación si és que reciven un valor de entrada

    -Pruebas unitarias de aleat()

        Comprobación del funcionamiento de aleat()

>>> rand = aleat(m=64, a=5, c=46, x0=36)
>>> for _ in range(4):
...     print(next(rand))
...
34
24
38
44

        Comprobación del reinicio de aleat()

>>> rand.send(24)
38
>>> for _ in range(4):
...     print(next(rand))
...
44
10
32
14

'''

# Clase Aleat
class Aleat:
    def __init__(self, *, m=2**31, a=1103515245, c=12345, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x
    
    def __call__(self, value):
        self.x = value

# Función generadora
def aleat(*, m=2**31, a=1103515245, c=12345, x0=1212121):
    x = x0
    while True:
        rebut = (yield x)
        if rebut is not None:
            x = rebut
        x = (a * x + c) % m

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)