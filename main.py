import grid as g
import player as p
from tkinter import *
import tkinter.ttk as ttk


def takeCoord(event):
    informations.delete("all")

    x = int((event.x - jeu.offsetX) / sizeCells)
    y = int((event.y - jeu.offsetY) / sizeCells)
    informations.create_text(500, 500, text=x)
    informations.create_text(500, 550, text=y)

    if available(x, y):
        player1.putPiece(piece, (x, y))

    jeu.updateGridTk(game)


def modifPiece(event):
    print(event.keysym)
    if event.keysym == 'r':
        player1.rotationPieces(piece)
    if event.keysym == 's':
        player1.symmetryPieces(piece)


def available(x, y):
    for cell in player1.pieceToCoord()[piece]:
        cellX, cellY = cell
        if x + cellX - 2 > jeu.numberCells -1:
            informations.create_text(400, 525, text='Impossible')
            return False
        if y + cellY - 2 > jeu.numberCells - 1:
            informations.create_text(400, 525, text='Impossible')
            return False
        if x + cellX - 2 < 0:
            informations.create_text(400, 525, text='Impossible')
            return False
        if y + cellY - 2 < 0:
            informations.create_text(400, 525, text='Impossible')
            return False
        if jeu.arrayGrid[x + cellX - 2][y + cellY - 2] != 0:
            informations.create_text(400, 525, text='Impossible')
            return False

    return True


piece = 12
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
window.bind('<Key>', modifPiece)

window.mainloop()
