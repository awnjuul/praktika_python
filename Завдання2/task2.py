import tkinter as tk
import math

window = tk.Tk()
window.title("calculator")
window.geometry("500x750")
window.resizable(False, False)
window.configure(bg="black")


# Функція вирахування операцій калькулятора
def calculate(operation):
    global formula

    if operation == 'C':
        formula = ''
    elif operation == "DEL":
        formula = formula[0:-1]
    elif operation == "X^2":
        formula = str((eval(formula)) ** 2)
    elif operation == "cos":
        formula = str(math.cos(eval(formula)))
    elif operation == "sin":
        formula = str(math.sin(eval(formula)))
    elif operation == "tan":
        formula = str(math.tan(eval(formula)))
    elif operation == "ln":
        formula = str(math.log1p(eval(formula)))
    elif operation == "log":
        formula = str(math.log(eval(formula)))
    elif operation == "ctg":
        formula = str(math.cos(eval(formula)) / math.sin(eval(formula)))
    elif operation == "bin":
        formula = str(bin(eval(formula)))
    elif operation == "=":
        formula = str(eval(formula))
    else:
        if formula == '0':
            formula = ''
        formula += operation
    label_text.configure(text=formula)


# Створення вікна для виводу вичислення
formula = "0"
label_text = tk.Label(text=formula, font=("Roboto", 30))
label_text.place(x=11, y=50)

# Створюємо кнопки
buttons = ["C", "del", "+", "=", "1", "2", "3", "4", "/", "4", "5", "*", "6", "7", "8", "9", "-", "0", "%", "X^2",
           "cos", "sin", "tan", "ctg", "bin", "log", "ln"]
x = 18
y = 140
for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    tk.Button(text=button, bg='orange', font=('Roboto', 20), command=get_lbl).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 18
        y += 81

window.mainloop()
