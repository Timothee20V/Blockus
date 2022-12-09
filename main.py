import grid as g
import player as p
from save_load import *
from tkinter import *
from PIL import Image, ImageTk
from functools import partial
import shutil


def count(mainCount):
    if mainCount == 0:
        shutil.rmtree('pieces/blue')
        shutil.rmtree('pieces/piecesX2/pieces/blue')
        shutil.copytree('pieces/Start/blue', 'pieces/blue')
        shutil.copytree('pieces/Start/pieces/blue', 'pieces/piecesX2/pieces/blue')
        shutil.rmtree('pieces/red')
        shutil.rmtree('pieces/piecesX2/pieces/red')
        shutil.copytree('pieces/Start/red', 'pieces/red')
        shutil.copytree('pieces/Start/pieces/red', 'pieces/piecesX2/pieces/red')
        shutil.rmtree('pieces/yellow')
        shutil.rmtree('pieces/piecesX2/pieces/yellow')
        shutil.copytree('pieces/Start/yellow', 'pieces/yellow')
        shutil.copytree('pieces/Start/pieces/yellow', 'pieces/piecesX2/pieces/yellow')
        shutil.rmtree('pieces/green')
        shutil.rmtree('pieces/piecesX2/pieces/green')
        shutil.copytree('pieces/Start/green', 'pieces/green')
        shutil.copytree('pieces/Start/pieces/green', 'pieces/piecesX2/pieces/green')
        return mainCount + 1


def takeCoord(event):
    global player
    global counterGame

    x = int((event.x - jeu.offsetX) / sizeCells)
    y = int((event.y - jeu.offsetY) / sizeCells)
    informations.create_text(329, 230, text=x)
    informations.create_text(329, 240, text=y)

    if available(x, y):
        player.putPiece(piece - 1, (x, y))
        player.removePiece(piece)
        if counterGame == 0 and player1.surrend != True:
            player = player1
            counterGame += 1
        elif counterGame == 1 and player2.surrend != True:
            player = player2
            counterGame += 1
        elif counterGame == 2 and player3.surrend != True:
            player = player3
            counterGame += 1
        elif counterGame == 3 and player4.surrend != True:
            player = player4
            counterGame = 0

    jeu.updateGridTk(game)
    availablePiecesDisplay()


def modifPiece(event):
    if event.keysym == 'r':
        player.rotationPieces(piece)
        image = Image.open(player.namePieceListImg[piece])
        imRotate = image.rotate(-90)
        imRotate.save(player.namePieceListImg[piece])
        image = Image.open("pieces/piecesX2/{}".format(player.namePieceListImg[piece]))
        imRotate = image.rotate(-90)
        imRotate.save("pieces/piecesX2/{}".format(player.namePieceListImg[piece]))
    if event.keysym == 's':
        player.symmetryPieces(piece)
        image = Image.open(player.namePieceListImg[piece])
        imFlip = image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
        imFlip.save(player.namePieceListImg[piece])
        image = Image.open("pieces/piecesX2/{}".format(player.namePieceListImg[piece]))
        imFlip = image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
        imFlip.save("pieces/piecesX2/{}".format(player.namePieceListImg[piece]))


def available(x, y):
    for cell in player.pieceToCoord()[piece - 1]:
        cellX, cellY = cell

        if x + cellX - 2 > jeu.numberCells - 1 or \
                y + cellY - 2 > jeu.numberCells - 1 or \
                x + cellX - 2 < 0 or y + cellY - 2 < 0 or \
                jeu.arrayGrid[x + cellX - 2][y + cellY - 2] != '0' or \
                piece not in player.namePieceList:
            informations.create_text(329, 250, text='Impossible')
            return False
        try:
            if jeu.arrayGrid[x + cellX - 2 - 1][y + cellY - 2 - 0] != '0' or \
                    jeu.arrayGrid[x + cellX - 2 + 1][y + cellY - 2 - 0] != '0' or \
                    jeu.arrayGrid[x + cellX - 2 - 1][y + cellY - 2 + 0] != '0' or \
                    jeu.arrayGrid[x + cellX - 2 + 1][y + cellY - 2 + 0] != '0' or \
                    jeu.arrayGrid[x + cellX - 2 - 0][y + cellY - 2 - 1] != '0' or \
                    jeu.arrayGrid[x + cellX - 2 + 0][y + cellY - 2 - 1] != '0' or \
                    jeu.arrayGrid[x + cellX - 2 - 0][y + cellY - 2 + 1] != '0' or \
                    jeu.arrayGrid[x + cellX - 2 + 0][y + cellY - 2 + 1] != '0':
                informations.create_text(329, 250, text='Impossible')
                return False
        except IndexError:
            print("Bordure")

    return True


