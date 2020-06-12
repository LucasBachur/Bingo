#generar carton
#0 representas celdas vacias en el carton
#1 representan celdas ocupadas en el carton
def carton():
    carton = (
            (7, 0 ,  0   ,31 , 55 , 0 , 72 ,81 ,90),
            (0, 11 , 24 , 34 , 0 ,  68 ,75 ,86 ,0),
            (0, 13 , 0 ,  0 ,  58 , 0 , 0 , 89 ,0)
    )
    return carton
#Funcion contar celdas
def contar_celdas_ocupadas():
    mi_carton= carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
             contador = contador + celda
    return contador
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
print (columna(carton(),1))
