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
    global gameWindow
    global information
    global game
    global mainCount

    game = g.Grid(offsetX, offsetY, sizeCells, [], numberCells)

    window = Tk()
    window.title("Blokus")
    window.attributes('-fullscreen', True)

    gameWindow = Canvas(window, width=870, height=860)

    gameWindow.grid(row=0, column=0)
    gameWindow.create_rectangle(offsetX, offsetY, 830, 830)
    gameWindow.create_line(871, 0, 871, 860, width=2)

    information = Canvas(window, width=658, height=860)
    information.grid(row=0, column=1)

    game.creationGridTk(gameWindow)

    # If the game begin do that
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

        # Generate 4 players
        player1 = p.Player("blue", "B", game)
        player2 = p.Player("red", "R", game)
        player3 = p.Player("yellow", "Y", game)
        player4 = p.Player("green", "G", game)
        player = player1

        # Load a game if an old game exist
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
            game.arrayGrid = loadGameBoard()

        # Reset the current game folder
        saveGameBoard(game.arrayGrid)
        saveGamePieces(player1.namePieceList, player1.color)
        saveGamePieces(player2.namePieceList, player2.color)
        saveGamePieces(player3.namePieceList, player3.color)
        saveGamePieces(player4.namePieceList, player4.color)
        saveDataTour(player.color)

        mainCount = mainCount + 1

        # Display avalable pieces for the players
        availablePiecesDisplay()

    # If we place a piece on the screen do takeCoord function
    gameWindow.bind('<Button-1>', takeCoord)

    # If we click on escape, end the game
    window.bind('<Escape>', lambda e: endGame())

    # If we click on the keyboard
    window.bind('<Key>', keyboard)

    # For the follwing of the mouse
    gameWindow.bind('<Motion>', pieceFollowing)


# Put the piece on the array if we can
def takeCoord(event):
    global player

    x = int((event.x - game.offsetX) / sizeCells)
    y = int((event.y - game.offsetY) / sizeCells)
    printInformation(x)
    printInformation(y)

    # Test if we can put the piece
    if available(x, y):

        # Put the piece
        player.putPiece(piece - 1, (x, y))

        # Remove the piece
        player.removePiece(piece)

        # Next player
        nextPlayer()


# Typing on the keyboard
def keyboard(event):
    global mainCount

    # If we type 'r' on the keyboard
    if event.keysym == 'r':

        # Rotation of the piece in the array / image
        player.rotationPieces(piece)
        image = Image.open(player.namePieceListImg[piece])
        imRotate = image.rotate(-90)
        imRotate.save(player.namePieceListImg[piece])
        image = Image.open("pieces/piecesX2/{}".format(player.namePieceListImg[piece]))
        imRotate = image.rotate(-90)
        imRotate.save("pieces/piecesX2/{}".format(player.namePieceListImg[piece]))

    # If we type 's' on the keyboard
    if event.keysym == 's':

        # Do the symmetry of the piece in the array / image
        player.symmetryPieces(piece)
        image = Image.open(player.namePieceListImg[piece])
        imFlip = image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
        imFlip.save(player.namePieceListImg[piece])
        image = Image.open("pieces/piecesX2/{}".format(player.namePieceListImg[piece]))
        imFlip = image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
        imFlip.save("pieces/piecesX2/{}".format(player.namePieceListImg[piece]))

    # If we type 'e' we want to terminate the game without saving
    if event.keysym == 'e':

        # Close the window
        window.destroy()

        # Display the scores
        winner, b, r, y, g = game.countCells()
        if winner == 'b':
            print("The winner is the Blue Player !!")
        if winner == 'r':
            print("The winner is the Red Player !!")
        if winner == 'y':
            print("The winner is the Yellow Player !!")
        if winner == 'g':
            print("The winner is the Green Player !!")
        print("Blue Player with {} cells".format(b))
        print("Red Player with {} cells".format(r))
        print("Yellow Player with {} cells".format(b))
        print("Green Player with {} cells".format(g))

    # If we type 'd' we want to reset the game
    if event.keysym == 'd':

        # Reset all the save files
        os.remove('save/save_otherData.txt')
        os.remove('save/save_piecesB.txt')
        os.remove('save/save_piecesG.txt')
        os.remove('save/save_piecesY.txt')
        os.remove('save/save_piecesR.txt')
        os.remove('save/save_plateau.txt')
        window.destroy()
        mainCount = 0
        start()


# Next player after the current player have played
def nextPlayer():
    global player

    # All test in order to know which is the next player, depending on the current player and other player statu
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

    # If all player can't play, end the game
    if player.surrend:
        window.destroy()
        print(game.countCells())
    else:
        game.updateGridTk(gameWindow)
        availablePiecesDisplay()


