def saveGameBoard(plateau):
    with open("save/save_plateau.txt", "w") as file:
        for ligne in range(len(plateau)):
            for colonne in plateau[ligne]:
                file.writelines(str(colonne))
                file.write(" ")
            file.write("\n")

def saveGamePieces(grillePiece,color):
    if(color=="red"):
        fileName = "save/save_piecesR.txt"
    elif(color=="green"):
        fileName = "save/save_piecesG.txt"
    elif(color=="blue"):
        fileName = "save/save_piecesB.txt"
    elif(color=="yellow"):
        fileName = "save/save_piecesY.txt"

    with open(fileName, "w") as file:
        for i in range(len(grillePiece)):
            file.write(str(i+1)+" "+grillePiece.get(i+1))
            file.write("\n")

def saveDataTour(round,counter):
    with open("save/save_otherData.txt", "w") as file:
        file.write(round)
        file.write("\n")
        file.write(counter)


def loadGameBoard():
    returnplateau = []
    with open("save/save_plateau.txt", "r") as file:
        for line in file:
            returnplateau.append(line.strip().split(' '))
    return returnplateau

def loadGamePiece(color):
    returnpiece = {}

    if(color=="red"):
        fileName = "save/save_piecesR.txt"
    elif(color=="green"):
        fileName = "save/save_piecesG.txt"
    elif(color=="blue"):
        fileName = "save/save_piecesB.txt"
    elif(color=="yellow"):
        fileName = "save/save_piecesY.txt"

    with open(fileName, "r") as file:
        for line in file:
            returnpiece.update({int(line.split(" ")[0]):line.split(" ")[1].strip()})
    return returnpiece

def loadDataRound():
    returnData=[]
    with open("save/save_otherData.txt", "r") as file:
     for line in file:
        returnData.append(int(line.strip()))
    return returnData[0]

def loadDataCounter():
    returnData=[]
    with open("save/save_otherData.txt", "r") as file:
     for line in file:
        returnData.append(int(line.strip()))
    return returnData[1]