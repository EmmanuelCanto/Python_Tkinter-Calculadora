from tkinter import * 

raiz=Tk()
raiz.title('Calculadora')

miFrame=Frame(raiz)
miFrame.pack()


# --------------ACCIONES DE BOTONES--------------
def btnClick(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)

# ------------CONVIERTE LO REGISTRADO A RESULTADO----------------
def operacion():
    global operador
    try:
        opera=eval(operador)
    except:
        clear()
        opera=('ERROR')
    input_text.set(opera)
# -----------FUNCION PARA LIMPIAR LA PANTALLA-----------------
def clear():
    global operador
    operador=''
    input_text.set(operador)
    

# --------------DECLARACION DE VARIABLE PARA MOSTRAR EN LA PANTALLA--------------
input_text=StringVar()
# --------------DECLARACION PARA GUARDAR LO QUE PONGAMOS POR MEDIO DE LOS BOTONES--------------
operador='' 

botonColor=('#fff')

# --------------PANTALLA--------------
pantalla = Entry(miFrame, textvariable=input_text)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg='#292929',relief='sunken',bd=10, fg='#03f943', justify='right')

# -------------FILA UNO----------------
botonDiv = Button(miFrame, fg='#fff', bg='#292929', text='EXP', width=3, command=lambda:btnClick('**'))
botonDiv.grid(row=2, column=3)
botonClear = Button(miFrame, bg='#ef495c', text='C', width=3, command=clear)
botonClear.grid(row=2, column=4)



# -------------FILA DOS---------------
boton7 = Button(miFrame, bg=botonColor, text='7', width=3, command=lambda:btnClick(7))
boton7.grid(row=3, column=1)
boton8 = Button(miFrame, bg=botonColor, text='8', width=3, command=lambda:btnClick(8))
boton8.grid(row=3, column=2)
boton9 = Button(miFrame, bg=botonColor, text='9', width=3, command=lambda:btnClick(9))
boton9.grid(row=3, column=3)
botonDiv = Button(miFrame, fg='#fff', bg='#292929', text='/', width=3, command=lambda:btnClick('/'))
botonDiv.grid(row=3, column=4)

# -------------FILA TRES---------------
boton4 = Button(miFrame, bg=botonColor, text='4', width=3, command=lambda:btnClick(4))
boton4.grid(row=4, column=1)
boton5 = Button(miFrame, bg=botonColor, text='5', width=3, command=lambda:btnClick(5))
boton5.grid(row=4, column=2)
boton6 = Button(miFrame, bg=botonColor, text='6', width=3, command=lambda:btnClick(6))
boton6.grid(row=4, column=3)
botonMult = Button(miFrame, fg='#fff', bg='#292929', text='X', width=3, command=lambda:btnClick('*'))
botonMult.grid(row=4, column=4)

# -------------FILA CUATRO--------------
boton1 = Button(miFrame, bg=botonColor, text='1', width=3, command=lambda:btnClick(1))
boton1.grid(row=5, column=1)
boton2 = Button(miFrame, bg=botonColor, text='2', width=3, command=lambda:btnClick(2))
boton2.grid(row=5, column=2)
boton3 = Button(miFrame, bg=botonColor, text='3', width=3, command=lambda:btnClick(3))
boton3.grid(row=5, column=3)
botonRest = Button(miFrame,fg='#fff', bg='#292929', text='-', width=3, command=lambda:btnClick('-'))
botonRest.grid(row=5, column=4)

# -------------FILA CINCO---------------

botonComa = Button(miFrame, bg=botonColor, text='.', width=3, command=lambda:btnClick('.'))
botonComa.grid(row=6, column=1)
boton0 = Button(miFrame, bg=botonColor, text='0', width=3, command=lambda:btnClick(0))
boton0.grid(row=6, column=2)
botonIgual = Button(miFrame, bg=botonColor, text='=', width=3, command=operacion)
botonIgual.grid(row=6, column=3)
botonSuma = Button(miFrame,fg='#fff', bg='#292929', text='+', width=3, command=lambda:btnClick('+'))
botonSuma.grid(row=6, column=4)



raiz.mainloop()