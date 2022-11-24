class Player:
    # initialisation des paramètres
    def __init__(self, color, initial, grid):
        self.color = color
        self.initial = initial
        self.namePieceList = {1: "pieces/piece1", 2: "pieces/piece2", 3: "pieces/piece3", 4: "pieces/piece4",
                              5: "pieces/piece5", 6: "pieces/piece6", 7: "pieces/piece7",
                              8: "pieces/piece8", 9: "pieces/piece9", 10: "pieces/piece10", 11: "pieces/piece11",
                              12: "pieces/piece12", 13: "pieces/piece13", 14: "pieces/piece14", 15: "pieces/piece15",
                              16: "pieces/piece16", 17: "pieces/piece17", 18: "pieces/piece18", 19: "pieces/piece19",
                              20: "pieces/piece20", 21: "pieces/piece21"}
        self.pieces = []
        self.grid = grid
        self.convertTextFiles()

    # Convertion des fichiers textes en une liste de pieces
    def convertTextFiles(self):
        pieceSelectedModel = []
        for pieceNum in range(1, 22):
            with open(self.namePieceList[pieceNum], "r") as f:
                for line in f:
                    pieceSelectedModel.append(line.strip().split(' '))
                    # change les 1 en RJVB
                for length in range(0, len(pieceSelectedModel)):
                    for width in range(0, len(pieceSelectedModel[length])):
                        if pieceSelectedModel[length][width] == "1":
                            pieceSelectedModel[length][width] = self.initial
                self.pieces.append(pieceSelectedModel)
                pieceSelectedModel = []

    # retourne le contenu du dictionnaire
    def removePiece(self, numPiece):
        return self.pieces[numPiece]

    def pieceToCoord(self):
        piecesInCoord = []

        for i in range(0, len(self.pieces)):
            thePiece = []
            for x in range(0, len(self.pieces[i])):
                for y in range(0, len(self.pieces[i])):
                    if self.pieces[i][x][y] == self.initial:
                        coord = x, y
                        thePiece.append(coord)
            piecesInCoord.append(thePiece)

        return piecesInCoord

        # change le sens de la piece

    def rotationPieces(self, pieceSelected):
        thePiece = self.pieces[pieceSelected]

        returnedPiece = [[thePiece[j][i] for j in range(len(thePiece))] for i in range(len(thePiece[0]) - 1, -1, -1)]

        self.pieces[pieceSelected] = returnedPiece

    def symmetryPieces(self, pieceSelected):
        thePiece = self.pieces[pieceSelected]
        theNewPiece = []

        for i in range(len(thePiece)):
            theNewPiece.append(thePiece[-i])
        self.pieces[pieceSelected] = theNewPiece

    def putPiece(self, num, coord):
        coordX, coordY = coord
        piece = self.pieceToCoord()[num]
        for i in range(len(piece)):
            pX, pY = piece[i]
            self.grid.arrayGrid[coordX + pX - 2][coordY + pY - 2] = self.initial
        print("piece ajouté au coord:", coordX + pX - 2, coordY + pY - 2)

