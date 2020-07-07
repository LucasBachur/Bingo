from src.bingo import generar_carton
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
from src.bingo import filasvacias
from src.bingo import columnasvacias
mi_carton= generar_carton()
#verificar que existan 15 numeros
def test_15celdasocupadas():
    assert validar_quince_numeros(mi_carton)==True

#verifica que no tenga menos de 15 celdas ocupadas
def test_menor15():
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
             contador = contador + 1

    assert contador>=15

#verifica que no tenga mas de 15 celdas ocupadas
def test_mayor15():
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
             contador = contador + 1

    assert contador<=15

#Funcion mostrar columnas ocupadas
def test_columansocupadas():
    revelador = True
    for columna in range(9):
        if(mi_carton[0][columna]== 0 and mi_carton[1][columna]== 0 and mi_carton[2][columna]==0):
            revelador=False
    assert revelador == True
#Test numeros 1  a 90 en celdas
def test_numeros1a90():
    assert numeros1a90(mi_carton)==True
#Test Columnas izq derec
def test_colizqder():
    assert colmizqder(mi_carton)==True

#Test no numeros repetidos
def test_numerosrep():
    assert numerosrep(mi_carton)==0
#Test Columna numeros menores arriba de mayores
def test_arribamy():
    assert arribamyor(mi_carton)==0
#Test 5 celdas ocupadas x fila
def test_cincoceldaocupa():
    assert fila_cincoocupa(mi_carton)==True
#Test 3 columnas ocupadas 1 celdas
def test_3colum():
    assert trescolumnas(mi_carton)==True

#Test 2 celdas vacias consecutivas
def test_2celdasva():
    assert dosceldasvacias(mi_carton)==True
#Test 2 celdas ocupadas consecutivas
def test_2celdasocupas():
    assert dosceldasocupadas(mi_carton)==True
#Test columnas llenas
def test_columnasllenas():
    assert columnasllenas(mi_carton)==True
#Test filas vacias
def test_filasvacias():
    assert filasvacias(mi_carton)==True
#Test columnas vacias
assert columnasvacias(mi_carton)==True
