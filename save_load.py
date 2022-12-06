def saveGame(plateau):
    with open("save", "w") as file:
        file.write("Plateau")
        file.write("\n")
        for ligne in range(len(plateau)):
            for colonne in plateau[ligne]:
                file.writelines(colonne)
                file.write(" ")
            file.write("\n")
        file.write("\n")
        file.write("Piece")

             
def loadGameBoard():
    returnplateau = []
    with open("save", "r") as file:
        for i in file:
            if(i=="PLateau"):
                for line in i:
                    returnplateau.append(line.strip().split(' '))
    return returnplateau

def loadGamePiece():
    returnpiece = {}
    with open("save", "r") as file:
        for i in file:
            while(i=="Piece"):
                for line in i:
                    returnpiece.append(line.strip().split(' '))
    return returnpiece

ref_couleur = ['rouge','jaune','vert','bleu','orange','blanc','violet','fuchsia']
saveGame(ref_couleur)
print(loadGameBoard())