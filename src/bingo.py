#generar carton
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