# Test if we can put a piece on a position
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
        if x + cellX - 2 > game.numberCells - 1 or \
                y + cellY - 2 > game.numberCells - 1 or \
                x + cellX - 2 < 0 or y + cellY - 2 < 0 or \
                game.arrayGrid[x + cellX - 2][y + cellY - 2] != '0' or \
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
                (x + cellX - 2 != 0 and game.arrayGrid[x + cellX - 2 - 1][y + cellY - 2] == player.initial or
                 x + cellX - 2 != 19 and game.arrayGrid[x + cellX - 2 + 1][y + cellY - 2] == player.initial or
                 y + cellY - 2 != 0 and game.arrayGrid[x + cellX - 2][y + cellY - 2 - 1] == player.initial or
                 y + cellY - 2 != 19 and game.arrayGrid[x + cellX - 2][y + cellY - 2 + 1] == player.initial):
            printInformation('Piece is too attached to his color')
            return False

        # Part of the piece is next to his color ?
        if not beginningTurn and \
                (x + cellX - 2 != 0 and y + cellY - 2 != 0 and
                 game.arrayGrid[x + cellX - 2 - 1][y + cellY - 2 - 1] == player.initial) or \
                (x + cellX - 2 != 19 and y + cellY - 2 != 0 and
                 game.arrayGrid[x + cellX - 2 + 1][y + cellY - 2 - 1] == player.initial) or \
                (x + cellX - 2 != 0 and y + cellY - 2 != 19 and
                 game.arrayGrid[x + cellX - 2 - 1][y + cellY - 2 + 1] == player.initial) or \
                (x + cellX - 2 != 19 and y + cellY - 2 != 19 and
                 game.arrayGrid[x + cellX - 2 + 1][y + cellY - 2 + 1] == player.initial):
            nextToColor = True
            printInformation('Part of the piece is next to his color')

    # Piece is in the angle at the beginning ?
    if beginningTurn and not inAngle:
        printInformation("Piece must be in the angle at the beginning")
        return False

    # Piece is next to his color ?
    if not beginningTurn and not nextToColor:
        printInformation("Piece must be next to his color")
        return False

    return True


# Function allowing the pieces to follow the mouse
def pieceFollowing(event):
    x, y = event.x, event.y
    global piece

    # Try if the piece can follow the mouse
    try:
        fileImg = "pieces/piecesX2/{}".format(player.namePieceListImg[piece])
        img = PhotoImage(file=fileImg)
        temp[fileImg] = img
        img = gameWindow.create_image(-330, -330, image=img, anchor='nw')

        # If the mouse is in the game window then the piece follow the mouse
        if not x > 830 or x < 30 or y > 830 or y < 30:
            game.updateGridTk(gameWindow)
            x = int((event.x - game.offsetX) / sizeCells)
            y = int((event.y - game.offsetY) / sizeCells)
            gameWindow.coords(img, x * 40 - 50, y * 40 - 50)
    except:
        random = True


# Display all the available pieces of the current player
def availablePiecesDisplay():
    global information
    oX = 60
    oY = 300
    space = 10

    # Create or replace the information window
    information = Canvas(window, width=658, height=860)
    information.grid(row=0, column=1)

    # Display some information in the information window
    printInformation(text)

    # Button to give up or to say that the player is stuck
    lose = Button(information, text='Stuck player', font=150, height=2, width=40, command=playerStuck)
    lose.place(x=145, y=240)

    # Loop to show all the buttons related to the pieces
    for i in range(5):
        for j in range(5):

            # Format the display of the button
            if i < 4 or (i == 4 and j == 2):
                if i * 5 + j + 1 <= 20:
                    num = i * 5 + j + 1
                else:
                    num = 21

                # If the piece is not used then display it
                if num in player.namePieceList:
                    fileImg = player.namePieceListImg[num]
                    img = PhotoImage(file=fileImg)
                    temp[fileImg] = img
                    information.create_image(oX + (100 + space) * j, oY + (100 + space) * i, image=img, anchor='nw')
                    btn = Button(information, image=img, command=partial(selectionPiece, num))
                    btn.place(x=oX + (100 + space) * j, y=oY + (100 + space) * i)


# Changes the piece when we select a piece button
def selectionPiece(num):
    global piece
    global text
    piece = num
    printInformation(text=num)
    availablePiecesDisplay()


# Display information when the function is called
def printInformation(text):
    information.delete('all')
    information.create_text(329, 80, text='Information related to the current game', font=150)
    information.create_text(329, 120, text=text, font=150)


# When the player is stuck and clicked on the button
def playerStuck():
    player.surrend = True
    nextPlayer()


# End the game and save current information
def endGame():
    saveGameBoard(game.arrayGrid)
    saveGamePieces(player1.namePieceList, player1.color)
    saveGamePieces(player2.namePieceList, player2.color)
    saveGamePieces(player3.namePieceList, player3.color)
    saveGamePieces(player4.namePieceList, player4.color)
    saveDataTour(player.color)
    window.destroy()


piece = 1
numberCells = 20
sizeCells = 40
offsetX = 30
offsetY = 30

text = ''

temp = {}

mainCount = 0

# Start the game
start()

# Loop of the game
window.mainloop()
