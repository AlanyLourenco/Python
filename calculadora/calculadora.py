from tkinter import *
from tkinter import ttk
from tkinter import font


cor1="#000000"
cor2="#566362"
cor3="#e6b8ba"
cor4="#80afb0"
cor5="#ffffff"


janela= Tk()
janela.title("Calculadora")
janela.geometry("235x330")
janela.config(bg=cor2)


frame_tela=Frame(janela, width=260, height=50,bg=cor1)
frame_tela.grid(row=0,column=0)

frame_corpo=Frame(janela, width=260, height=290,bg=cor3)
frame_corpo.grid(row=1,column=0)


todos_valores=''
valor_texto=StringVar()



def entrada_valores(event):
    global todos_valores
    todos_valores=todos_valores+str(event)
    valor_texto.set(todos_valores)



def calcular():
    global todos_valores
    resultado=eval(todos_valores)
    
    valor_texto.set(str(resultado))


def limpar_tela():
    global todos_valores
    todos_valores=""
    valor_texto.set("")



app_label=Label(frame_tela, textvariable=valor_texto, width=16,height=2,padx=7,relief=FLAT,anchor="e",justify=RIGHT, font=('Ivy 16'),bg=cor1,fg=cor5)
app_label.place(x=0,y=0)


b1=Button(frame_corpo,command=limpar_tela,text="C", width=8,height=2, bg=cor5, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b1.place(x=0,y=0)

b2=Button(frame_corpo,command=lambda:entrada_valores('%'),text="%", width=3,height=2,bg=cor5, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b2.place(x=118,y=0)

b3=Button(frame_corpo,command=lambda:entrada_valores('/'),text="/", width=3,height=2,bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b3.place(x=177,y=0)


b4=Button(frame_corpo,command=lambda:entrada_valores('7'),text="7", width=3,height=2,bg=cor5, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b4.place(x=0,y=56)

b5=Button(frame_corpo,command=lambda:entrada_valores('8'),text="8", width=3,height=2,bg=cor5, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b5.place(x=59,y=56)

b6=Button(frame_corpo,command=lambda:entrada_valores('9'),text="9", width=3,height=2,bg=cor5, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b6.place(x=118,y=56)

b7=Button(frame_corpo,command=lambda:entrada_valores('*'),text="*", width=3,height=2,bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b7.place(x=177,y=56)


b8=Button(frame_corpo,command=lambda:entrada_valores('4'),text="4", width=3,height=2,bg=cor5, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b8.place(x=0,y=112)

b9=Button(frame_corpo,command=lambda:entrada_valores('5'),text="5", width=3,height=2,bg=cor5, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b9.place(x=59,y=112)

b10=Button(frame_corpo,command=lambda:entrada_valores('6'),text="6", width=3,height=2,bg=cor5, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b10.place(x=118,y=112)

b11=Button(frame_corpo,command=lambda:entrada_valores('-'),text="-", width=3,height=2,bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b11.place(x=177,y=112)


b12=Button(frame_corpo,command=lambda:entrada_valores('1'),text="1", width=3,height=2,bg=cor5, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b12.place(x=0,y=168)

b13=Button(frame_corpo,command=lambda:entrada_valores('2'),text="2", width=3,height=2,bg=cor5, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b13.place(x=59,y=168)

b14=Button(frame_corpo,command=lambda:entrada_valores('3'),text="3", width=3,height=2,bg=cor5, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b14.place(x=118,y=168)

b15=Button(frame_corpo,command=lambda:entrada_valores('+'),text="+", width=3,height=2,bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b15.place(x=177,y=168)


b16=Button(frame_corpo,command=lambda:entrada_valores('0'),text="0", width=8,height=2, bg=cor5, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b16.place(x=0,y=224)

b17=Button(frame_corpo,command=lambda:entrada_valores('.'),text=".", width=3,height=2,bg=cor5, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b17.place(x=118,y=224)


b18=Button(frame_corpo,command=calcular,text="=", width=3,height=2,bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b18.place(x=177,y=224)


janela.mainloop()