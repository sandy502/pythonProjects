from decimal import Decimal
from distutils.log import error
from tkinter import *
from turtle import width
from unicodedata import name

expression = ""

#function for text box entry
def press(num):
    global expression

    expression = expression + str(num)
    #it is used to set expression in the textbox
    equation.set(expression)

#function for evaluation of expression through equalto
def equalpress():
    try:
        global expression
        #evaluation method used to evaluate expression inside the text box
        total = str(eval(expression))
        equation.set(total)    
        expression = ""
    except:
        equation.set(error)
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    #to create GUI window
    gui = Tk()
    #for changing background color
    gui.configure(background="light green")
    #for defining title
    gui.title("Simple Calculator")
    #to define dimensions to the box
    gui.geometry("300x270")
    #it is a variable class
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=80)

    btn1 = Button(gui,text = '1', fg='black', bg='white', command=lambda: press(1), height=2, width=8)
    btn1.grid(row=2, column=0)

    btn2 = Button(gui,text = '2', fg='black', bg='white', command=lambda: press(2), height=2, width=8)
    btn2.grid(row=2, column=1)

    btn3 = Button(gui,text = '3', fg='black', bg='white', command=lambda: press(3), height=2, width=8)
    btn3.grid(row=2, column=2)

    btn4 = Button(gui,text = '4', fg='black', bg='white', command=lambda: press(4), height=2, width=8)
    btn4.grid(row=3, column=0)

    btn5 = Button(gui,text = '5', fg='black', bg='white', command=lambda: press(5), height=2, width=8)
    btn5.grid(row=3, column=1)

    btn6 = Button(gui,text = '6', fg='black', bg='white', command=lambda: press(6), height=2, width=8)
    btn6.grid(row=3, column=2)

    btn7 = Button(gui,text = '7', fg='black', bg='white', command=lambda: press(7), height=2, width=8)
    btn7.grid(row=4, column=0)

    btn8 = Button(gui,text = '8', fg='black', bg='white', command=lambda: press(8), height=2, width=8)
    btn8.grid(row=4, column=1)

    btn9 = Button(gui,text = '9', fg='black', bg='white', command=lambda: press(9), height=2, width=8)
    btn9.grid(row=4, column=2)

    btn0 = Button(gui,text = '0', fg='black', bg='white', command=lambda: press(0), height=2, width=8)
    btn0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=2, width=8)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=2, width=8)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=2, width=8)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='white', command=lambda: press("/"), height=2, width=8)
    divide.grid(row=5, column=3)
 
    Decimal = Button(gui, text='.', fg='black', bg='white', command=lambda: press('.'), height=2, width=8)
    Decimal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='black', bg='white', command=clear, height=2, width=8)
    clear.grid(row=5, column='1')
 
    equal= Button(gui, text=' = ', fg='black', bg='white', command=equalpress, height=2, width=8)
    equal.grid(row=6, column=0)

    gui.mainloop()