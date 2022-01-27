from optparse import Values
from Libraries import Functions
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt

#Inicializa um Objeto Tk
app = Tk()

#Class da aplicação
class Aplicação():
    def __init__(self):
        self.app = app
        self.tela()
        self.frame_tela()
        self.label()
        self.widgets()
        self.treeview()
        #Loop
        app.mainloop()
    
    #Configurações da Janela
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

        label_porcentagem = Label(self.frame, text = 'Porcentagem de Capital:', font = ('Times', 12))
        label_porcentagem.place(relx = 0.077, rely = 0.58, relwidth = 0.2, relheight = 0.026)

        label_dados = Label(self.frame, text = 'Carteiras Anteriores:', font = ('Times', 12, 'bold'))
        label_dados.place(relx = 0.075, rely = 0.65, relwidth = 0.2, relheight = 0.026)


    def widgets(self):
        entry_1 = Entry()
        entry_1.place(relx = 0.1, rely = 0.115, relwidth = 0.2, relheight = 0.021)

        entry_2 = Entry()
        entry_2.place(relx = 0.1, rely = 0.173, relwidth = 0.1, relheight = 0.021)

        entry_3 = Entry()
        entry_3.place(relx = 0.1, rely = 0.546, relwidth = 0.1, relheight = 0.021)

        entry_4 = Entry()
        entry_4.place(relx = 0.1, rely = 0.609, relwidth = 0.05, relheight = 0.021)

    def treeview(self):
        self.lista = ttk.Treeview(self.frame, height = 3, columns = ('col1', 'col2', 'col3'))
        self.lista.heading('#0', text = '')
        self.lista.heading('#1', text = 'Data')
        self.lista.heading('#2', text = 'Nome')
        self.lista.heading('#3', text = 'Cotação R$')

        self.lista.column('#0', width = 1)
        self.lista.column('#1', width = 20)
        self.lista.column('#2', width = 120)
        self.lista.column('#3', width = 50)

        #Adicionar nomes das ações na treeview
        
        self.lista.place(relx = 0.1, rely = 0.253, relwidth = 0.3, relheight = 0.25)

        self.scrol_lista = Scrollbar(self.frame, orient = 'vertical')
        self.lista.configure(yscroll=self.scrol_lista.set)
        self.scrol_lista.place(relx = 0.4, rely = 0.253, relwidth = 0.03, relheight = 0.25)

        self.carteiras = ttk.Treeview(self.frame)
        self.carteiras.place(relx = 0.1, rely = 0.68, relwidth = 0.3, relheight = 0.25)

Aplicação()