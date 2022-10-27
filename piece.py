class Joueur:
    # initialisation des paramètres
    def __init__(self, couleur, initiale):
        self.couleur = couleur
        self.initiale = initiale
        self.nom_Piece_Liste = {1: "pieces/piece1", 2: "pieces/piece2", 3: "pieces/piece3", 4: "pieces/piece4",
                                5: "pieces/piece5", 6: "pieces/piece6", 7: "pieces/piece7",
                                8: "pieces/piece8", 9: "pieces/piece9", 10: "pieces/piece10", 11: "pieces/piece11",
                                12: "pieces/piece12", 13: "pieces/piece13", 14: "pieces/piece14", 15: "pieces/piece15",
                                16: "pieces/piece16", 17: "pieces/piece17", 18: "pieces/piece18", 19: "pieces/piece19",
                                20: "pieces/piece20", 21: "pieces/piece21"}
        self.pieces = []

        # référencement des pièces disponibles

        piece_Selectionnee_Model = []
        # lecture du fichier choisit et récupération du modèle
        for piece_Numero in range(1, 22):
            with open(self.nom_Piece_Liste[piece_Numero], "r") as f:
                for ligne in f:
                    piece_Selectionnee_Model.append(ligne.strip().split(' '))
                    # change les 1 en RJVB
                for longueur in range(0, len(piece_Selectionnee_Model)):
                    for largeur in range(0, len(piece_Selectionnee_Model[longueur])):
                        if (piece_Selectionnee_Model[longueur][largeur] == "1"):
                            piece_Selectionnee_Model[longueur][largeur] = self.initiale
                self.pieces.append(piece_Selectionnee_Model)
                piece_Selectionnee_Model = []

    # retourne le contenu du dictionnaire
    def suppression_Piece(self, numero_Piece):
        return self.pieces[numero_Piece]

    def pieceEnCoord(self):
        piecesEnCoord = []

        for i in range(0, len(self.pieces)):
            laPiece = []
            for x in range(0, len(self.pieces[i])):
                for y in range(0, len(self.pieces[i])):
                    if self.pieces[i][x][y] == self.initiale:
                        coord = x, y
                        laPiece.append(coord)
            piecesEnCoord.append(laPiece)

        return piecesEnCoord

        # change le sens de la piece
    def rotation_Pieces(self, piece_Selectionnee):
        laPiece = self.pieces[piece_Selectionnee]

        piece_Retournee = [[laPiece[j][i] for j in range(len(laPiece))] for i in range(len(laPiece[0]) - 1, -1, -1)]

        self.pieces[piece_Selectionnee] = piece_Retournee

    def symetrie_Pieces(self, piece_Selectionnee):
        laPiece = self.pieces[piece_Selectionnee]

        piece_Symetrique = [[laPiece[j][i] for j in range(len(laPiece))] for i in range(len(laPiece[0]) - 1, -1, -1)]

        self.pieces[piece_Selectionnee] = piece_Retournee


Bleu = Joueur("Bleu", "B")
print(Bleu.pieceEnCoord()[5])
Bleu.rotation_Pieces(5)
print(Bleu.pieceEnCoord()[5])
