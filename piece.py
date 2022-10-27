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

        # référencement des pièces disponibles
       
        piece_Selectionnee_Model = []
        # lecture du fichier choisit et récupération du modèle
        for piece_Numero in range(1,22):
            with open(self.nom_Piece_Liste[piece_Numero], "r") as f:
                for ligne in f:
                    piece_Selectionnee_Model.append(ligne.strip().split(' '))
                    #change les 1 en RJVB
                if(self.couleur == "Bleu"):
                    for longueur in range(0,len(piece_Selectionnee_Model)):
                        for largeur in range(0,len(piece_Selectionnee_Model[longueur])):
                            if ( piece_Selectionnee_Model[longueur][largeur] == "1"):
                                piece_Selectionnee_Model[longueur][largeur] = "B"                                
                elif(self.couleur == "Rouge"):
                    for longueur in range(0,len(piece_Selectionnee_Model)):
                        for largeur in range(0,len(piece_Selectionnee_Model[longueur])):
                            if ( piece_Selectionnee_Model[longueur][largeur] == "1"):
                                    piece_Selectionnee_Model[longueur][largeur] = "R"
                elif(self.couleur == "Jaune"):
                    for longueur in range(0,len(piece_Selectionnee_Model)):
                        for largeur in range(0,len(piece_Selectionnee_Model[longueur])):
                            if( piece_Selectionnee_Model[longueur][largeur] == "1"):
                                    piece_Selectionnee_Model[longueur][largeur] = "J" 
                elif(self.couleur == "Vert"):
                    for longueur in range(0,len(piece_Selectionnee_Model)):
                        for largeur in range(0,len(piece_Selectionnee_Model[longueur])):
                            if ( piece_Selectionnee_Model[longueur][largeur] == "1"):
                                    piece_Selectionnee_Model[longueur][largeur] = "V"
                self.pieces.append(piece_Selectionnee_Model)
                piece_Selectionnee_Model = []

    # retourne le contenu du dictionnaire
    def suppression_Piece(self,numero_Piece):
        return self.pieces[numero_Piece]

    # suppression de la pièce utilisé
    def restePieces(self, piece_Utilisée):
        del self.nom_Piece_Liste[piece_Utilisée]
        #print(self.nom_Piece_Liste)

    # change le sens de la piece
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
        piecesEnCoord = []
        for i in range(0, len(self.pieces)):
            laPiece = []
            for x in range(0, len(self.pieces[i])):
                for y in range(0, len(self.pieces[i])):
                    if self.pieces[i][x][y] == '1':
                        coord = x, y
                        laPiece.append(coord)
            piecesEnCoord.append(laPiece)
        return piecesEnCoord

Bleu = Joueur("Bleu")
print(Bleu.pieces)


