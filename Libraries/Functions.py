from numpy import source
from pandas_datareader import data as web
from datetime import datetime, timedelta

#Recolhe os nomes da ações de um csv, afim de realizar busca.
#OBS: Esse arquivo.csv pode ser encontrado no site da B3, 
#procurei uma forma de atualizar a cada vez que aplicação fosse executada, 
#porem não encontrei formas
#site: https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br
def Lista_Acoes():
    lista = []

    with open('Files/IBOV.csv', 'r') as arquivo:
        for linha in arquivo:
            lista.append(linha)
        arquivo.close()

    return lista

#Verifica se a ação desejada consta na lista, caso conste será retornado
#o nome da ação que consta na B3, caso contrário será retornado false
"colocar um aviso ou uma opção de inserir novamente"
def Busca_Acao(lista, nome):
    for linha in lista:
        if nome in linha:
            linha = str(linha)
            pos = linha.index(';')+1
            acao = linha[0:pos-1]
            return acao
    return 0

#Obtem o valor do dia atual e uma tabela com os ultimos 5 dias (fora finais de semana).
# --> True para obter apenas o valor da ação no presente momento
# --> False para obter uma tabela de valores dos ultimos 5 dias para análise e gráficos
def Tabela_acao(acao, funcao):
    acao = acao + '.SA'
    dias = -4

    data_atual = datetime.today().strftime('%m-%d-%y')
    data_final = datetime.today() + timedelta(days=dias)
    data_final = data_final.strftime('%m-%d-%y')

    tabela = web.DataReader(acao, data_source='yahoo', start=data_final, end=data_atual)
    
    if funcao == True:
        valor = '{:.2f}'.format(tabela['Close'].iloc[len(tabela) - 1])
        return valor
    else:
        return tabela

