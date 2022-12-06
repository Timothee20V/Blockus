import grid as g
import player as p
from tkinter import *


def takeCoord(event):

    global player
    global counter
    informations.delete("all")

    x = int((event.x - jeu.offsetX) / sizeCells)
    y = int((event.y - jeu.offsetY) / sizeCells)
    informations.create_text(329, 230, text=x)
    informations.create_text(329, 240, text=y)

    ##if available(x, y):
    ##    player1.putPiece(piece - 1, (x, y))

    if(counter == 0 and player1.surrend != True):
        player = player1
        counter += 1
    elif(counter == 1 and player2.surrend != True):
        player = player2
        counter +=1
    elif(counter == 2 and player3.surrend != True):
        player = player3
        counter +=1
    elif(counter == 3 and player4.surrend != True):
        player = player4
        counter = 0
        
    if available(x, y):
        player.putPiece(piece - 1, (x, y))

    jeu.updateGridTk(game)
    availablePiecesDisplay()



def modifPiece(event):
    if event.keysym == 'r':

        player.rotationPieces(piece)
    if event.keysym == 's':
        player.symmetryPieces(piece)

def available(x, y):
    
    for cell in player.pieceToCoord()[piece - 1]:
        cellX, cellY = cell
       
        

        if x + cellX - 2 > jeu.numberCells - 1 or \
                y + cellY - 2 > jeu.numberCells - 1 or \
                x + cellX - 2 < 0 or y + cellY - 2 < 0 or \
                jeu.arrayGrid[x + cellX - 2][y + cellY - 2] != 0:
            informations.create_text(329, 250, text='Impossible')
            return False
        if jeu.arrayGrid[x + cellX - 2 - 1][y + cellY - 2 - 0] != 0:
            informations.create_text(329, 250, text='Impossible')
            return False
        if jeu.arrayGrid[x + cellX - 2 + 1][y + cellY - 2 - 0] != 0:
            informations.create_text(329, 250, text='Impossible')
            return False
        if jeu.arrayGrid[x + cellX - 2 - 1][y + cellY - 2 + 0] != 0:
            informations.create_text(329, 250, text='Impossible')
            return False
        if jeu.arrayGrid[x + cellX - 2 + 1][y + cellY - 2 + 0] != 0:
            informations.create_text(329, 250, text='Impossible')
            return False
        if jeu.arrayGrid[x + cellX - 2 - 0][y + cellY - 2 - 1] != 0:
            informations.create_text(329, 250, text='Impossible')
            return False
        if jeu.arrayGrid[x + cellX - 2 + 0][y + cellY - 2 - 1] != 0:
            informations.create_text(329, 250, text='Impossible')
            return False
        if jeu.arrayGrid[x + cellX - 2 - 0][y + cellY - 2 + 1] != 0:
            informations.create_text(329, 250, text='Impossible')
            return False
        if jeu.arrayGrid[x + cellX - 2 + 0][y + cellY - 2 + 1] != 0:
            informations.create_text(329, 250, text='Impossible')
            return False

    return True



def pieceFollowing(event):
    x, y = event.x, event.y

    if x > 830 or x < 30 or y > 830 or y < 30:
        game.coords(mapimg, 330, 330)
    else:
        game.coords(mapimg, x - 100, y - 100)


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

                fileImg = player.namePieceListImg[num]

                img = PhotoImage(file=fileImg)
                temp[fileImg] = img
                informations.create_image(oX + (100 + space) * j, oY + (100 + space) * i, image=img, anchor='nw')






piece = 21
numberCells = 20
sizeCells = 40
turn = 0
offsetX = 30
offsetY = 30

global count 
count = 0

temp = {}

jeu = g.Grid(offsetX, offsetY, sizeCells, [], numberCells)

window = Tk()
window.title("Blokus")
window.attributes('-fullscreen', True)

game = Canvas(window, width=870, height=860)

game.grid(row=0, column=0)
game.create_rectangle(offsetX, offsetY, 830, 830)
game.create_line(871, 0, 871, 860, width=2)

img = PhotoImage(file='images200px/piece21.png')
mapimg = game.create_image(330, 330, image=img, anchor='nw')

informations = Canvas(window, width=658, height=860)
informations.grid(row=0, column=1)

jeu.creationGridTk(game)

player1 = p.Player("blue", "B", jeu)
player2 = p.Player("red", "R", jeu)
player3 = p.Player("yellow", "Y", jeu)
player4 = p.Player("green", "G", jeu)
player = player1
counter = 0


availablePiecesDisplay()

game.bind('<Button-1>', takeCoord)

window.bind('<Escape>', lambda e: window.destroy())
window.bind('<Key>', modifPiece)

game.bind('<Motion>', pieceFollowing)


window.mainloop()
