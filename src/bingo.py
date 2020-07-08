import random
import math
#Funcion mostrar columna
def columna(carton,nro_columna):
    return(
        carton[0][nro_columna],
        carton[1][nro_columna],
        carton[2][nro_columna],
    )
#Si el carton tiene quince numeros ocupados
def validar_quince_numeros(carton):
    contador = 0
    for fila in carton:
        for celda in fila:
            if celda != 0 :
                contador = contador + 1
    return contador == 15
#Funcion el carton numeros entre 1 y 90 celdas ocupadas
def numeros1a90(carton):
    contador = 0
    revelador= True
    for fila in range(0,3):
        for columna in range(0,9):
            celda=carton[fila][columna]
            if (celda >= 0 and celda <=90):
                contador=contador+1#no afecta en nada esto pero cuando tenga ganas hago mejor la funcion
            else:
                revelador=False

    return revelador
#columnas izq derec
def colmizqder(carton):
    revelador=True
    for fila in range(0,3):
        for columna in (range(0,9)):
            if(carton[fila][columna]!=0):
                for j in (range(columna+1,9)):
                    if(carton[0][j]!=0):
                        if(carton[fila][columna]>carton[0][j]):
                            revelador=False
                    if(carton[1][j]!=0):
                        if(carton[fila][columna]>carton[1][j]):
                            revelador=False
                    if(carton[2][j]!=0):
                        if(carton[fila][columna]>carton[2][j]):
                            revelador=False


    return revelador
#Nonumeros repetidos
def numerosrep(carton):
    contador =0
    for fila in range(0,3):
        for columna in range(0,9):
            if(carton[fila][columna]!=0):
                for i in range(0,3):
                    for j in range(0,9):
                        if(carton[fila][columna]==carton[i][j]and (fila,columna)!=(i,j)):
                            contador =1
    return contador
#Columna numeros menores arriba de mayores
def arribamyor(carton):
    contador=0
    for fila in range(0,3):
        for columna in (range(0,9)):
            if(carton[fila][columna]!=0):
                if(fila==0):
                    if(carton[fila][columna]>carton[1][columna] and carton[1][columna]!=0):
                        contador=1
                    if(carton[fila][columna]>carton[2][columna] and carton[2][columna]!=0):
                        contador=1
                if(fila==1):
                    if(carton[fila][columna]<carton[0][columna] and carton[0][columna]!=0):
                        contador=1
                    if(carton[fila][columna]>carton[2][columna] and carton[2][columna]!=0):
                        contador=1
                if(fila==2):
                    if(carton[fila][columna]<carton[1][columna] and carton[1][columna]!=0):
                        contador=1
                    if(carton[fila][columna]<carton[2][columna] and carton[2][columna]!=0):
                        contador=1
    return contador
# 5 celdas ocupadas x fila
def fila_cincoocupa(carton):
    for fila in carton:
        contador = 0
        for celda in fila:
            if  (celda!=0):
                contador += 1
        if (contador != 5):
            return False
    return True

# 3 columnas una celda ocupada
def trescolumnas(carton):
    aux=0
    for celda in range(0,9):
        contador=0
        for fila in range(0,3):
            if(carton[fila][celda]!=0):
                contador += 1
        if(contador==1):
            aux += 1
    if(aux!=3):
        return False
    return True
# 2 celdas consecutivas vacias
def dosceldasvacias(carton):
    for celda in range(0,7):
        for fila in range(0,3):
            if(carton[fila][celda]==0 and carton[fila][celda+1]==0 and carton[fila][celda+2]==0):
                return False
    return True
# 2 celdas consecutivas ocupadas

# 2 celdas consecutivas vacias
def dosceldasocupadas(carton):
    for celda in range(0,7):
        for fila in range(0,3):
            if(carton[fila][celda]!=0 and carton[fila][celda+1]!=0 and carton[fila][celda+2]!=0):
                return False
    return True
# columnas llenas
def columnasllenas(carton):
    contador=0
    for celda in range(9):
        for fila in range(3):
            if(carton[fila][celda]!=0):
                contador += 1
        if(contador==3):
            return False
        contador=0
    return True
# filas vacias
def filasvacias(carton):
    contador = 0
    for fila in carton:
        for celda in fila:
             contador = contador + celda
        if(contador==0):
            return False
        else :
            contador=0
    return True
#columnas vacias
def columnasvacias(carton):
    contador=0
    for celda in range(9):
        for fila in range(3):
            if(carton[fila][celda]==0):
                contador += 1
        if(contador==3):
            return False
        contador=0
    return True

def intentoCarton():
    contador = 0

    carton = [
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0]
    ]
    numerosCarton = 0

    while (numerosCarton < 15):
      contador = contador + 1
      if (contador==50):
        return intentoCarton()

      numero=random.randint(1, 90)

      columna = math.floor (numero / 10)
      if (columna==9):
        columna=8

      huecos=0

      for i in range (3):
        if (carton[i][columna] == 0):
          huecos=huecos + 1

        if (carton[i][columna]==numero):
          huecos=0
          break
      if (huecos<2):
        continue

      fila = 0
      for j in range(3):
        huecos = 0
        for i in range(9):
          if (carton[fila][i] == 0):
            huecos = huecos + 1

        if (huecos < 5 or carton[fila][columna] != 0):
          fila = fila + 1
        else:
          break

      if (fila == 3):
        continue

      carton[fila][columna] = numero
      numerosCarton = numerosCarton + 1
      contador = 0

    for x in range(9):
      huecos = 0
      for y in range(3):
        if (carton[y][x] == 0):
          huecos = huecos + 1
      if (huecos == 3):
        return intentoCarton()

    return carton
#funcion generar carton
def generar_carton():
  while True:
      carton = intentoCarton()
      if(validar_quince_numeros(carton)
      and fila_cincoocupa(carton)
      and columnasvacias(carton)
      and filasvacias(carton)
      and numeros1a90(carton)
      and colmizqder(carton)
      and arribamyor(carton)==0
      and numerosrep(carton)==0
      and columnasllenas(carton)
      and dosceldasvacias(carton)
      and dosceldasocupadas(carton)
      and trescolumnas(carton)):
          break
  return carton

carton=generar_carton()

for fila in carton:
    print(fila)
