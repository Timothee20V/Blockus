class Player:
    # initialisation des paramètres
    def __init__(self, color, initial, grid):
        self.color = color
        self.initial = initial
        self.namePieceList = {1: "pieces/piece1", 2: "pieces/piece2", 3: "pieces/piece3", 4: "pieces/piece4",
                              5: "pieces/piece5", 6: "pieces/piece6", 7: "pieces/piece7", 8: "pieces/piece8",
                              9: "pieces/piece9", 10: "pieces/piece10", 11: "pieces/piece11", 12: "pieces/piece12",
                              13: "pieces/piece13", 14: "pieces/piece14", 15: "pieces/piece15", 16: "pieces/piece16",
                              17: "pieces/piece17", 18: "pieces/piece18", 19: "pieces/piece19", 20: "pieces/piece20",
                              21: "pieces/piece21"
                              }
        self.namePieceListImg = {1: "pieces/{}/piece1.png".format(self.color),
                                 2: "pieces/{}/piece2.png".format(self.color),
                                 3: "pieces/{}/piece3.png".format(self.color),
                                 4: "pieces/{}/piece4.png".format(self.color),
                                 5: "pieces/{}/piece5.png".format(self.color),
                                 6: "pieces/{}/piece6.png".format(self.color),
                                 7: "pieces/{}/piece7.png".format(self.color),
                                 8: "pieces/{}/piece8.png".format(self.color),
                                 9: "pieces/{}/piece9.png".format(self.color),
                                 10: "pieces/{}/piece10.png".format(self.color),
                                 11: "pieces/{}/piece11.png".format(self.color),
                                 12: "pieces/{}/piece12.png".format(self.color),
                                 13: "pieces/{}/piece13.png".format(self.color),
                                 14: "pieces/{}/piece14.png".format(self.color),
                                 15: "pieces/{}/piece15.png".format(self.color),
                                 16: "pieces/{}/piece16.png".format(self.color),
                                 17: "pieces/{}/piece17.png".format(self.color),
                                 18: "pieces/{}/piece18.png".format(self.color),
                                 19: "pieces/{}/piece19.png".format(self.color),
                                 20: "pieces/{}/piece20.png".format(self.color),
                                 21: "pieces/{}/piece21.png".format(self.color)
                                 }

        self.pieces = []
        self.grid = grid
        self.convertTextFiles()
        self.usedPieces = []
        self.surrend = False

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
        self.namePieceList.pop(numPiece)
        self.namePieceListImg.pop(numPiece)



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
        thePiece = self.pieces[pieceSelected - 1]

        returnedPiece = [[thePiece[j][i] for j in range(len(thePiece))] for i in range(len(thePiece[0]) - 1, -1, -1)]

        print("rotation:")
        print(self.pieceToCoord()[pieceSelected - 1])
        self.pieces[pieceSelected - 1] = returnedPiece
        print(self.pieceToCoord()[pieceSelected - 1])

    def symmetryPieces(self, pieceSelected):
        thePiece = self.pieces[pieceSelected - 1]
        theNewPiece = []

        for i in range(len(thePiece)):
            theNewPiece.append(thePiece[len(thePiece) - i - 1])

        print('symétrie:')
        print(self.pieceToCoord()[pieceSelected - 1])
        self.pieces[pieceSelected - 1] = theNewPiece
        print(self.pieceToCoord()[pieceSelected - 1])

    def putPiece(self, num, coord):
        coordX, coordY = coord
        self.usedPieces.append(num)
        piece = self.pieceToCoord()[num]
        print("piece placé:")
        print(piece)
        print(num)
        for i in range(len(piece)):
            pX, pY = piece[i]
            self.grid.arrayGrid[coordX + pX - 2][coordY + pY - 2] = self.initial
