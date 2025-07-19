import tkinter as tk
import math


def click(button_text):
    expression = entry.get()

    try:
        if button_text == "=":
            expression = expression.replace('^', '')  # For power
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)

        elif button_text == "Cancel":
            entry.delete(0, tk.END)

        elif button_text == "sin":
            result = math.sin(math.radians(float(expression)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

        elif button_text == "cos":
            result = math.cos(math.radians(float(expression)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

        elif button_text == "tan":
            result = math.tan(math.radians(float(expression)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

        elif button_text == "mod":
            entry.insert(tk.END, "%")

        elif button_text == "log":
            result = math.log10(float(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

        elif button_text == "ln":
            result = math.log(float(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

        elif button_text == "sqrt":
            result = math.sqrt(float(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

        elif button_text == "pi":
            entry.insert(tk.END, str(math.pi))

        else:
            entry.insert(tk.END, button_text)

    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("Scientific Calculator")

label = tk.Label(window, text="Scientific Calculator", font=("Arial", 16))
label.grid(row=0, column=0, columnspan=4, pady=10)

entry = tk.Entry(window, width=30, font=("Arial", 14), borderwidth=5)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['sin', 'cos', 'tan', 'mod'],
    ['log', 'ln', 'sqrt', '^'],
    ['pi',       'Cancel']
]

row_start = 2
for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        tk.Button(window, text=button_text, width=7, height=2, font=("Arial", 12),
                  command=lambda text=button_text: click(text)).grid(row=row_start + i, column=j, padx=5, pady=5)

window.mainloop()


