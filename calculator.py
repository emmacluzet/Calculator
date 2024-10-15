import tkinter as tk

# fen creation
fen=tk.Tk()
fen.title("Calculator")

# Buttons
buttons=["7","8","9","/","4","5","6","*","1","2","3","+","0",".","C","-","="]

science=["π","e","|x|","x²"]

# Function called when a button is clicked
def click(text_button):
    current = entry.get()
    # If the "=" button is clicked, evaluate the current expression
    if text_button == "=":
        try:
            # Evaluate the expression and display it next to the current entry
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            # if an error occurs, display "Error" in the entry field
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    # If the "C" button is clicked, clear the entry field
    elif text_button == "C":
        entry.delete(0, tk.END)
    else:
        # Add the clicked button'ss next to the entry field
        entry.insert(tk.END, text_button)


# Create the display area (text entry for calculation)

entry= tk.Entry(fen, width=30, font=("Arial", 18),borderwidth=2, relief="raised")
entry.grid(row=0, column=0, columnspan=7)

rowValue = 3
colValue = 4
# Loop to create and place the buttons in a grid
for button in buttons:
    calcul = lambda x=button: click(x)
    tempo =  tk.Button(fen, text=button, width=5, height=2, font=("Arial", 18), command=calcul,borderwidth=5,relief="ridge",activebackground="#c7ceff", background="#dbf0ff")
    tempo.grid(row=rowValue, column=colValue)
    colValue += 1
    if colValue > 7:
        colValue = 4
        rowValue += 1

rowVal=3
colVal=0
for button in science:
    calcul = lambda x=button: click(x)
    tempo =  tk.Button(fen, text=button, width=5, height=2, font=("Arial", 18), command=calcul,borderwidth=5,relief="ridge",activebackground="#c7ceff", background="white")
    tempo.grid(row=rowVal, column=colVal)
    colVal += 1
    if colVal > 3:
        colVal = 0
        rowVal += 1

calcul2=0
# RadioButton
buttonN = tk.Radiobutton(fen, text="normal", value="n", command = calcul)
buttonN.grid(row=2, column=0)
buttonN = tk.Radiobutton(fen, text="scientifique", value="s", command = calcul)
buttonN.grid(row=2, column=1)
fen.mainloop()