#generar carton
#0 representas celdas vacias en el carton
#1 representan celdas ocupadas en el carton
def carton():
    carton = (
            (90,0,0,11,25,0,54,0,76),
            (0,15,24,15,0,47,86,52,53),
            (0,44,0,0,67,0,0,76,0)
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
#Nonumeros repetidos
def numerosrep(carton):
    contador =0
    for fila in range(0,3):
        for columna in range(0,9):
            
#Columna numeros menores arriba de mayores

#columnas izq derec
print (columna(carton(),1))
