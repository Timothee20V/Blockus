from tkinter import *


class Grille:
    def __init__(self, x, y, size):
        self.offsetX = x
        self.offsetY = y
        self.tailleCase = size

    def creationGrilleAffiche(self, other):
        for i in range(1, 20):
            leJeu.create_line(i * self.tailleCase + self.offsetX,
                              self.offsetY,
                              i * self.tailleCase + self.offsetX,
                              800 + self.offsetY
                              )

        for i in range(1, 20):
            leJeu.create_line(self.offsetX,
                              self.offsetY + i * self.tailleCase,
                              self.offsetX + 800,
                              self.offsetY + i * self.tailleCase
                              )


jeu = Grille(100, 30, 40)

fenetre = Tk()
# Le nom du jeu
fenetre.title("Blokus")
# La taille de la fenetre
fenetre.attributes('-fullscreen', True)

# Zone de dessin pour le jeu
leJeu = Canvas(fenetre, width=1000, height=860)

jeu.creationGrilleAffiche(leJeu)

leJeu.grid(row=0, column=0)

leJeu.create_rectangle(100, 30, 900, 830)

# Zone de dessin pour les informations
informations = Canvas(fenetre, width=528, height=860)
informations.grid(row=0, column=1)

fenetre.bind('<Escape>', lambda e: fenetre.destroy())

fenetre.mainloop()
