from Libraries import Functions
from tkinter import *

#Inicializa um Objeto Tk
app = Tk()

# --------Configurações da Janela-------- #

#Dimensões da janela
largura = 480
altura = 480

#Dimensões do screen
largura_screen = app.winfo_screenwidth()
altura_screen = app.winfo_screenheight()

#Posicionamento da janela no screen
posx = int((largura_screen / 2) - (largura / 2))
posy = int((altura_screen / 2) - (altura / 2))

#Muda o nome da aplicação no canto superior esquerdo
app.title('Name')

#Muda o icone da janela
#app.iconbitmap("caminho/arquivo.ico")

#Defini o tamanho da janela
app.geometry('{}x{}+{}+{}'.format(largura, altura, posx, posy))

#Trava o redimensionamento da janela
app.resizable(False, False)

#Loop
app.mainloop()