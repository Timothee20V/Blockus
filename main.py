import grid as g
import player as p
from tkinter import *
import tkinter.ttk as ttk


def takeCoord(event):
    informations.delete("all")
    piece = 9
    x = int((event.x - jeu.offsetX) / sizeCells)
    y = int((event.y - jeu.offsetY) / sizeCells)
    informations.create_text(500, 500, text=x)
    informations.create_text(500, 550, text=y)
    jeu.arrayGrid[x][y] = "X"

    jeu.updateGridTk(game)

    jeu.arrayGridDisplay()
    print("")


numberCells = 20
sizeCells = 40

offsetX = 100
offsetY = 30

jeu = g.Grid(offsetX, offsetY, sizeCells, [], numberCells)

window = Tk()
window.title("Blokus")
window.attributes('-fullscreen', True)

game = Canvas(window, width=1000, height=860)

game.grid(row=0, column=0)
game.create_rectangle(100, 30, 900, 830)

informations = Canvas(window, width=528, height=860)
informations.grid(row=0, column=1)

jeu.creationGridTk(game)
player1 = p.Player("blue", "B", jeu)

game.bind('<Button-1>', takeCoord)

window.bind('<Escape>', lambda e: window.destroy())

window.mainloop()
