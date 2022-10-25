class Joueur:

    def __init__(self,couleur,pieces):
        self.couleur = couleur
        self.pieces = pieces

    def creationPieces (self):
        nom_Piece_Liste = ["pieces/piece1","pieces/piece2","pieces/piece3","pieces/piece4","pieces/piece5","pieces/piece6","pieces/piece7",
        "pieces/piece8","pieces/piece9","pieces/piece10","pieces/piece11","pieces/piece12","pieces/piece13","pieces/piece14","pieces/piece15",
        "pieces/piece16","pieces/piece17","pieces/piece18","pieces/piece19","pieces/piece20","pieces/piece21"]
        piece_Select = []
        with open(nom_Piece_Liste[self.pieces-1], "r") as f:
            for ligne in f:
                piece_Select.append(ligne.strip().split(' '))
        return piece_Select

tableau = Joueur("bleu",2)
print(tableau.creationPieces())