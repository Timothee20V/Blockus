import grid as g
import player as p
from tkinter import *
from PIL import Image
from functools import partial
import shutil
from save_load import *
import os
import copy


def start():
    global player
    global player1
    global player2
    global player3
    global player4
    global window
    global game
    global informations
    global jeu
    global mainCount

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

        player1 = p.Player("blue", "B", jeu)
        player2 = p.Player("red", "R", jeu)
        player3 = p.Player("yellow", "Y", jeu)
        player4 = p.Player("green", "G", jeu)
        player = player1

        if os.path.exists('save/save_otherData.txt'):
            if loadDataCounter() == 'bleu':
                player = player1
            if loadDataCounter() == 'red':
                player = player2
            if loadDataCounter() == 'yellow':
                player = player3
            if loadDataCounter() == 'green':
                player = player4

        namePieceList = {1: "pieces/piece1", 2: "pieces/piece2", 3: "pieces/piece3", 4: "pieces/piece4",
                         5: "pieces/piece5", 6: "pieces/piece6", 7: "pieces/piece7", 8: "pieces/piece8",
                         9: "pieces/piece9", 10: "pieces/piece10", 11: "pieces/piece11", 12: "pieces/piece12",
                         13: "pieces/piece13", 14: "pieces/piece14", 15: "pieces/piece15", 16: "pieces/piece16",
                         17: "pieces/piece17", 18: "pieces/piece18", 19: "pieces/piece19", 20: "pieces/piece20",
                         21: "pieces/piece21"
                         }

        if os.path.exists('save/save_piecesB.txt') and loadGamePiece(player1.color) != {}:
            player1.namePieceList = loadGamePiece(player1.color)
        else:
            player1.namePieceList = copy.deepcopy(namePieceList)

        if os.path.exists('save/save_piecesR.txt') and loadGamePiece(player2.color) != {}:
            player2.namePieceList = loadGamePiece(player2.color)
        else:
            player2.namePieceList = copy.deepcopy(namePieceList)

        if os.path.exists('save/save_piecesY.txt') and loadGamePiece(player3.color) != {}:
            player3.namePieceList = loadGamePiece(player3.color)
        else:
            player3.namePieceList = copy.deepcopy(namePieceList)

        if os.path.exists('save/save_piecesG.txt') and loadGamePiece(player4.color) != {}:
            player4.namePieceList = loadGamePiece(player4.color)
        else:
            player4.namePieceList = copy.deepcopy(namePieceList)

        if os.path.exists('save/save_plateau.txt'):
            jeu.arrayGrid = loadGameBoard()

        saveGameBoard(jeu.arrayGrid)
        saveGamePieces(player1.namePieceList, player1.color)
        saveGamePieces(player2.namePieceList, player2.color)
        saveGamePieces(player3.namePieceList, player3.color)
        saveGamePieces(player4.namePieceList, player4.color)
        saveDataTour(player.color)

        mainCount = mainCount + 1

        availablePiecesDisplay()

    game.bind('<Button-1>', takeCoord)

    window.bind('<Escape>', lambda e: endGame())
    window.bind('<Key>', keyboard)

    game.bind('<Motion>', pieceFollowing)


def takeCoord(event):
    global player

    x = int((event.x - jeu.offsetX) / sizeCells)
    y = int((event.y - jeu.offsetY) / sizeCells)
    printInformation(x)
    printInformation(y)

    if available(x, y):
        player.putPiece(piece - 1, (x, y))
        player.removePiece(piece)

        nextPlayer()


def keyboard(event):
    global mainCount

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

    if event.keysym == 'f':
        window.destroy()
        print(jeu.countCells())

    if event.keysym == 't':
        os.remove('save/save_otherData.txt')
        os.remove('save/save_piecesB.txt')
        os.remove('save/save_piecesG.txt')
        os.remove('save/save_piecesY.txt')
        os.remove('save/save_piecesR.txt')
        os.remove('save/save_plateau.txt')
        window.destroy()
        mainCount = 0
        start()


def nextPlayer():
    global player
    if player == player1 and player2.surrend != True:
        player = player2
    elif player == player1 and player3.surrend != True:
        player = player3
    elif player == player1 and player4.surrend != True:
        player = player4

    elif player == player2 and player3.surrend != True:
        player = player3
    elif player == player2 and player4.surrend != True:
        player = player4
    elif player == player2 and player1.surrend != True:
        player = player1

    elif player == player3 and player4.surrend != True:
        player = player4
    elif player == player3 and player1.surrend != True:
        player = player1
    elif player == player3 and player2.surrend != True:
        player = player2

    elif player == player4 and player1.surrend != True:
        player = player1
    elif player == player4 and player2.surrend != True:
        player = player2
    elif player == player4 and player3.surrend != True:
        player = player3

    if player.surrend:
        window.destroy()
        print(jeu.countCells())
    else:
        jeu.updateGridTk(game)
        availablePiecesDisplay()


