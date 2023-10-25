def concat(a, b):
    """
    este metodo suma dos nums
    """
    return a + b


def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


def saludar(nombre, saludo="Hola"):
    mensaje = saludo + ", " + nombre
    return mensaje


def mult_by_five(x):
    return 5 * x


def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)


def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))


def modLista(funcion, lista):
    lista2 = []
    for elemento in lista:
        lista2.append(funcion(elemento))

    return lista2


numeros = [1, 2, 3, 4, 5]


# print(modLista(mult_by_five, numeros))


def filter(function, list):
    list2 = []
    for element in list:
        if function(element):
            list2.append(element)

    return list2


def isPar(n):
    return n % 2 == 0


numeros2 = [41, 12, 53, 43, 32]


# print(filter(isPar, numeros2))

def map(function, list):
    list2 = []
    for element in list:
        list2.append(function(element))
    return list2


def toLen(palabra):
    return len(palabra)


palabras = ["hola", "mundo"]
#print(map(toLen, palabras))

print(True+False+True)
