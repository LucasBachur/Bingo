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

print(carton())
