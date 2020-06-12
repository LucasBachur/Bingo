from src.bingo import carton
from src.bingo import validar_quince_numeros
from src.bingo import numeros1a90
from src.bingo import colmizqder
from src.bingo import arribamyor


#verificar que existan 15 numeros
def test_15celdasocupadas():
    mi_carton= carton()
    assert validar_quince_numeros(mi_carton)==True

#verifica que no tenga menos de 15 celdas ocupadas
def test_menor15():
    mi_carton= carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
             contador = contador + 1

    assert contador>=15

#verifica que no tenga mas de 15 celdas ocupadas
def test_mayor15():
    mi_carton= carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
             contador = contador + 1

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
#Test numeros 1  a 90 en celdas
def test_numeros1a90():
    mi_carton=carton()
    assert numeros1a90(mi_carton)==True
#Test Columnas izq derec
def test_colizqder():
    mi_carton=carton()
    assert colmizqder(mi_carton)==True

#Test no numeros repetidos

#Test Columna numeros menores arriba de mayores
def test_arribamy():
    mi_carton=carton()
    assert arribamyor(mi_carton)==0
