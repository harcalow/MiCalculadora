from tkinter import * #importar libreria
raiz=Tk() #crear el Frame principal 
raiz.title("Calculadora")# titulo
raiz.geometry("320x400")
raiz.config(bg="#2A2A2A")

miFrame=Frame(raiz)
miFrame.pack(fill="x",padx=0,pady=0)
miFrame.config(bg="black",height=20)

#Pantalla1
datosPantalla=StringVar()
pantalla1=Entry(miFrame,width=21,textvariable=datosPantalla)
pantalla1.grid(row=1,column=1,padx=0,pady=10,columnspan=5)
pantalla1.config(background="black",fg="white",justify="right",font=("Comic sand MS",20))


#Pantalla2
numeroPantalla=StringVar()
pantalla=Entry(miFrame,width=21,textvariable=numeroPantalla)
pantalla.grid(row=2,column=1,padx=0,pady=10,columnspan=5)
pantalla.config(background="black",fg="white",justify="right",font=("Comic sand MS",20))

#operaciones
valor1=""
valor2=""
operacion_aux=""
total=0
flag=0
n="0"
numeroPantalla.set(n)

def numeroPulsado(num):
    global n 
    global flag 
    if num=="3.1416":
        n="3.1416"
        flag=1
    elif num=="2.7182":
        n="2.7182"
        flag=1
    elif num=="."and n=="0":
        n="0"
    elif num=="." and n.count(".")>0:
        n=n
    elif n == "0" or n=="": 
        n=num
    else:
        if flag==1:
            n=num
            flag=0
        else:
            n+=num

    
    numeroPantalla.set(n)    

def borraUltimo():
    global n 
    n=n[:-1]
    if n=="":
        n="0"
    numeroPantalla.set(n)

def borraTodo():
    global n 
    global valor1
    global valor2
    n="0"
    valor1=""
    valor2=""
    numeroPantalla.set(n)
    datosPantalla.set(n)

def cambioSigno():
    global n
    n=numeroPantalla.get()
    if n=="0":
        n=n
    elif n[0]=="-":
        n=n[1:]
    else:
        n="-"+n
    numeroPantalla.set(n)

def operaciones(operacion):
    global valor1
    global valor2
    global n
    global operacion_aux
    global total
    calcular=False
    if valor1=="":
        valor1=numeroPantalla.get()
        if datosPantalla.get()=="0":
            datosPantalla.set(datosPantalla.get()[1:]+valor1+operacion)
        else:
            datosPantalla.set(datosPantalla.get()+valor1+operacion)    
        operacion_aux=operacion
        n=""
    else:
        valor2=numeroPantalla.get()
        if n!="":
            datosPantalla.set(datosPantalla.get()+valor2+operacion)
        
        calcular=True

    if operacion_aux=="x" and calcular and n!="":
        total=int(valor1)*int(valor2)
        numeroPantalla.set(str(total))
        valor1=str(total)
        valor2=""
        operacion_aux=operacion
        calcular=False
        n=""
    
    elif operacion_aux=="+" and calcular and n!="":
        total=int(valor1)+int(valor2)
        numeroPantalla.set(str(total))
        valor1=str(total)
        valor2=""
        operacion_aux=operacion
        calcular=False
        n=""

    elif operacion_aux=="-" and calcular and n!="":
        total=int(valor1)-int(valor2)
        numeroPantalla.set(str(total))
        valor1=str(total)
        valor2=""
        operacion_aux=operacion
        calcular=False    
        n=""
    elif n=="":
        operacion_aux=operacion

    if operacion=="=":
        datosPantalla.set(numeroPantalla.get())
        datosPantalla.set("")
        

#botones 
caracter=[["π","e","C","⇇"],["7","8","9","x"],["4","5","6","-"],["1","2","3","+"],["+/-","0",".","="]]

#fila 1
boton=Button(miFrame,text=caracter[0][0],width=10,command=lambda:numeroPulsado("3.1416"))
boton.grid(row=3,column=1,padx=0,pady=10)
boton=Button(miFrame,text=caracter[0][1],width=10,command=lambda:numeroPulsado("2.7182"))
boton.grid(row=3,column=2,padx=0,pady=10)
boton=Button(miFrame,text=caracter[0][2],width=10,command=lambda:borraTodo())
boton.grid(row=3,column=3,padx=0,pady=10)
boton=Button(miFrame,text=caracter[0][3],width=10,command=lambda:borraUltimo())
boton.grid(row=3,column=4,padx=0,pady=10)

#fila2
boton=Button(miFrame,text=caracter[1][0],width=10,command=lambda:numeroPulsado(caracter[1][0]))
boton.grid(row=4,column=1,padx=0,pady=10)
boton=Button(miFrame,text=caracter[1][1],width=10,command=lambda:numeroPulsado(caracter[1][1]))
boton.grid(row=4,column=2,padx=0,pady=10)
boton=Button(miFrame,text=caracter[1][2],width=10,command=lambda:numeroPulsado(caracter[1][2]))
boton.grid(row=4,column=3,padx=0,pady=10)
boton=Button(miFrame,text=caracter[1][3],width=10,command=lambda:operaciones("x"))
boton.grid(row=4,column=4,padx=0,pady=10)

#fila3
boton=Button(miFrame,text=caracter[2][0],width=10,command=lambda:numeroPulsado(caracter[2][0]))
boton.grid(row=5,column=1,padx=0,pady=10)
boton=Button(miFrame,text=caracter[2][1],width=10,command=lambda:numeroPulsado(caracter[2][1]))
boton.grid(row=5,column=2,padx=0,pady=10)
boton=Button(miFrame,text=caracter[2][2],width=10,command=lambda:numeroPulsado(caracter[2][2]))
boton.grid(row=5,column=3,padx=0,pady=10)
boton=Button(miFrame,text=caracter[2][3],width=10,command=lambda:operaciones("-"))
boton.grid(row=5,column=4,padx=0,pady=10)

#fila4
boton=Button(miFrame,text=caracter[3][0],width=10,command=lambda:numeroPulsado(caracter[3][0]))
boton.grid(row=6,column=1,padx=0,pady=10)
boton=Button(miFrame,text=caracter[3][1],width=10,command=lambda:numeroPulsado(caracter[3][1]))
boton.grid(row=6,column=2,padx=0,pady=10)
boton=Button(miFrame,text=caracter[3][2],width=10,command=lambda:numeroPulsado(caracter[3][2]))
boton.grid(row=6,column=3,padx=0,pady=10)
boton=Button(miFrame,text=caracter[3][3],width=10,command=lambda:operaciones("+"))
boton.grid(row=6,column=4,padx=0,pady=10)

#fila5
boton=Button(miFrame,text=caracter[4][0],width=10,command=lambda:cambioSigno())
boton.grid(row=7,column=1,padx=0,pady=10)
boton=Button(miFrame,text=caracter[4][1],width=10,command=lambda:numeroPulsado(caracter[4][1]))
boton.grid(row=7,column=2,padx=0,pady=10)
boton=Button(miFrame,text=caracter[4][2],width=10,command=lambda:numeroPulsado(caracter[4][2]))
boton.grid(row=7,column=3,padx=0,pady=10)
boton=Button(miFrame,text=caracter[4][3],width=10,command=lambda:operaciones("="))
boton.grid(row=7,column=4,padx=0,pady=10)

raiz.mainloop()