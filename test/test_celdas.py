from src.bingo import carton

#verifica que no tenga menos de 15 celdas ocupadas
def test_menor15():
    mi_carton= carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
             contador = contador + celda

    assert contador>=15

#verifica que no tenga mas de 15 celdas ocupadas
def test_mayor15():
    mi_carton= carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
             contador = contador + celda

    assert contador<=15

#Funcion mostrar columnas ocupadas
def test_columansocupadas():
    mi_carton=carton()
    revelador = True
    for columna in range(9):
        if(mi_carton[0][columna]== 0 and mi_carton[1][columna]== 0 and mi_carton[2][columna]==0):
            revelador=False
    assert revelador == True
#Funcion para testear filas vacias
def test_filasvacias():
    mi_carton=carton()
    revelador= True
    contador = 0
    for fila in mi_carton:
        for celda in fila:
             contador = contador + celda
        if(contador==0):
            revelador=False
        else :
            contador=0
    assert revelador == True
