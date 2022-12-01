def saveGame(plateau):
    with open("save", "w") as file:
        for ligne in range(len(plateau)):
            for colonne in plateau[ligne]:
                file.writelines(colonne)
                file.write(" ")
            file.write("\n")
             
def loadGame():
    returnplateau = []
    with open("save", "r") as file:
        for line in file:
            returnplateau.append(line.strip().split(' '))
    return returnplateau
