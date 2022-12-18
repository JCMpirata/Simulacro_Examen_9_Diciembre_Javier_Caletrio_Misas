def movimiento(jugador, tabla):
    mover = True
    while mover:    
        c = int(input("Elige una columna (Introduce un número entero): ", 0, len(tabla)-1))
        f = int(input("Elige la posicion de la torre (Introduce un número entero negativo para arriba y otro numero entero positivo hacia abajo): ", -(len(tabla)), len(tabla)))
        if f >=0:
            signo = 1
        else:
            signo = -1
        posiciono = tabla[c].index(jugador)
        posicion = tabla[c].index(jugador)

    for i in range(signo, f+signo, signo):
            if f < 0:
                posicion = posicion -1
                mover = False
            elif f > 0:
                posicion = posicion +1
                mover = False
            else:
                pass

    if (posiciono + f < 0 or posiciono + f > len(tabla)-1) or tabla[c][posicion] != 0:
                print("no puedes mover la torre a esa posicion")
                mover = True
                break
    
    tabla[c][posiciono] = 0
    tabla[c][posicion] = jugador
    return tabla

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])



    