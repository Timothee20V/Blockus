def saveGameBoard(plateau):
    with open("save/save_plateau", "w") as file:
        for ligne in range(len(plateau)):
            for colonne in plateau[ligne]:
                file.writelines(colonne)
                file.write(" ")
            file.write("\n")

def saveGamePieces(grillePiece,color):
    if(color=='Red'):
        fileName = "save/save_piecesR"
    elif(color=='Green'):
        fileName = "save/save_piecesG"
    elif(color=='Blue'):
        fileName = "save/save_piecesB"
    elif(color=='Yellow'):
        fileName = "save/save_piecesY"

    with open(fileName, "w") as file:
        for i in range(len(grillePiece)):
            file.write(str(i+1)+" "+grillePiece.get(i+1))
            file.write("\n")

             

def loadGameBoard():
    returnplateau = []
    with open("save/save_plateau", "r") as file:
        for line in file:
            returnplateau.append(line.strip().split(' '))
    return returnplateau

def loadGamePiece(color):
    returnpiece = {}

    if(color=='Red'):
        fileName = "save/save_piecesR"
    elif(color=='Green'):
        fileName = "save/save_piecesG"
    elif(color=='Blue'):
        fileName = "save/save_piecesB"
    elif(color=='Yellow'):
        fileName = "save/save_piecesY"

    with open(fileName, "r") as file:
        for line in file:
            returnpiece.update({int(line.split(" ")[0]):line.split(" ")[1].strip()})
    return returnpiece