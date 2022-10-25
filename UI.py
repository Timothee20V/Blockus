import tkinter
from tkinter import *


def jeu():
    # Création de la fenetre du jeu
    fenetre = Tk()
    # Le nom du jeu
    fenetre.title("Blokus")
    # La taille de la fenetre
    fenetre.attributes('-fullscreen', True)

    # Zone de dessin pour le jeu
    leJeu = Canvas(fenetre, width=1000, height=400, bg='green')
    leJeu.grid(row=0, column=0)

    # Zone de dessin pour les informations
    informations = Canvas(fenetre, width=525, height=400, bg='blue')
    informations.grid(row=0, column=1)

    fenetre.bind('<Escape>', lambda e: fenetre.destroy())

    fenetre.mainloop()


jeu()
