from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Libraries import Functions
from ações import *

#Inicializa um Objeto Tk
app = Tk()

#Class da aplicação
class Aplicação():
    def __init__(self):
        self.app = app
        self.indice = []
        self.porcentagem = []
        self.nome = []
        self.capital = []
        self.porcentagem_restante = 100

        self.tela()
        self.frame_tela()
        self.label()
        self.widgets()
        self.treeview()
        self.button()
        self.graficos(self.indice, self.porcentagem)

        #Loop
        app.mainloop()

    # --------------> Configurações da Janela <-------------- #
    def tela(self):
        #Dimensões do screen
        self.largura_screen = app.winfo_screenwidth()
        self.altura_screen = app.winfo_screenheight()

        #Dimensões da janela
        self.largura = int(self.largura_screen - self.largura_screen * 0.3)
        self.altura = int(self.altura_screen - self.altura_screen * 0.1)

        #Posicionamento da janela no screen
        self.posx = int((self.largura_screen / 2) - (self.largura / 2))
        self.posy = int((self.altura_screen / 2) - (self.altura / 1.8))

        #Muda o icone da janela
        #self.app.iconbitmap("caminho/arquivo.ico")

        #Defini o tamanho da janela
        self.app.geometry('{}x{}+{}+{}'.format(self.largura, self.altura, self.posx, self.posy))

        #Trava o redimensionamento da janela
        self.app.resizable(False, False)

    # --------------> Parte Visual <-------------- #
    def frame_tela(self):
        self.frame = Frame(self.app)
        self.frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    def label(self):
        label_titulo = Label(self.frame, text = 'Cadastro de Carteira', font = ('Times', 14, 'italic'))
        label_titulo.place(relx = 0.4, rely = 0, relwidth = 0.2, relheight = 0.1)

        label_nome = Label(self.frame, text = 'Nome:', font = ('Times', 12))
        label_nome.place(relx = 0.096, rely = 0.09, relwidth = 0.05, relheight = 0.02)

        label_valor = Label(self.frame, text = 'Valor do Investimento R$:', font = ('Times', 12))
        label_valor.place(relx = 0.0837, rely = 0.15, relwidth = 0.2, relheight = 0.02)

        label_cotacao = Label(self.frame, text = 'Cotações Ibovespa:', font = ('Times', 12, 'bold'))
        label_cotacao.place(relx = 0.07, rely = 0.22, relwidth = 0.2, relheight = 0.024)

        label_acao = Label(self.frame, text = 'Digite uma Ação:', font = ('Times', 12))
        label_acao.place(relx = 0.054, rely = 0.515, relwidth = 0.2, relheight = 0.026)

        label_acao = Label(self.frame, text = 'Capital Disponível:', font = ('Times', 12))
        label_acao.place(relx = 0.22, rely = 0.515, relwidth = 0.2, relheight = 0.026)        

        label_porcentagem = Label(self.frame, text = 'Porcentagem de Capital:', font = ('Times', 12))
        label_porcentagem.place(relx = 0.077, rely = 0.58, relwidth = 0.2, relheight = 0.026)

        label_dados = Label(self.frame, text = 'Ações da Carteira', font = ('Times', 12, 'bold'))
        label_dados.place(relx = 0.065, rely = 0.65, relwidth = 0.2, relheight = 0.026)

        label_acao = Label(self.frame, text = '{}%'.format(self.porcentagem_restante), font = ('Times', 12))
        label_acao.place(relx = 0.22, rely = 0.545, relwidth = 0.2, relheight = 0.026)         

    def widgets(self):
        self.entry_1 = Entry()
        self.entry_1.place(relx = 0.1, rely = 0.115, relwidth = 0.2, relheight = 0.021)

        self.entry_2 = Entry()
        self.entry_2.place(relx = 0.1, rely = 0.173, relwidth = 0.1, relheight = 0.021)

        self.entry_3 = Entry()
        self.entry_3.place(relx = 0.1, rely = 0.546, relwidth = 0.1, relheight = 0.021)

        self.entry_4 = Entry()
        self.entry_4.place(relx = 0.1, rely = 0.609, relwidth = 0.05, relheight = 0.021)

    def treeview(self):
        self.lista = ttk.Treeview(self.frame, height = 3, columns = ('col1', 'col2'))
        self.lista.heading('#0', text = '')
        self.lista.heading('#1', text = 'Índice')
        self.lista.heading('#2', text = 'Cotação R$')

        self.lista.column('#0', width = 1)
        self.lista.column('#1', width = 120)
        self.lista.column('#2', width = 80)
        
        tabela = Functions.lista(True)
        tamanho = Functions.lista(False)

        for x in range(tamanho):
            treeview = []
            treeview.append(tabela['Indice'].iloc[x])
            treeview.append(tabela['Cotação'].iloc[x])

            self.lista.insert('', END, values = treeview)      

        self.lista.place(relx = 0.1, rely = 0.253, relwidth = 0.3, relheight = 0.25)

        self.scrol_lista = Scrollbar(self.frame, orient = 'vertical')
        self.lista.configure(yscroll=self.scrol_lista.set)
        self.scrol_lista.place(relx = 0.4, rely = 0.253, relwidth = 0.03, relheight = 0.25)
    
    def graficos(self, indice, porcentagem):
        #Gráfico 1
        figura = Figure(figsize = (8, 4), dpi = 60)
        ax1 = figura.add_subplot(111)

        ax1.pie(porcentagem, labels = indice, autopct='%1.1f%%',
        shadow=True, startangle=90)

        ax1.set_title('{}'.format(self.nome))
        ax1.axis('equal')

        canvas = FigureCanvasTkAgg(figura, self.frame)
        canvas.get_tk_widget().place(relx = 0.1, rely = 0.68, relwidth = 0.3, relheight = 0.3)

        #Grafico 2
        
        figura2 = Figure(figsize = (8, 4), dpi = 60)
        ax2 = figura2.add_subplot(111)
        Carteira = carteira_valorização(indice)
        ax2.plot(Carteira,figsize=(18,8),labels = indice)
        ax2.set_title('{}'.format(self.nome))

        canvas2 = FigureCanvasTkAgg(figura2, self.frame)
        canvas2.get_tk_widget().place(relx = 0.1, rely = 0.68, relwidth = 0.3, relheight = 0.3)

        #Grafico 3
        
        figura3 = Figure(figsize = (8, 4), dpi = 60)
        ax3 = figura3.add_subplot(111)
        acumulado = saldo(self.capital,indice,porcentagem,Carteira)
        ibov_notempo = ibov_valorização()
        ax3.plot(acumulado,ibov_notempo,figsize=(18,8),labels = indice)
        ax3.set_title('{}'.format(self.nome))

        canvas3 = FigureCanvasTkAgg(figura3, self.frame)
        canvas3.get_tk_widget().place(relx = 0.1, rely = 0.68, relwidth = 0.3, relheight = 0.3)

    def button(self):
        button_1 = Button(self.frame, text = 'Enviar', command = self.button_function_1)
        button_1.place(relx = 0.35, rely = 0.154, relwidth = 0.05, relheight = 0.04)
        
        button_2 = Button(self.frame, text = 'Enviar', command = self.button_function_2)
        button_2.place(relx = 0.35, rely = 0.59, relwidth = 0.05, relheight = 0.04)
    
    # --------------> Funções <-------------- #
    def button_function_1(self):
        self.nome.append(self.entry_1.get())
        self.capital.append(self.entry_2.get())

    def button_function_2(self):
        if self.porcentagem_restante != 0:
            self.indice.append(self.entry_3.get())
            self.porcentagem.append(self.entry_4.get())

            self.entry_3.delete(0, END)
            self.entry_4.delete(0, END)

            self.graficos(self.indice, self.porcentagem)
            self.porcentagem_()

        label_acao = Label(self.frame, text = '{}%'.format(self.porcentagem_restante), font = ('Times', 12))
        label_acao.place(relx = 0.22, rely = 0.545, relwidth = 0.2, relheight = 0.026) 

    def porcentagem_(self):
        pos = len(self.porcentagem)
        porcentagem = int(self.porcentagem[pos - 1])
        self.porcentagem_restante = self.porcentagem_restante - porcentagem

Aplicação()