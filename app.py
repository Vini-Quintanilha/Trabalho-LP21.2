from cProfile import label
from matplotlib import figure
from Libraries import Functions
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Inicializa um Objeto Tk
app = Tk()

#Class da aplicação
class Aplicação():
    def __init__(self):
        self.app = app
        self.tela()
        self.frame_tela()
        self.label()
        self.grafico()
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
        label_titulo = Label(self.frame, text = 'Guia de Investimento', font = ('Times', 14, 'italic'))
        label_titulo.pack()
    def grafico(self):
        pass

Aplicação()