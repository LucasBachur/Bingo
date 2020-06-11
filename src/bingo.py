#generar carton
#0 representas celdas vacias en el carton
#1 representan celdas ocupadas en el carton
def carton():
    carton = (
            (1,0,0,1,1,0,1,0,1),
            (0,1,1,1,0,1,1,1,1),
            (0,1,0,0,1,0,0,1,0)
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

def validar_quince_numeros(carton):
    contador = 0
    for fila in carton:
        for celda in fila:
            if celda != 0 :
                contador = contador + 1
    return contador == 15

print (columna(carton(),1))
