import math
import tkinter as tk

# fen creation

fen=tk.Tk()
fen.title("Calculator")
fen.geometry("400x600")

Zone=tk.Canvas(fen, width=400, height=600, bg="white")

# Buttons

Buttons=["7","8","9","/",
         "4","5","6","*",
         "1","2","3","+",
         "="]

# Functions

def sketch_calc():
    return

def addition(nombre):
    return

def soustraction():
    return

def division():
    return

def multiplication():
    return

# Entry

entry= tk.Entry(fen, width=16, font=("Arial", 24),borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=1)

# Principal Program

addition()


fen.mainloop()