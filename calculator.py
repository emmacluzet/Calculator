from tkinter import*
import math

# Function called when a button is clicked
def click(text_button):
    current = entry.get()
    value = float(current)
    # If the "=" button is clicked, evaluate the current expression
    if text_button == "=":
        try:
            # Evaluate the expression and display it next to the current entry
            result = str(eval(current))
            entry.delete(0, END)
            entry.insert(0, result)
        except:
            # if an error occurs, display "Error" in the entry field
            entry.delete(0, END)
            entry.insert(0, "Erreur")
    # If the "C" button is clicked, clear the entry field
    elif text_button == "C":
        entry.delete(0, END)
    elif text_button == "√":
        try:
            result = str(math.sqrt(float(current)))
            entry.delete(0, END)
            entry.insert(0, result)
        except:
            entry.delete(0, END)
            entry.insert(0, "Erreur")
    elif text_button in ["sin", "cos","tan"]:
        try:
            if text_button == "sin":
                result = str(math.sin(math.radans(value))) # math.radians : converts a degree value into radians
            elif text_button == "cos":
                result = str(math.cos(math.radians(value)))
            elif text_button == "tan":
                result = str(math.tan(math.radians(value)))
            entry.delete(0, END)
            entry.insert(0, result)
        except:
            entry.delete(0, END)
            entry.insert(0, "Erreur")
    elif text_button == "ln":
        try:
            result = str(math.log(value))
        except:
            entry.delete(0, END)
            entry.insert(0, "Erreur")
    elif text_button == "log":
        try:
            result = str(math.log10(value))
        except:
            entry.delete(0, END)
            entry.insert(0, "Erreur")
    else:
        # Add the clicked button'ss next to the entry field
        entry.insert(END, text_button)


# fen creation
fen=Tk()
fen.title("Calculator")
fen.configure(bg ="#2E2E2E")

# Buttons
buttons=["7","8","9","/","4","5","6","*","1","2","3","+","0",".","C","-","=","^"]

science=["π","e","|x|","x²","log","ln","√","n!","sin","cos","tan"]

# Create the display area (text entry for calculation)

entry=Entry(fen, width=30, font=("Arial", 18),borderwidth=2, relief="raised")
entry.grid(row=0, column=0, columnspan=7)

rowValue = 3
colValue = 4
# Loop to create and place the buttons in a grid
for button in buttons:
    calcul = lambda x=button: click(x)
    tempo = Button(fen, text=button, width=5, height=2, font=("Arial", 18), command=calcul,borderwidth=5,relief="ridge",activebackground="#c7ceff", background="#dbf0ff")
    tempo.grid(row=rowValue, column=colValue)
    colValue += 1
    if colValue > 7:
        colValue = 4
        rowValue += 1

rowVal=3
colVal=0
for button in science:
    calcul = lambda x=button: click(x)
    tempo = Button(fen, text=button, width=5, height=2, font=("Arial", 18), command=calcul,borderwidth=5,relief="ridge",activebackground="white", background="#4caf50")
    tempo.grid(row=rowVal, column=colVal)
    colVal += 1
    if colVal > 3:
        colVal = 0
        rowVal += 1
# RadioButton
"""
buttonN = Radiobutton(fen, text="normal", value="n", command = calcul)
buttonN.grid(row=1, column=0)
buttonN = Radiobutton(fen, text="scientifique", value="s", command = calcul)
buttonN.grid(row=1, column=1)
"""
# MenuButton
"""
trigonometry = Menubutton(fen, text='Trigonométrie', width='20', borderwidth=2, bg='white', activebackground='darkorange', relief = "raised")
trigonometry.grid(row=1, column= 0, columnspan=2)

menuDeroulant1 = Menu(trigonometry, tearoff= 0)

menuDeroulant1.add_command(label='sin', command = sinus)
menuDeroulant1.add_command(label="cos", command = cosinus)
menuDeroulant1.add_command(label='tan', command = tangente)

trigonometry.configure(menu=menuDeroulant1)
"""

fen.mainloop()