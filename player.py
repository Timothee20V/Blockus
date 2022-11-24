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
        self.namePieceListImg = {1: "images100px/piece1.png", 2: "images100px/piece2.png",
                                 3: "images100px/piece3.png", 4: "images100px/piece4.png",
                                 5: "images100px/piece5.png", 6: "images100px/piece6.png",
                                 7: "images100px/piece7.png",
                                 8: "images100px/piece8.png", 9: "images100px/piece9.png",
                                 10: "images100px/piece10.png", 11: "images100px/piece11.png",
                                 12: "images100px/piece12.png", 13: "images100px/piece13.png",
                                 14: "images100px/piece14.png", 15: "images100px/piece15.png",
                                 16: "images100px/piece16.png", 17: "images100px/piece17.png",
                                 18: "images100px/piece18.png", 19: "images100px/piece19.png",
                                 20: "images100px/piece20.png", 21: "images100px/piece21.png"}

        self.pieces = []
        self.grid = grid
        self.convertTextFiles()
        self.usedPieces = []

    # Convertion des fichiers textes en une liste de pieces
    def convertTextFiles(self):
        pieceSelectedModel = []

        for pieceNum in range(1, 22):
            with open(self.namePieceList[pieceNum], "r") as f:

                for line in f:
                    pieceSelectedModel.append(line.strip().split(' '))

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
        self.usedPieces.append(num)
        piece = self.pieceToCoord()[num]
        for i in range(len(piece)):
            pX, pY = piece[i]
            self.grid.arrayGrid[coordX + pX - 2][coordY + pY - 2] = self.initial
