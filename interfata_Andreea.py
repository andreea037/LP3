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
        # Evaluate the calculation
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

root = tk.Tk()  # Generate the user interface
root.geometry("600x800")
root.title("Complex Calculator")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=6)

# Numeric buttons
buttons = [
    ('1', 2, 1), ('2', 2, 2), ('3', 2, 3),
    ('4', 3, 1), ('5', 3, 2), ('6', 3, 3),
    ('7', 4, 1), ('8', 4, 2), ('9', 4, 3), ('0', 5, 2)
]

for (text, row, col) in buttons:
    tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), width=5, font=("Arial", 14)).grid(row=row, column=col)

# Operation buttons
operations = [
    ('+', 2, 4), ('-', 3, 4),
    ('*', 4, 4), ('/', 5, 4),
    ('(', 5, 1), (')', 5, 3)
]

for (text, row, col) in operations:
    tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), width=5, font=("Arial", 14)).grid(row=row, column=col)

# Function buttons
functions = [
    ('sin', 'sin('), ('cos', 'cos('), ('tan', 'tan('), ('cot', 'cot('),
    ('log', 'log('), ('√', 'sqrt(')
]

for i, (text, symbol) in enumerate(functions):
    tk.Button(root, text=text, command=lambda s=symbol: add_to_calculation(s), width=5, font=("Arial", 14)).grid(row=2+i, column=5)

# Additional buttons
tk.Button(root, text='a', command=set_a_value, width=5, font=("Arial", 14)).grid(row=7, column=1)
tk.Button(root, text='b', command=set_b_value, width=5, font=("Arial", 14)).grid(row=7, column=2)
tk.Button(root, text='c', command=set_c_value, width=5, font=("Arial", 14)).grid(row=7, column=3)
tk.Button(root, text='Plot', command=plot_graph, width=11, font=("Arial", 14)).grid(row=7, column=4, columnspan=2)

# Clear and equal buttons
tk.Button(root, text='C', command=clear_field, width=11, font=("Arial", 14)).grid(row=8, column=3, columnspan=2)
tk.Button(root, text='=', command=evaluate_calculation, width=11, font=("Arial", 14)).grid(row=8, column=1, columnspan=2)

root.mainloop()  # This method listens for events, such as button clicks or keypresses and blocks any code that comes after it from running until you close the window.
