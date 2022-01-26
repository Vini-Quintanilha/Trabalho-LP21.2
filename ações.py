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


"""Valor = float(input("Quanto deseja investir?"))

def ativos():
   contador = 0
   acoes = []
            "precisa fazer uma conta para n bater mais de 100% aqui e se a conta der 100% ir para a prox função"

   while contador != 1:
      if contador < 1:

         acoes[0] += input("Qual ação deseja investir?")
         #conectar com a fução busca_Acao
         append.acoes[1](float(input("Quantos por cento da carteira você gostaria de investir nessa ação?(Responda apenas com números)")))

         contador += (float(input("Quantos por cento da carteira você gostaria de investir nessa ação?(Responda apenas com números)"))

         tickers = acoes[0]

         carteira = yf.download(tickers, period="10y")["Adj Close"]

         ibov = yf.download("^BVSP", period="10y")["Adj Close"]

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