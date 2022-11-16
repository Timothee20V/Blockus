class Joueur:
    # initialisation des paramètres
    def __init__(self, couleur):
        self.couleur = couleur
        self.piecesMain = [i for i in range(1, 22)]

    # suppression de la pièce utilisé
    def restePieces(self, pieceUtilisée):
        self.piecesMain[pieceUtilisée - 1] = 0

    # récupération du modèle de la pièce et suppression de celle-ci dans le tableau
    def creationPieces(self, pieceNumero):
        # référencement des pièces disponibles
        nomPieceListe = ["pieces/piece1", "pieces/piece2", "pieces/piece3", "pieces/piece4", "pieces/piece5",
                         "pieces/piece6", "pieces/piece7", "pieces/piece8", "pieces/piece9", "pieces/piece10",
                         "pieces/piece11", "pieces/piece12", "pieces/piece13", "pieces/piece14", "pieces/piece15",
                         "pieces/piece16", "pieces/piece17", "pieces/piece18", "pieces/piece19", "pieces/piece20",
                         "pieces/piece21"]
        pieceSelect = []

        # lecture du fichier choisit et récupération du modèle
        with open(nomPieceListe[pieceNumero - 1], "r") as f:
            for ligne in f:
                pieceSelect.append(ligne.strip().split(' '))
            # suppression de la pièce dans la liste des pièces restantes
            self.restePieces(pieceNumero)
        return pieceSelect
