import grid as g
import player as p
from tkinter import *
from PIL import Image, ImageTk
from functools import partial
import shutil


def count(mainCount):
    if mainCount == 0:
        print("1")
        shutil.rmtree('pieces/blue')
        shutil.copytree('pieces/Start/blue', 'pieces/blue')
        shutil.rmtree('pieces/red')
        shutil.copytree('pieces/Start/red', 'pieces/red')
        shutil.rmtree('pieces/yellow')
        shutil.copytree('pieces/Start/yellow', 'pieces/yellow')
        shutil.rmtree('pieces/green')
        shutil.copytree('pieces/Start/green', 'pieces/green')
        return mainCount + 1


def takeCoord(event):
    informations.delete("all")

    x = int((event.x - jeu.offsetX) / sizeCells)
    y = int((event.y - jeu.offsetY) / sizeCells)
    informations.create_text(329, 230, text=x)
    informations.create_text(329, 240, text=y)

    if available(x, y):
        player1.putPiece(piece - 1, (x, y))

    jeu.updateGridTk(game)
    availablePiecesDisplay()


def modifPiece(event):
    if event.keysym == 'r':
        player1.rotationPieces(piece)
        image = Image.open(player1.namePieceListImg[piece])
        imRotate = image.rotate(-90)
        imRotate.save(player1.namePieceListImg[piece])
    if event.keysym == 's':
        player1.symmetryPieces(piece)


def available(x, y):
    for cell in player1.pieceToCoord()[piece - 1]:
        cellX, cellY = cell

        if x + cellX - 2 > jeu.numberCells - 1 or \
                y + cellY - 2 > jeu.numberCells - 1 or \
                x + cellX - 2 < 0 or y + cellY - 2 < 0 or \
                jeu.arrayGrid[x + cellX - 2][y + cellY - 2] != 0:
            informations.create_text(329, 250, text='Impossible')
            return False

        if jeu.arrayGrid[x + cellX - 2 - 1][y + cellY - 2 - 1] != 0:
            return False

    return True


def pieceFollowing(event):
    x, y = event.x, event.y

    '''img = Image.open(player1.namePieceListImg[piece])
    img = ImageTk.PhotoImage(img)
    mapimg = game.create_image(330, 330, image=img, anchor='nw')'''

    fileImg = player1.namePieceListImg[piece]
    img = PhotoImage(file=fileImg)
    temp[fileImg] = img
    img = game.create_image(330, 330, image=img, anchor='nw')

    if x > 830 or x < 30 or y > 830 or y < 30:
        availablePiecesDisplay()
    else:
        game.coords(img, x - 50, y - 50)


def availablePiecesDisplay():
    oX = 60
    oY = 300
    space = 10

    for i in range(5):
        for j in range(5):
            if i < 4 or (i == 4 and j == 2):
                if i * 5 + j + 1 <= 20:
                    num = i * 5 + j + 1
                else:
                    num = 21
                fileImg = player1.namePieceListImg[num]
                img = PhotoImage(file=fileImg)
                temp[fileImg] = img
                informations.create_image(oX + (100 + space) * j, oY + (100 + space) * i, image=img, anchor='nw')
                btn = Button(informations, image=img, command=partial(selectionPiece, num))
                btn.place(x=oX + (100 + space) * j, y=oY + (100 + space) * i)


def selectionPiece(num):
    global piece
    piece = num
    informations.create_text(329, 200, text=num)
    availablePiecesDisplay()


mainCount = 0
mainCount = count(mainCount)

piece = 1
numberCells = 20
sizeCells = 40

offsetX = 30
offsetY = 30

temp = {}

jeu = g.Grid(offsetX, offsetY, sizeCells, [], numberCells)

window = Tk()
window.title("Blokus")
window.attributes('-fullscreen', True)

game = Canvas(window, width=870, height=860)

game.grid(row=0, column=0)
game.create_rectangle(offsetX, offsetY, 830, 830)
game.create_line(871, 0, 871, 860, width=2)

informations = Canvas(window, width=658, height=860)
informations.grid(row=0, column=1)

jeu.creationGridTk(game)
player1 = p.Player("blue", "B", jeu)

availablePiecesDisplay()

game.bind('<Button-1>', takeCoord)

window.bind('<Escape>', lambda e: window.destroy())
window.bind('<Key>', modifPiece)

game.bind('<Motion>', pieceFollowing)

window.mainloop()
