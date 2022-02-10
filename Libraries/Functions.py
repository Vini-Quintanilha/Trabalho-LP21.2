import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf

# ------------------------- Tratamento de dados ------------------------- #

# True --> Retorna uma tabela(datadrame) com os índices e as devidas cotações
# False --> Retorna a tamanho da lista de índices

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

# ---------------------------- Gráfico Ibov ----------------------------- #

def grafico_ibov():
   ibov = web.get_data_yahoo('^BVSP')
   ibov = ibov[(ibov.index.year >= 2020)]
   plt.title(' TÍTULO ')
   x = ibov["Close"].plot(figsize=(22,8), label="IBOV",linewidth=3.0)
   plt.ylabel('Valorização')
   plt.xlabel('Ano')
   plt.legend(loc='best')

# ----------------------------- carteira -------------------------------- #

def carteira(tickers):
   for i in range(len(tickers)):
      tickers[i] = tickers[i] + '.SA'
   carteira = yf.download(tickers, period="10y")["Adj Close"]
   return carteira

# ------------------------ carteira Valorização ------------------------- #

def carteira_valorização(indice):

   carteira = yf.download(indice, period="10y")["Adj Close"]
   valorização = carteira / carteira.iloc[0]
   
   valorização.plot()
   plt.show()

# -------------------------------- ibov --------------------------------- #

def ibov():
   ibov = yf.download("^BVSP", period="10y")["Adj Close"]
   return ibov

# -------------------------- ibov Valorização --------------------------- #

def ibov_valorização():
   ibov = yf.download("^BVSP", period="10y")["Adj Close"]
   ibov_valorização = ibov / ibov.iloc[0]
   return ibov_valorização

# ------------------------------- saldo --------------------------------- #

def saldo(Valor_investido,tickers,porcentagem,valorização):
 
   for i in range(len(porcentagem)):
      porcentagem[i] = porcentagem[i] / 100

   for i in range(len(tickers)):
      acao = tickers[i]
      multiplicador = porcentagem[i] * Valor_investido
      valorização[acao] = valorização[acao].mul(multiplicador) 
      valorização["saldo"] = valorização.sum(axis=1)
   return valorização["saldo"]

# -----------------------   Valorização Ativo --------------------------- #

def valorização_por_ativo():
  carteira_valorização = (carteira / carteira.iloc[0])
  x = carteira_valorização.plot(figsize=(18,8),label="Carteira",linewidth=3.0,xlabel = 'Data',title = "Carteira")
  return(x)