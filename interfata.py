import tkinter as tk
import math
import matplotlib.pyplot as plt
import numpy as np

calculation = ""
a_value = 0
b_value = 0
c_value = 0

def add_to_calculation(symbol): #adauga in text valorile de pe butoane
    global calculation
    calculation += str(symbol) # transforma toate simbolurile in string pentru a nu se face calculul direct
    text_result.delete(1.0, "end") #sterge textul dupa ce se apasa =
    text_result.insert(1.0, calculation) #insereaza valorile


def evaluate_calculation():
    global calculation
    try:
        # evalueaza calculul
        calculation = str(eval(calculation, {"__builtins__": None}, {
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "cot": lambda x: 1/math.tan(math.radians(x)),
            "log": math.log10,  # Change to log base 10 for standard logarithm
            "sqrt": math.sqrt
        }))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error") # genereaza un msj de eroare daca nu este bun calculul

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def set_a_value():
    global a_value
    try:
        a_value = float(calculation)
        clear_field()
        text_result.insert(1.0, f"a = {a_value}")
    except:
        clear_field()
        text_result.insert(1.0, "Invalid a")

def set_b_value():
    global b_value
    try:
        b_value = float(calculation)
        clear_field()
        text_result.insert(1.0, f"b = {b_value}")
    except:
        clear_field()
        text_result.insert(1.0, "Invalid b")

def set_c_value():
    global c_value
    try:
        c_value = float(calculation)
        clear_field()
        text_result.insert(1.0, f"c = {c_value}")
    except:
        clear_field()
        text_result.insert(1.0, "Invalid c")

def plot_graph():
    global a_value, b_value, c_value
    x = np.linspace(-10, 10, 400)
    y = a_value * x**2 + b_value * x + c_value
    plt.figure()
    plt.plot(x, y, label=f'{a_value}x^2 + {b_value}x + {c_value} = 0')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

root = tk.Tk()  # #genereaza interfata cu utilizatorul
root.geometry("600x800") #dimensiunile
root.title("Calculator") #titlul

text_result = tk.Text(root, height=2, width=18, font=("Arial", 24)) #genereaza textul scris
text_result.grid(columnspan=6) #dimensiunile

# butoane pentru cifre
buttons = [
    ('1', 2, 1), ('2', 2, 2), ('3', 2, 3),
    ('4', 3, 1), ('5', 3, 2), ('6', 3, 3),
    ('7', 4, 1), ('8', 4, 2), ('9', 4, 3), ('0', 5, 2)
]

for (text, row, col) in buttons:
    tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), width=5, font=("Arial", 14), bg="#d1e7dd", fg="black").grid(row=row, column=col)
    # functie lambda pt ca doar adauga simboluri, nu le calculeaza direct
# butoanele pentru operatii simple
operations = [
    ('+', 2, 4), ('-', 3, 4),
    ('*', 4, 4), ('/', 5, 4),
    ('(', 5, 1), (')', 5, 3)
]

for (text, row, col) in operations:
    tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), width=5, font=("Arial", 14), bg="#f8d7da", fg="black").grid(row=row, column=col)

# butoane pentru functiile complexe
functions = [
    ('sin', 'sin('), ('cos', 'cos('), ('tan', 'tan('), ('cot', 'cot('),
    ('log', 'log('), ('√', 'sqrt(')
]

for i, (text, symbol) in enumerate(functions):
        tk.Button(root, text=text, command=lambda s=symbol: add_to_calculation(s), width=5, font=("Arial", 14), bg="#cff4fc", fg="black").grid(row=i+2, column=5)

# butoane aditionale
tk.Button(root, text='a', command=set_a_value, width=5, font=("Arial", 14), bg="#e2e3e5", fg="black").grid(row=6, column=1, columnspan=1)
tk.Button(root, text='b', command=set_b_value, width=5, font=("Arial", 14), bg="#e2e3e5", fg="black").grid(row=6, column=2, columnspan=1)
tk.Button(root, text='c', command=set_c_value, width=5, font=("Arial", 14), bg="#e2e3e5", fg="black").grid(row=6, column=3, columnspan=1)
tk.Button(root, text='Plot', command=plot_graph, width=5, font=("Arial", 14), bg="#d1e7dd", fg="black").grid(row=6, column=4, columnspan=1)

# butoane pentru stergere si egal
tk.Button(root, text='C', command=clear_field, width=11, font=("Arial", 14), bg="#f8d7da", fg="black").grid(row=7, column=3, columnspan=2)
tk.Button(root, text='=', command=evaluate_calculation, width=11, font=("Arial", 14), bg="#d1e7dd", fg="black").grid(row=7, column=1, columnspan=2)

root.mainloop()  #metoda "asculta" evenimente, cum ar fi apasarea butoanelor
                #si blocheaza orice cod ce apare dupa el din a rula pana inchidem feresatra