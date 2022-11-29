def letraAAscii(M):
    L=len(M)
    N = [None]*L
    for i in range(0,L,1):
        N[i] = ord(M[i])
    return N

def asciiALetra(s):
    n = ""
    for x in s:
        n += x
    return n

def cifrarMensaje(M):
    X = letraAAscii(M)
    JC = [None]*len(X)
    JCL = [None]*len(X)

    for i in range(0, len(X), 1):
        JC[i] = X[i] + 3
        JCL[i] = chr(JC[i] % 255)
    return asciiALetra(JCL)

def descifrarMensaje(M):
    Y = letraAAscii(M)
    DJC = [None] * len(Y)
    DJCL = [None] * len(Y)

    for i in range(0, len(Y), 1):
        DJC[i] = Y[i] - 3
        DJCL[i] = chr(DJC[i] % 255)
    return asciiALetra(DJCL)

# Código Principal #
mensaje_a_cifrar = input('Ingrese el mensaje a cifrar: ')
mensaje_cifrado = cifrarMensaje(mensaje_a_cifrar)
print('Mensaje Cifrado: ', mensaje_cifrado)
input('Presione una tecla para descifrar el mensaje...')
mensaje_descifrado = descifrarMensaje(mensaje_cifrado)
print('Mensaje Descifrado: ', mensaje_descifrado)
