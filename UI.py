from tkinter import *


def creationGrilleAffiche(leJeu):
    offsetX = 100
    offsetY = 30
    tailleCase = 40
    for i in range(1,20):
        leJeu.create_line(i * tailleCase + offsetX, offsetY, i * tailleCase + offsetX, 800 + offsetY)
    for i in range(1,20):
        leJeu.create_line(offsetX, offsetY + i * tailleCase, offsetX + 800, offsetY + i * tailleCase)



def jeu():
    # Création de la fenetre du jeu
    fenetre = Tk()
    # Le nom du jeu
    fenetre.title("Blokus")
    # La taille de la fenetre
    fenetre.attributes('-fullscreen', True)

    # Zone de dessin pour le jeu
    leJeu = Canvas(fenetre, width=1000, height=860)
    leJeu.grid(row=0, column=0)

    leJeu.create_rectangle(100, 30, 900, 830)

    # Zone de dessin pour les informations
    informations = Canvas(fenetre, width=528, height=860)
    informations.grid(row=0, column=1)

    creationGrilleAffiche(leJeu)

    fenetre.bind('<Escape>', lambda e: fenetre.destroy())

    fenetre.mainloop()


jeu()
