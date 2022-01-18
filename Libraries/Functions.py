from tracemalloc import start
from numpy import source
from pandas_datareader import data as web
from datetime import datetime

#Recolhe os nomes da ações de um txt, afim de realizar busca.
def Lista_Acoes():
    lista = []

    with open('Files/IBOV.csv', 'r') as arquivo:
        for linha in arquivo:
            lista.append(linha)
        arquivo.close()

    return lista

#Verifica se a ação desejada consta na lista, caso conste será retornado
#o nome da ação que consta na B3, caso contrário será retornado false
def Busca_Acao(lista, nome):
    for linha in lista:
        if nome in linha:
            linha = str(linha)
            pos = linha.index(';')+1
            acao = linha[0:pos-1]
            return acao
    return 0

#Obtem valor de uma ação
def Valor_Acao():
    pass

nome = 'azul'
print(Busca_Acao(Lista_Acoes(), nome.upper()))