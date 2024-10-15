import tkinter as tk

# fen creation

fen=tk.Tk()
fen.title("Calculator")
# fen.minsize(200,200)

# Buttons

buttons=["7","8","9","/","4","5","6","*","1","2","3","+","0",".","C","-","="]

# Functions

def click(text_button):
    current = entry.get()
    if text_button == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    elif text_button == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text_button)


# Entry

entry= tk.Entry(fen, width=18, font=("Arial", 18),borderwidth=2, relief="raised")
entry.grid(row=0, column=0, columnspan=3)

# window creation

rowValue = 1
colValue = 0
for button in buttons:
    temp = lambda x=button: click(x)
    tk.Button(fen, text=button, width=5, height=2, font=("Arial", 18), command=temp,borderwidth=5,relief="ridge",activebackground="#c7ceff", background="#dbf0ff").grid(row=rowValue, column=colValue)
    colValue += 1
    if colValue > 3:
        colValue = 0
        rowValue += 1

fen.mainloop()