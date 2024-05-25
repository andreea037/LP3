import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation +=str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk() #genereaza interfata cu utilizatorul
root.geometry("300x300")
root.title("Calculator")

text_result = tk.Text(root, height = 2, width = 16, font = ("Arial", 24))
text_result.grid(columnspan=5)

b1 = tk.Button(root, text='1', command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
b1.grid(row = 2, column = 1)

b2 = tk.Button(root, text='2', command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
b2.grid(row = 2, column = 2)

b3 = tk.Button(root, text='3', command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
b3.grid(row = 2, column = 3)

b4 = tk.Button(root, text='4', command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
b4.grid(row = 3, column = 1)

b5 = tk.Button(root, text='5', command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
b5.grid(row = 3, column = 2)

b6 = tk.Button(root, text='6', command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
b6.grid(row = 3, column = 3)

b7 = tk.Button(root, text='7', command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
b7.grid(row = 4, column = 1)

b8 = tk.Button(root, text='8', command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
b8.grid(row = 4, column = 2)

b9 = tk.Button(root, text='9', command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
b9.grid(row = 4, column = 3)

b0 = tk.Button(root, text='0', command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
b0.grid(row = 5, column = 2)

bPlus = tk.Button(root, text='+', command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
bPlus.grid(row = 2, column = 4)

bMinus = tk.Button(root, text='-', command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
bMinus.grid(row = 3, column = 4)

bMult = tk.Button(root, text='*', command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
bMult.grid(row = 4, column = 4)

bDiv = tk.Button(root, text='/', command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
bDiv.grid(row = 5, column = 4)

bPar1 = tk.Button(root, text='(', command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
bPar1.grid(row = 5, column = 1)

bPar2 = tk.Button(root, text=')', command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
bPar2.grid(row = 5, column = 3)

bSterge = tk.Button(root, text='C', command=clear_field, width=11, font=("Arial", 14))
bSterge.grid(row = 6, column = 3, columnspan=2)

bEgal = tk.Button(root, text='=', command=evaluate_calculation, width=11, font=("Arial", 14))
bEgal.grid(row = 6, column = 1, columnspan=2)

root.mainloop() #this method listens for events, such as button clicks or keypresses
                #and blocks any code that comes after it from running until you close the window




