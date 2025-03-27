import tkinter as tk
import math

def on_click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif button_text == "√":
        try:
            result = math.sqrt(float(entry_var.get()))
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif button_text == "^":
        entry_var.set(entry_var.get() + "**")
    else:
        entry_var.set(entry_var.get() + button_text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x450")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), bd=10, relief=tk.GROOVE, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

buttons = [
    ("(", ")", "√", "/"),
    ("7", "8", "9", "*"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "+"),
    ("C", "0", "=", "^")
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack()
    for btn in row:
        button = tk.Button(row_frame, text=btn, font=("Arial", 18), width=5, height=2, command=lambda b=btn: on_click(b))
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

root.mainloop()
