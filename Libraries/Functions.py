from numpy import source
from pandas_datareader import data as web
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import yfinance as yf

#Recolhe os nomes da ações de um csv, afim de realizar busca.
#OBS: Esse arquivo.csv pode ser encontrado no site da B3, 
#procurei uma forma de atualizar a cada vez que aplicação fosse executada, 
#porem não encontrei formas
#site: https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br
def lista():
    lista = []

    with open('Files/IBOV.csv', 'r') as arquivo:
        for linha in arquivo:
            pos = linha.index(';')+1
            acao = linha[0:pos-1]
            lista.append(acao)
        arquivo.close()

    return lista

#Verifica se a ação desejada consta na lista, caso conste será retornado
#o nome da ação que consta na B3, caso contrário será retornado false
def busca_Acao(lista, nome):
    for linha in lista:
        if nome in linha:
            linha = str(linha)
            pos = linha.index(';')+1
            acao = linha[0:pos-1]
            return acao
    return 0
    #Erro, caso o utilizador digite a ação errada será retornado um valor 0, onde será
    #tratado na interface do tkinter

#Obtem o valor do dia atual e uma tabela com os ultimos 5 dias (fora finais de semana).
# --> True para obter apenas o valor da ação no presente momento
# --> False para obter uma tabela de valores dos ultimos 5 dias para análise e gráficos
def tabela_acao(acao, funcao):
    acao = acao + '.SA'

    if funcao == True:
        data_atual = datetime.today().strftime('%m-%d-%y')
        valor = web.DataReader(acao, data_source='yahoo', start=data_atual)
        valor = '{:.2f}'.format(valor['Adj Close'].iloc[0])
        return valor
    else:
        tabela = yf.download(acao, period="5d")["Adj Close"]
        return tabela

def ibovespa():
    ibov = yf.download('^BVSP', period="7d")["Adj Close"]
    return ibov

lista()