from tkinter import *


class Grid:
    def __init__(self, x, y, sizeCase):
        self.offsetX = x
        self.offsetY = y
        self.sizeCase = sizeCase

        window = Tk()
        window.title("Blokus")
        window.attributes('-fullscreen', True)

        game = Canvas(window, width=1000, height=860)

        self.creationGrid(game)

        game.grid(row=0, column=0)
        game.create_rectangle(100, 30, 900, 830)

        informations = Canvas(window, width=528, height=860)
        informations.grid(row=0, column=1)

        window.bind('<Escape>', lambda e: window.destroy())

        window.mainloop()

    def creationGrid(self, game):
        for i in range(1, 20):
            game.create_line(i * self.sizeCase + self.offsetX,
                             self.offsetY,
                             i * self.sizeCase + self.offsetX,
                             800 + self.offsetY
                             )

        for i in range(1, 20):
            game.create_line(self.offsetX,
                             self.offsetY + i * self.sizeCase,
                             self.offsetX + 800,
                             self.offsetY + i * self.sizeCase
                             )


jeu = Grid(100, 30, 40)
