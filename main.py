# importar Tkinter
from tkinter import *
from tkinter import ttk

#cores
cor1 = '#3b3b3b' #preto 
cor2 = '#feffff' #branco 
cor3 = '#38576b' #azul
cor4 = '#ECEFF1' #cinzenta
cor5 = '#FFAB40' #laranja

#Cria uma nova janela
janela = Tk() 
janela.title('Calculadora') #Título da janela
janela.geometry('235x310') #Tamanho da janela ('largura x altura')
janela.config(bg=cor1)


#cria os frames
frame_display = Frame(janela, width=235, height=50, bg=cor4)
frame_display.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor1)
frame_corpo.grid(row=1, column=0)


#Cria label
valor_texto=StringVar()
app_label = Label(frame_display, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

#Variável valores
valores = ''

#criando função entrar_valores
def entrar_valores(event):
    global valores
    valores = valores + str(event)

    #passando resultado para display
    valor_texto.set(valores)

#criando função para calcular
def calcular():
    global valores
    resultado = eval(valores)
    valor_texto.set(str(resultado))

#criando função limpar
def limpar():
    global valores
    valores = ''
    valor_texto.set('')


#cria botões
b1=Button(frame_corpo, command=limpar, text='C', width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #cria o botão 'clean'
b1.place(x=0, y=0) #posiciona o botão na posição 0
b2=Button(frame_corpo, command= lambda: entrar_valores('%'), text='%', width=5 , height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118, y=0)
b3=Button(frame_corpo, command= lambda: entrar_valores('/'), text='/', width=5 , height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=177, y=0)

b4=Button(frame_corpo, command= lambda: entrar_valores('7'), text='7', width=5 , height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5=Button(frame_corpo, command= lambda: entrar_valores('8'), text='8', width=5 , height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=52)
b6=Button(frame_corpo, command= lambda: entrar_valores('9'), text='9', width=5 , height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=52)
b7=Button(frame_corpo, command= lambda: entrar_valores('*'), text='*', width=5 , height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=177, y=52)

b8=Button(frame_corpo, command= lambda: entrar_valores('4'), text='4', width=5 , height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9=Button(frame_corpo, command= lambda: entrar_valores('5'), text='5', width=5 , height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=104)
b10=Button(frame_corpo, command= lambda: entrar_valores('6'), text='6', width=5 , height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=118, y=104)
b11=Button(frame_corpo, command= lambda: entrar_valores('-'), text='-', width=5 , height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=177, y=104)

b12=Button(frame_corpo, command= lambda: entrar_valores('1'), text='1', width=5 , height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)
b13=Button(frame_corpo, command= lambda: entrar_valores('2'), text='2', width=5 , height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=156)
b14=Button(frame_corpo, command= lambda: entrar_valores('3'), text='3', width=5 , height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=118, y=156)
b15=Button(frame_corpo, command= lambda: entrar_valores('+'), text='+', width=5 , height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=177, y=156)

b16=Button(frame_corpo, command= lambda: entrar_valores('0'), text='0', width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #cria o botão 'clean'
b16.place(x=0, y=208) #posiciona o botão na posição 0
b17=Button(frame_corpo, command= lambda: entrar_valores('.'), text='.', width=5 , height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=208)
b18=Button(frame_corpo, command= lambda: calcular(), text='=', width=5 , height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=177, y=208)




janela.mainloop()