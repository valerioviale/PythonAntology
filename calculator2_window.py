""" This code imports the tkinter module as tk. The tkinter module provides a toolkit for 
creating graphical user interfaces in Python.
The code defines four basic arithmetic functions: add, subtract, multiply, and divide. 
These functions take two arguments, x and y, and return the appropriate result.
The calculate function is called when the user clicks the "Calculate" button. 
It gets the values from the two input fields (entry_num1 and entry_num2) and 
the operator selection (operator_var) and performs the appropriate calculation 
based on the selected operator. The result is then displayed in the result_label.
The code creates the graphical user interface by creating a Tk object (root) and 
setting its title to "Calculator". 
It creates two input fields for the user to enter the two numbers, and 
a set of radio buttons for the user to select the operator. 
The default operator is set to +. It creates a "Calculate" button that 
calls the calculate function when clicked, and a label (result_label) to display the result.
Finally, the code starts the GUI event loop by calling the mainloop method on the root object, 
which displays the GUI and waits for user input. """

import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operator = operator_var.get()

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)

    result_label.config(text=result)

# Create the GUI
root = tk.Tk()
root.title("Calculator")

# Create the input fields
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create the operator selection
operator_var = tk.StringVar(value='+')

radio_add = tk.Radiobutton(root, text='+', variable=operator_var, value='+')
radio_add.pack()
radio_subtract = tk.Radiobutton(root, text='-', variable=operator_var, value='-')
radio_subtract.pack()
radio_multiply = tk.Radiobutton(root, text='*', variable=operator_var, value='*')
radio_multiply.pack()
radio_divide = tk.Radiobutton(root, text='/', variable=operator_var, value='/')
radio_divide.pack()

# Create the calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

# Create the result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
