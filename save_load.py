# Save the current plate (the grid of the game)
def saveGameBoard(plate):
    fileName = "save/save_plateau.txt"
    with open(fileName, "w") as file:
        file.truncate(0)
        for ligne in range(len(plate)):
            for colonne in plate[ligne]:
                file.writelines(str(colonne))
                file.write(" ")
            file.write("\n")
    file.close()


# Save non-used pieces
def saveGamePieces(grillePiece, color):
    if color == "red":
        fileName = "save/save_piecesR.txt"
    elif color == "green":
        fileName = "save/save_piecesG.txt"
    elif color == "blue":
        fileName = "save/save_piecesB.txt"
    elif color == "yellow":
        fileName = "save/save_piecesY.txt"

    with open(fileName, "w") as file:
        file.truncate(0)
        for key, value in grillePiece.items():
            file.write(str(key) + " " + value)
            file.write("\n")
    file.close()


# Save the player turn
def saveDataTour(player):
    fileName = "save/save_otherData.txt"
    with open(fileName, "w") as file:
        file.truncate(0)
        file.write(str(player))
    file.close()


# Load the current plate (the grid of the game)
def loadGameBoard():
    returnplateau = []
    with open("save/save_plateau.txt", "r") as file:
        for line in file:
            data = line.strip().split(' ')
            returnplateau.append(data)

    file.close()
    return returnplateau


# Load non-used pieces
def loadGamePiece(color):
    returnpiece = {}

    if color == "red":
        fileName = "save/save_piecesR.txt"
    elif color == "green":
        fileName = "save/save_piecesG.txt"
    elif color == "blue":
        fileName = "save/save_piecesB.txt"
    elif color == "yellow":
        fileName = "save/save_piecesY.txt"

    with open(fileName, "r") as file:
        for line in file:
            returnpiece.update({int(line.split(" ")[0]): line.split(" ")[1].strip()})
    file.close()
    return returnpiece


# Load the player turn
def loadDataCounter():
    with open("save/save_otherData.txt", "r") as file:
        for line in file:
            file.close()
            return line