def available(x, y):
    inAngle = False

    beginningTurn = False

    nextToColor = False

    # Beginning or not ?
    if len(player.namePieceList) == 21:
        beginningTurn = True

    # Check multiple condition of each part of the piece
    for cell in player.pieceToCoord()[piece - 1]:
        cellX, cellY = cell

        # Piece is outside the box or on another piece or not available?
        if x + cellX - 2 > jeu.numberCells - 1 or \
                y + cellY - 2 > jeu.numberCells - 1 or \
                x + cellX - 2 < 0 or y + cellY - 2 < 0 or \
                jeu.arrayGrid[x + cellX - 2][y + cellY - 2] != '0' or \
                piece not in player.namePieceList:
            printInformation('Piece is outside the box or on another piece or not available')
            return False

        # Part of the piece is in the angle at the beginning ?
        if beginningTurn and \
                ((x + cellX - 2, y + cellY - 2) == (0, 0) or
                 (x + cellX - 2, y + cellY - 2) == (0, 19) or
                 (x + cellX - 2, y + cellY - 2) == (19, 0) or
                 (x + cellX - 2, y + cellY - 2) == (19, 19)):
            inAngle = True
            printInformation('Part of the piece is in the angle at the beginning')

        # Piece is too attached to his color ?
        if not beginningTurn and \
                (x + cellX - 2 != 0 and jeu.arrayGrid[x + cellX - 2 - 1][y + cellY - 2] == player.initial or
                 x + cellX - 2 != 19 and jeu.arrayGrid[x + cellX - 2 + 1][y + cellY - 2] == player.initial or
                 y + cellY - 2 != 0 and jeu.arrayGrid[x + cellX - 2][y + cellY - 2 - 1] == player.initial or
                 y + cellY - 2 != 19 and jeu.arrayGrid[x + cellX - 2][y + cellY - 2 + 1] == player.initial):
            printInformation('Impossible')
            printInformation('Piece is too attached to his color')
            return False

        # Part of the piece is next to his color ?
        if not beginningTurn and \
                (x + cellX - 2 != 0 and y + cellY - 2 != 0 and
                 jeu.arrayGrid[x + cellX - 2 - 1][y + cellY - 2 - 1] == player.initial) or \
                (x + cellX - 2 != 19 and y + cellY - 2 != 0 and
                 jeu.arrayGrid[x + cellX - 2 + 1][y + cellY - 2 - 1] == player.initial) or \
                (x + cellX - 2 != 0 and y + cellY - 2 != 19 and
                 jeu.arrayGrid[x + cellX - 2 - 1][y + cellY - 2 + 1] == player.initial) or \
                (x + cellX - 2 != 19 and y + cellY - 2 != 19 and
                 jeu.arrayGrid[x + cellX - 2 + 1][y + cellY - 2 + 1] == player.initial):
            nextToColor = True
            print('Part of the piece is next to his color')

    # Piece is in the angle at the beginning ?
    if beginningTurn and not inAngle:
        printInformation("Piece must be in the angle at the beginning")
        return False

    # Piece is next to his color ?
    if not beginningTurn and not nextToColor:
        printInformation("Piece must be next to his color")
        return False

    return True


def pieceFollowing(event):
    x, y = event.x, event.y
    global piece

    try:
        fileImg = "pieces/piecesX2/{}".format(player.namePieceListImg[piece])
        img = PhotoImage(file=fileImg)
        temp[fileImg] = img
        img = game.create_image(-330, -330, image=img, anchor='nw')

        if not x > 830 or x < 30 or y > 830 or y < 30:
            jeu.updateGridTk(game)
            x = int((event.x - jeu.offsetX) / sizeCells)
            y = int((event.y - jeu.offsetY) / sizeCells)
            game.coords(img, x * 40 - 50, y * 40 - 50)
    except:
        var = True


def availablePiecesDisplay():
    global informations
    oX = 60
    oY = 300
    space = 10

    informations = Canvas(window, width=658, height=860)
    informations.grid(row=0, column=1)
    printInformation(text)

    lose = Button(informations, text='Joueur bloqué', command=playerStuck)
    lose.place(x=329, y=150)

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


def selectionPiece(num):
    global piece
    global text
    piece = num
    printInformation(text=num)
    availablePiecesDisplay()


def printInformation(text):
    informations.delete('all')
    informations.create_text(329, 80, text='Les informations relatives au jeu actuel')
    informations.create_text(329, 100, text=text)


def playerStuck():
    player.surrend = True
    nextPlayer()


def endGame():
    saveGameBoard(jeu.arrayGrid)
    saveGamePieces(player1.namePieceList, player1.color)
    saveGamePieces(player2.namePieceList, player2.color)
    saveGamePieces(player3.namePieceList, player3.color)
    saveGamePieces(player4.namePieceList, player4.color)
    saveDataTour(player.color)
    window.destroy()


piece = 1
numberCells = 20
sizeCells = 40
turn = 0
offsetX = 30
offsetY = 30

text = ''

temp = {}

mainCount = 0
start()

window.mainloop()
