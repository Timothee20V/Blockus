from tkinter import *


class Grille:
    def __init__(self, x, y, size):
        self.offsetX = x
        self.offsetY = y
        self.tailleCase = size

        fenetre = Tk()
        fenetre.title("Blokus")
        fenetre.attributes('-fullscreen', True)

        game = Canvas(fenetre, width=1000, height=860)

        self.creationGrid(game)

        game.grid(row=0, column=0)
        game.create_rectangle(100, 30, 900, 830)

        informations = Canvas(fenetre, width=528, height=860)
        informations.grid(row=0, column=1)

        fenetre.bind('<Escape>', lambda e: fenetre.destroy())

        fenetre.mainloop()

    def creationGrid(self, game):
        for i in range(1, 20):
            game.create_line(i * self.tailleCase + self.offsetX,
                             self.offsetY,
                             i * self.tailleCase + self.offsetX,
                             800 + self.offsetY
                             )

        for i in range(1, 20):
            game.create_line(self.offsetX,
                             self.offsetY + i * self.tailleCase,
                             self.offsetX + 800,
                             self.offsetY + i * self.tailleCase
                             )


jeu = Grille(100, 30, 40)
