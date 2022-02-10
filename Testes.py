from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Libraries import Functions

#Inicializa um Objeto Tk
#menu = Tk()

#Alterar tamanho da janela e posição de onde vai aparecer
#menu.geometry("500x250+250+250")
#Codigo aqui
#---->
def teste(indice):

    Carteira = Functions.carteira_valorização(indice)
    Carteira.plot(figsize=(18,8));
    plt.legend();
"""def teste():
    acoes = ["ABEV3.SA","ITSA4.SA","WEGE3.SA","USIM5.SA","VALE3.SA"]
    figura2 = Figure(figsize = (8, 4), dpi = 60)
    ax2 = figura2.add_subplot(111)
    Carteira = Functions.carteira_valorização(acoes)
    ax2.plot(Carteira,figsize=(18,8),labels = acoes)
    ax2.set_title('{}'.format("vini"))

    canvas2 = FigureCanvasTkAgg(figura2,  master = "50x50")
    canvas2.get_tk_widget().place(relx = 0.1, rely = 0.59, relwidth = 0.3, relheight = 0.3)"""

'''      #Grafico 3
        figura3 = Figure(figsize = (8, 4), dpi = 60)
        ax3 = figura3.add_subplot(111)
        capital = 
        indice = 
        porcentagem = 
        Carteira=
        acumulado = Functions.saldo(capital,indice,porcentagem,Carteira)
        ibov_notempo = Functions.ibov_valorização()
        ax3.plot(acumulado,ibov_notempo,figsize=(18,8),labels = indice)
        ax3.set_title('{}'.format(self.nome))

        canvas3 = FigureCanvasTkAgg(figura3, self.frame)
        canvas3.get_tk_widget().place(relx = 0.4, rely = 0.68, relwidth = 0.3, relheight = 0.3)'''

teste(["ABEV3.SA","ITSA4.SA","WEGE3.SA","USIM5.SA","VALE3.SA"])
#menu.mainloop()