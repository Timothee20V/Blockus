def saveGameBoard(plateau):
    fileName = "save/save_plateau.txt"
    with open(fileName, "w") as file:
        for ligne in range(len(plateau)):
            for colonne in plateau[ligne]:
                file.writelines(str(colonne))
                file.write(" ")
            file.write("\n")
    file.close()
        
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
        for key,value in grillePiece.items():
            file.write(str(key)+" "+value)
            file.write("\n")
    file.close()

def saveDataTour(counter):
    fileName = "save/save_otherData.txt"
    with open(fileName, "w") as file:
        file.write(str(counter))
    file.close()


def loadGameBoard():
    returnplateau = []
    with open("save/save_plateau.txt", "r") as file:
        for line in file:
            data = line.strip().split(' ')
            returnplateau.append(data)
    file.close()        
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
    file.close()
    return returnpiece

def loadDataCounter():
    returnData=[]
    with open("save/save_otherData.txt", "r") as file:
        for line in file:
            file.close()
            return int(line)