def pieceFollowing(event):
    x, y = event.x, event.y
    global piece

    try:
        fileImg = "pieces/piecesX2/{}".format(player.namePieceListImg[piece])
        img = PhotoImage(file=fileImg)
        temp[fileImg] = img
        img = game.create_image(-330, -330, image=img, anchor='nw')

        if x > 830 or x < 30 or y > 830 or y < 30:
            '''availablePiecesDisplay()'''
        else:
            jeu.updateGridTk(game)
            x = int((event.x - jeu.offsetX) / sizeCells)
            y = int((event.y - jeu.offsetY) / sizeCells)
            game.coords(img, x * 40 - 50, y * 40 - 50)
    except:
        x = 1


def availablePiecesDisplay():
    oX = 60
    oY = 300
    space = 10

    informations = Canvas(window, width=658, height=860)
    informations.grid(row=0, column=1)

    print(player.namePieceList)

    for i in range(5):
        for j in range(5):
            if i < 4 or (i == 4 and j == 2):
                if i * 5 + j + 1 <= 20:
                    num = i * 5 + j + 1
                else:
                    num = 21

                if num in player.namePieceList:
                    fileImg = player.namePieceListImg[num]
                    img = PhotoImage(file=fileImg)
                    temp[fileImg] = img
                    informations.create_image(oX + (100 + space) * j, oY + (100 + space) * i, image=img, anchor='nw')
                    btn = Button(informations, image=img, command=partial(selectionPiece, num))
                    btn.place(x=oX + (100 + space) * j, y=oY + (100 + space) * i)
                else:
                    val = True


def selectionPiece(num):
    global piece
    piece = num
    informations.create_text(329, 200, text=num)
    availablePiecesDisplay()


def endGame():
    playerBaseColor = [player1.color, player2.color, player3.color, player4.color]
    playerBaseNameList = [player1.namePieceList, player2.namePieceList, player3.namePieceList, player4.namePieceList]
    i = 0

    saveGameBoard(jeu.arrayGrid)
    saveDataTour(counterGame)
    for playerColor in playerBaseColor:
        saveGamePieces(playerBaseNameList[i], playerColor)
        i += 1
    window.destroy()


def reset():
    global counterGame

    plateauSave = [['0' for i in range(20)] for j in range(20)]
    saveGameBoard(plateauSave)
    saveDataTour(1)

    playerBase = ["red", "blue", "green", "yellow"]
    namePieceListBase = {1: "pieces/piece1", 2: "pieces/piece2", 3: "pieces/piece3", 4: "pieces/piece4",
                         5: "pieces/piece5", 6: "pieces/piece6", 7: "pieces/piece7", 8: "pieces/piece8",
                         9: "pieces/piece9", 10: "pieces/piece10", 11: "pieces/piece11", 12: "pieces/piece12",
                         13: "pieces/piece13", 14: "pieces/piece14", 15: "pieces/piece15", 16: "pieces/piece16",
                         17: "pieces/piece17", 18: "pieces/piece18", 19: "pieces/piece19", 20: "pieces/piece20",
                         21: "pieces/piece21"
                         }
    for playerName in playerBase:
        saveGamePieces(namePieceListBase, playerName)

    player1.namePieceList = namePieceListBase
    player2.namePieceList = namePieceListBase
    player3.namePieceList = namePieceListBase
    player4.namePieceList = namePieceListBase

    counterGame = loadDataCounter()

    game.delete('all')
    jeu.creationArrayGrid(loadGameBoard())
    jeu.creationGridTk(game)

    game.create_rectangle(offsetX, offsetY, 830, 830)
    availablePiecesDisplay()
    jeu.updateGridTk(game)


mainCount = 0
mainCount = count(mainCount)

piece = 1
numberCells = 20
sizeCells = 40
turn = 0
offsetX = 30
offsetY = 30

count = 0

temp = {}

jeu = g.Grid(offsetX, offsetY, sizeCells, loadGameBoard(), numberCells)

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

colorSwitch = ["blue", "red", "yellow", "green"]

for color in colorSwitch:

    listPiece = loadGamePiece(color)
    if (listPiece == {}):
        listPiece = "None"

    if (color == "blue"):
        player1 = p.Player("blue", "B", jeu, listPiece)
    elif (color == "red"):
        player2 = p.Player("red", "R", jeu, listPiece)
    elif (color == "yellow"):
        player3 = p.Player("yellow", "Y", jeu, listPiece)
    elif (color == "green"):
        player4 = p.Player("green", "G", jeu, listPiece)

player = player1
counterGame = loadDataCounter()

availablePiecesDisplay()

game.bind('<Button-1>', takeCoord)

window.bind('<Escape>', lambda e: endGame())
window.bind('<Key>', modifPiece)
window.bind('<t>', lambda e: reset())
game.bind('<Motion>', pieceFollowing)

window.mainloop()
