import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from datetime import datetime, timedelta
import yfinance as yf

def grafico_ibov():
   ibov = web.get_data_yahoo('^BVSP')
   ibov = ibov[(ibov.index.year >= 2020)]
   plt.title(' TÍTULO ')
   x = ibov["Close"].plot(figsize=(22,8), label="IBOV",linewidth=3.0)
   plt.ylabel('Valorização')
   plt.xlabel('Ano')
   plt.legend(loc='best')
   print(x)
grafico_ibov()
 #----------------------------- carteira-------------------------
def carteira(tickers):
   for i in range(len(tickers)):
      tickers[i] = tickers[i] + '.SA'
   carteira = yf.download(tickers, period="10y")["Adj Close"]
   return carteira
   
   #----------------------------- ibov-------------------------
def ibov():
   ibov = yf.download("^BVSP", period="10y")["Adj Close"]
   return ibov


def valorização_por_ativo():
  carteira_valorização = (carteira / carteira.iloc[0])
  x = carteira_valorização.plot(figsize=(18,8),label="Carteira",linewidth=3.0,xlabel = 'Data',title = "Carteira")
  return(x)

def ativos():
   contador = 0
   acoes = []
   lista = lista()
           

   while contador != 100:
      if contador < 100:
        acao = input("Qual ação deseja investir?")
        for linha in lista:
          if acao in linha:
             acao += ".SA"
             append.acoes[0](acao)
            append.acoes[1](float(input("Quantos por cento da carteira você gostaria de investir nessa ação?(Responda apenas com números)")))
            contador += (float(input("Quantos por cento da carteira você gostaria de investir nessa ação?(Responda apenas com números)"))
        break

      else:
        contador = 0
        print("Insira novamente")
        break
         return acoes

def teste():
  Valor_investido = 100000
  acoes = [["ABEV3.SA", "ITSA4.SA","WEGE3.SA", "USIM5.SA", "VALE3.SA"],[0.1,0.2,0.3,0.2,0.2]]
  carteira_valorização = (carteira / carteira.iloc[0])
  for i in range(5):
    acaomuda = acoes[0][i]
    multiplicador = acoes[1][i]
    carteira_valorização[acaomuda] = carteira_valorização[acaomuda].mul(multiplicador) 
  carteira_valorização["saldo"] = carteira_valorização.sum(axis=1)
  ibov_valorização = (ibov / ibov.iloc[0])
  carteira_valorização["saldo"].plot(figsize=(18,8), label="Minha Carteira")
  ibov_valorização.plot(label="IBOV")
  plt.legend();
   print(carteira_valorização)


"""Valor = float(input("Quanto deseja investir?"))
  # tickers = acoes[0]

         #carteira = yf.download(tickers, period="10y")["Adj Close"]

        # ibov = yf.download("^BVSP", period="10y")["Adj Close"]


   dados_yahoo = yf.download(tickers=tickers, period="5y")['Adj Close']
   retorno = dados_yahoo.pct_change()
   retorno_acumulado = (1 + retorno).cumprod()
   retorno_acumulado.iloc[0] = 1
   carteira = Valor * retorno_acumulado.iloc[:, :5]
   carteira["saldo"] = carteira.sum(axis=1)
   carteira["retorno"] = carteira["saldo"].pct_change()
   carteira

#Qual ações deseja investir?
#class ativo:
 # def __init__(self,nome,porcentagem,setor):
    # Salva as variáveis como atributos
  #  self.nome = nome
   # self.porcentagem = porcentagem
    #self.setor = setor"""