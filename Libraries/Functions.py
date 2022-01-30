from pandas_datareader import data as web
import yfinance as yf
import pandas as pd

#Recolhe os nomes da ações de um csv, afim de realizar busca.
#OBS: Esse arquivo.csv pode ser encontrado no site da B3, 
#procurei uma forma de atualizar a cada vez que aplicação fosse executada, 
#porem não encontrei formas
#site: https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br
def lista(funcao):
    indice = []
    cotacao = []

    with open('Files/IBOV.csv', 'r') as arquivo:
        for linha in arquivo:
            pos = linha.index(';')+1
            acao = linha[0:pos-1] + '.SA'
            indice.append(acao)

    if funcao == True:
        for linha in indice:
            valor = yf.download(linha, period="1d")["Adj Close"]
            valor = '{:.2f}'.format(valor.iloc[0])
            cotacao.append(valor)
        
        indice_cotacao = list(zip(indice, cotacao))

        tabela = pd.DataFrame(indice_cotacao, columns = ['Indice', 'Cotação'])

        return tabela
    
    else:
        tamanho = len(indice)
        return tamanho