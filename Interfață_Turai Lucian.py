import tkinter as tk
import math
import matplotlib.pyplot as plt
import numpy as np

calculation = ""
a_value = 0
b_value = 0
c_value = 0

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation, {"__builtins__": None}, {
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "cot": lambda x: 1 / math.tan(math.radians(x)),
            "log": math.log10,
            "sqrt": math.sqrt
        }))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

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

root = tk.Tk()
root.geometry("500x700")
root.title("Complex Calculator")

text_result = tk.Text(root, height=2, width=22, font=("Helvetica", 24), bg="#f0f0f0", fg="#333")
text_result.grid(columnspan=5)

button_font = ("Helvetica", 14)
button_bg = "#ffffff"
button_fg = "#333333"
operation_bg = "#ffcccc"
function_bg = "#ccffcc"
clear_bg = "#ffcc99"
equal_bg = "#ccff99"

# Numeric buttons
buttons = [
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('0', 5, 1)
]

for (text, row, col) in buttons:
    tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), width=5, font=button_font, bg=button_bg, fg=button_fg).grid(row=row, column=col)

# Operation buttons
operations = [
    ('+', 2, 3), ('-', 3, 3),
    ('*', 4, 3), ('/', 5, 3),
    ('(', 5, 0), (')', 5, 2)
]

for (text, row, col) in operations:
    tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), width=5, font=button_font, bg=operation_bg, fg=button_fg).grid(row=row, column=col)

# Function buttons
functions = [
    ('sin', 'sin('), ('cos', 'cos('), ('tan', 'tan('), ('cot', 'cot('),
    ('log', 'log('), ('√', 'sqrt(')
]

for i, (text, symbol) in enumerate(functions):
    tk.Button(root, text=text, command=lambda s=symbol: add_to_calculation(s), width=5, font=button_font, bg=function_bg, fg=button_fg).grid(row=i+2, column=4)

# Additional buttons
tk.Button(root, text='a', command=set_a_value, width=5, font=button_font, bg=function_bg, fg=button_fg).grid(row=6, column=0)
tk.Button(root, text='b', command=set_b_value, width=5, font=button_font, bg=function_bg, fg=button_fg).grid(row=6, column=1)
tk.Button(root, text='c', command=set_c_value, width=5, font=button_font, bg=function_bg, fg=button_fg).grid(row=6, column=2)
tk.Button(root, text='Plot', command=plot_graph, width=11, font=button_font, bg=function_bg, fg=button_fg).grid(row=6, column=3, columnspan=1)

# Clear and equal buttons
tk.Button(root, text='C', command=clear_field, width=11, font=button_font, bg=clear_bg, fg=button_fg).grid(row=7, column=2, columnspan=2)
tk.Button(root, text='=', command=evaluate_calculation, width=11, font=button_font, bg=equal_bg, fg=button_fg).grid(row=7, column=0, columnspan=1)

root.mainloop()
