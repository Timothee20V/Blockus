class Joueur:
    # initialisation des paramètres
    def __init__(self, couleur):
        self.couleur = couleur
        self.nom_Piece_Liste = {1: "pieces/piece1", 2: "pieces/piece2", 3: "pieces/piece3", 4: "pieces/piece4",
                                5: "pieces/piece5", 6: "pieces/piece6", 7: "pieces/piece7",
                                8: "pieces/piece8", 9: "pieces/piece9", 10: "pieces/piece10", 11: "pieces/piece11",
                                12: "pieces/piece12", 13: "pieces/piece13", 14: "pieces/piece14", 15: "pieces/piece15",
                                16: "pieces/piece16", 17: "pieces/piece17", 18: "pieces/piece18", 19: "pieces/piece19",
                                20: "pieces/piece20", 21: "pieces/piece21"}
        self.pieces = []
        self.piecesCoord = []

    # retourne le contenu du dictionnaire
    def retourDictionnaire(self):
        return self.nom_Piece_Liste

    # suppression de la pièce utilisé
    def restePieces(self, piece_Utilisée):
        del self.nom_Piece_Liste[piece_Utilisée]
        print(self.nom_Piece_Liste)

    def couleurEquipe(self, piece_Selectionnee):
        if (self == "Bleu"):
            for longueur in range(5):
                for largeur in range(5):
                    if (piece_Selectionnee[longueur][largeur] == 1):
                        piece_Selectionnee[longueur][largeur] = "B"
        elif (self == "Rouge"):
            for longueur in range(5):
                for largeur in range(5):
                    if (piece_Selectionnee[longueur][largeur] == 1):
                        piece_Selectionnee[longueur][largeur] = "R"
        elif (self == "Jaune"):
            for longueur in range(5):
                for largeur in range(5):
                    if (piece_Selectionnee[longueur][largeur] == 1):
                        piece_Selectionnee[longueur][largeur] = "J"
        elif (self == "Vert"):
            for longueur in range(5):
                for largeur in range(5):
                    if (piece_Selectionnee[longueur][largeur] == 1):
                        piece_Selectionnee[longueur][largeur] = "V"
        return piece_Selectionnee

    # récupération du modèle de la pièce et suppression de celle-ci dans le tableau
    def creationPieces(self, piece_Numero):
        # référencement des pièces disponibles
        piece_Selectionnee_Model = []
        # lecture du fichier choisit et récupération du modèle
        with open(self.nom_Piece_Liste[piece_Numero], "r") as f:
            for ligne in f:
                piece_Selectionnee_Model.append(ligne.strip().split(' '))
            # suppression de la pièce dans la liste des pièces restantes
            self.restePieces(piece_Numero)
            piece_Selectionnee_Model = self.couleurEquipe(piece_Selectionnee_Model)
            self.pieces.append(piece_Selectionnee_Model)

    def rotation_Pieces(self, piece_Selectionnee, rotation):
        piece_Retournee = piece_Selectionnee
        if (rotation == "Gauche"):
            for longueur in range(5):
                for largeur in range(5):
                    piece_Retournee[longueur][largeur] = piece_Selectionnee[5 - largeur - 1][longueur]
        elif (rotation == "Droite"):
            for longueur in range(len(piece_Retournee)):
                for largeur in range(len(piece_Retournee[longueur])):
                    piece_Retournee[longueur][largeur] = piece_Selectionnee[5 - largeur - 1][longueur]
        return piece_Retournee

    def pieceEnCoord(self):
        for i in len(self.nom_Piece_Liste):
            for x in len(self.pieces[0]):
                for y in len(self.pieces[0]):
                    self.piecesCoord.append()


Bleu = Joueur("Bleu")
print(Bleu.creationPieces(5))
