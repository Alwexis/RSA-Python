from os import system

def isPrime(n):
    if n > 1:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True
    return False

def cifrar(msg: str, key: list):
    msgChars = []
    for x in msg:
        c = ord(x)
        # Según la fórmula: C = M^e mod n
        result = (c**key[1]) % key[0]
        msgChars.append(result)
    return " ".join([str(x) for x in msgChars])

def descifrar(msg: str, key: list):
    msgChars = []
    for x in msg.split(" "):
        c = int(x)
        # Según la fórmula: M = C^d mod n
        result = c**key[1] % key[0]
        msgChars.append(chr(result))
    return "".join(msgChars)

# Código Central
def obtenerClaves():
    p = int(input('Ingrese el valor de P: '))
    while not isPrime(p):
        p = int(input('Ingrese un valor válido para P: '))
    q = int(input('Ingrese el valor de Q, que sea distinto de P: '))
    while not isPrime(q) or q == p:
        q = int(input('Ingrese un valor válido para Q, que sea distinto de P: '))
    n = p * q
    fi = (p - 1) * (q - 1)
    e = int(input(f'Ingrese el valor de E, que sea primo menor que {n}: '))
    while not isPrime(e) or e == p or e == q or e > fi:
        e = int(
            input(f'Ingrese un valor válido para E, que sea primo menor que {n}: '))
    d = 1
    while (d * e) % fi != 1:
        d += 1

    publica = [n, e]
    privada = [n, d]
    return [privada, publica]
    # print(f'La clave pública es: {e} | {publica}')
    # print(f'La clave privada es: {d} | {privada}')

def preguntarOpcion(firstTime: bool = False):
    if (firstTime):
        print('¿Qué desea hacer?')
    else:
        input('Presione enter para continuar...')
    system("cls")
    print("""Opciones:
   1. Generar claves
   2. Cifrar mensaje
   3. Descifrar mensaje
   4. Salir
    """)
    choice = int(input('opcion -> '))
    return choice

choice = preguntarOpcion(True)
while choice != 4:
    if choice == 1:
        system("cls")
        print("""Considere el siguiente ejemplo:
    |----------------------|
    | P: 61 | Q: 53 |E: 17 |
    |----------------------|
        """)
        claves = obtenerClaves()
        print(f'La clave pública es: {claves[1]}')
        print(f'La clave privada es: {claves[0]}')
        choice = preguntarOpcion()
    elif choice == 2:
        system("cls")
        print('Cifrar mensaje')
        claves = input('Ingrese las claves separadas por coma: ').split(',')
        claves = [int(x) for x in claves]
        mensaje = input('Ingrese el mensaje a cifrar: ')
        print('Mensaje Cifrado: ')
        print(f' -> {cifrar(mensaje, claves)}')
        choice = preguntarOpcion()
    elif choice == 3:
        system("cls")
        print('Descifrar mensaje')
        claves = input('Ingrese las claves separadas por coma: ').split(',')
        claves = [int(x) for x in claves]
        mensaje = input('Ingrese el mensaje a descifrar: ')
        print('Mensaje Descifrado: ')
        print(f' -> {descifrar(mensaje, claves)}')
        choice = preguntarOpcion()
    elif choice == 4:
        print('Saliendo...')
        system("cls")
        break
    else:
        system("cls")
        choice = preguntarOpcion()
