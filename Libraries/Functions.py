import os

#Recolhe os nomes da ações de um txt, afim de realizar busca.
def Lista_Acoes():
    lista = []

    with open('Files/Actions.txt', 'r') as arquivo:
        for linha in arquivo:
            lista.append(linha)
        arquivo.close()

    return lista

#Verifica se a ação desejada consta na lista
def Busca_Acao(lista, nome):
    pass