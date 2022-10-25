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
    leJeu = Frame(fenetre, width=1000, height=400, bg='green')
    leJeu.pack(side='left')

    # Zone de dessin pour la grille
    laGrille = Frame(leJeu, width=200, height=200, bg='red')
    laGrille.pack(side='right')

    # Zone de dessin pour les informations
    informations = Frame(fenetre, width=536, height=400, bg='blue')
    informations.pack(side='right')

    fenetre.bind('<Escape>', lambda e: fenetre.destroy())

    fenetre.mainloop()


jeu()
