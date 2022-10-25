import tkinter
from tkinter import *


def jeu():
    fen = Tk()
    fen.title("Blokus")
    fen.geometry("1920x1080")
    # fen.resizable(width=0, height=0)

    grille = Canvas(fen, width=1000, height=1080, bg='gray')
    grille.pack(side= 'left')

    information = Canvas(fen, width=920, height=1080, bg='blue')
    information.pack(side='right')

    fen.mainloop()


jeu()