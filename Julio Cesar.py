def charToAscii(M):
    return [ord(i) for i in M]

def asciiToChar(s):
    return ''.join(s)

def cifrarMensaje(M):
    X = charToAscii(M)
    JC = JCL = []
    for x in X:
        JC.append(x + 3)
        JCL.append(chr(JC[x] % 255))
    return asciiToChar(JCL)

def descifrarMensaje(M):
    Y = charToAscii(M)
    DJC = DJCL = []
    for y in Y:
        DJC.append(y - 3)
        DJCL.append(chr(DJC[y] % 255))
    return asciiToChar(DJCL)

# Código Principal #
mensaje_a_cifrar = input('Ingrese el mensaje a cifrar: ')
mensaje_cifrado = cifrarMensaje(mensaje_a_cifrar)
print('Mensaje Cifrado: ', mensaje_cifrado)
input('Presione una tecla para descifrar el mensaje...')
mensaje_descifrado = descifrarMensaje(mensaje_cifrado)
print('Mensaje Descifrado: ', mensaje_descifrado)
