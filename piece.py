class Joueur:
    #initialisation des paramètres
    def __init__(self,couleur):
        self.couleur = couleur
        self.piecesMain = [i for i in range(1,22)]

    #suppression de la pièce utilisé
    def restePieces(self,piece_Utilisée):
        self.piecesMain[piece_Utilisée-1] = 0

    #récupération du modèle de la pièce et suppression de celle-ci dans le tableau 
    def creationPieces (self,piece_Numero):

        #référencement des pièces disponibles
        nom_Piece_Liste = ["pieces/piece1","pieces/piece2","pieces/piece3","pieces/piece4","pieces/piece5","pieces/piece6","pieces/piece7",
        "pieces/piece8","pieces/piece9","pieces/piece10","pieces/piece11","pieces/piece12","pieces/piece13","pieces/piece14","pieces/piece15",
        "pieces/piece16","pieces/piece17","pieces/piece18","pieces/piece19","pieces/piece20","pieces/piece21"]
        piece_Select = []

        #lecture du fichier choisit et récupération du modèle
        with open(nom_Piece_Liste[piece_Numero-1], "r") as f:
            for ligne in f:
                piece_Select.append(ligne.strip().split(' '))
            #suppression de la pièce dans la liste des pièces restantes
            self.restePieces(piece_Numero) 
        return piece_Selectv