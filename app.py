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
        self.lista_acoes()
        #Loop
        app.mainloop()
    
    #Configurações da Janela
    def tela(self):
        #Dimensões da janela
        self.largura = 480
        self.altura = 480

        #Dimensões do screen
        self.largura_screen = app.winfo_screenwidth()
        self.altura_screen = app.winfo_screenheight()

        #Posicionamento da janela no screen
        self.posx = int((self.largura_screen / 2) - (self.largura / 2))
        self.posy = int((self.altura_screen / 2) - (self.altura / 2))

        #Muda o nome da aplicação no canto superior esquerdo
        self.app.title('Guia de Investimentos')

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
        label_titulo = Label(self.frame, text = 'Cotação Ibovespa', font = ('Times', 14, 'italic'))
        label_titulo.place(relx = 0.325, rely = 0.01)

    def lista_acoes(self):
        self.lista = ttk.Treeview(self.frame, height = 3, columns = ('col1', 'col2', 'col3'))
        self.lista.heading('#0', text = '')
        self.lista.heading('#1', text = 'Data')
        self.lista.heading('#2', text = 'Nome')
        self.lista.heading('#3', text = 'Cotação R$')

        self.lista.column('#0', width = 1)
        self.lista.column('#1', width = 50)
        self.lista.column('#2', width = 200)
        self.lista.column('#3', width = 100)

        #Adicionar nomes das ações na treeview
        
        self.lista.place(relx = 0.05, rely = 0.07, relwidth = 0.9, relheight = 0.25)

        self.scrol_lista = Scrollbar(self.frame, orient = 'vertical')
        self.lista.configure(yscroll=self.scrol_lista.set)
        self.scrol_lista.place(relx = 0.95, rely = 0.07, relwidth = 0.03, relheight = 0.25)

Aplicação()