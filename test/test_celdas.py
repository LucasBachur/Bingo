from src.bingo import carton
from src.bingo import validar_quince_numeros
from src.bingo import numeros1a90
from src.bingo import colmizqder
from src.bingo import arribamyor
from src.bingo import numerosrep
from src.bingo import fila_cincoocupa
from src.bingo import trescolumnas
from src.bingo import dosceldasvacias
from src.bingo import dosceldasocupadas
from src.bingo import columnasllenas
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
def test_numerosrep():
    mi_carton=carton()
    assert numerosrep(mi_carton)==0
#Test Columna numeros menores arriba de mayores
def test_arribamy():
    mi_carton=carton()
    assert arribamyor(mi_carton)==0
#Test 5 celdas ocupadas x fila
def test_cincoceldaocupa():
    mi_carton=carton()
    assert fila_cincoocupa(mi_carton)==True
#Test 3 columnas ocupadas 1 celdas
def test_3colum():
    mi_carton=carton()
    assert trescolumnas(mi_carton)==True

#Test 2 celdas vacias consecutivas
def test_2celdasva():
    mi_carton=carton()
    assert dosceldasvacias(mi_carton)==True
#Test 2 celdas ocupadas consecutivas
def test_2celdasocupas():
    mi_carton=carton()
    assert dosceldasocupadas(mi_carton)==True
#Test columnas llenas
def test_columnasllenas():
    mi_carton=carton()
    assert columnasllenas(mi_carton)==True
