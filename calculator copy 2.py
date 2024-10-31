import tkinter as tk
import math

# Définitions de fonctions
def click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "√":
        try:
            result = str(math.sqrt(float(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    elif button_text in ["sin", "cos", "tan"]:
        try:
            value = float(entry.get())
            if button_text == "sin":
                result = str(math.sin(math.radians(value)))
            elif button_text == "cos":
                result = str(math.cos(math.radians(value)))
            elif button_text == "tan":
                result = str(math.tan(math.radians(value)))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    elif button_text == "ln":
        try:
            result = str(math.log(float(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    elif button_text == "log":
        try:
            result = str(math.log10(float(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    elif button_text == "^":
        entry.insert(tk.END, "**")
    elif button_text == "x²":
        try:
            result = str(float(entry.get*entry.get))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur") 

    else:
        entry.insert(tk.END, button_text)

"""elif button_text == "π":
        try:
            result = str(math.factorial(float(entry.get)))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")"""

# Fenêtre principale
window = tk.Tk()
window.title("Calculatrice Scientifique")
window.geometry("400x500")
window.configure(bg="#eedae4")

# Zone d'affichage
entry = tk.Entry(window, font=("Segoe UI", 20), width=17, borderwidth=0, relief="flat", bg="#F3F3F3", fg="#FF70A6")
entry.grid(row=0, column=0, columnspan=7, padx=10, pady=10)

# Couleurs des boutons
button_colors = {"number": "pink", "operator": "#F3F3F3", "function": "#ff70a6", "equals": "#c42863", "clear": "#FF6961"}

# Configuration des boutons
buttons = [
    ("7", "number"), ("8", "number"), ("9", "number"), ("/", "operator"), ("sin", "function"), ("cos", "function"), ("n!", "function"),
    ("4", "number"), ("5", "number"), ("6", "number"), ("*", "operator"), ("tan", "function"), ("√", "function"), ("x²", "function"),
    ("1", "number"), ("2", "number"), ("3", "number"), ("-", "operator"), ("ln", "function"), ("log", "function"), ("π", "function"),
    ("0", "number"), (".", "number"), ("C", "clear"), ("+", "operator"), ("^", "operator"), ("=", "equals")
]

# Placement des boutons
for i, (text, btn_type) in enumerate(buttons):
    color = button_colors[btn_type]
    button = tk.Button(window, text=text, command=lambda x=text: click(x), width=6, height=2, font=("Segoe UI", 12),bg=color, fg="black" if btn_type != "equals" and btn_type!= "clear" else "white",activebackground="#D1D1D1" if btn_type != "equals" else "#6f1937", relief="flat")
    
    # pour des aisons de responsives design (optimisation de l'espace de la calculette sur le canva), j'utilise les propriétés weight et sticky
    button.grid(row=(i//7)+1, column=i%7, padx=2, pady=2, sticky="nsew") # sticky = "nsew" permet de le faire coller sur tous les côtés
    window.grid_rowconfigure((i//6)+1, weight=1)   # Ajustement des lignes
    window.grid_columnconfigure(i%7, weight=1)     # Ajustement des colonnes
boutegal = tk.Button(window, text="=", command=lambda x=text: click(x), width=6, height=2, font=("Segoe UI", 12),bg = color, fg= "white", activebackground="#6f1937", relief = "flat")
boutegal.grid(row= 4,column= 5, columnspan=2, padx=2, pady= 2, sticky ="nsew")
# Redimensionnement automatique
for i in range(1, 6):
    window.grid_columnconfigure(i, weight=1)

# Lancer l'application
window.mainloop()
