class Joueur:
    #initialisation des paramètres
    def __init__(self,couleur):
        self.couleur = couleur
        self.nom_Piece_Liste = {1:"pieces/piece1",2:"pieces/piece2",3:"pieces/piece3",4:"pieces/piece4",5:"pieces/piece5",6:"pieces/piece6",7:"pieces/piece7",
        8:"pieces/piece8",9:"pieces/piece9",10:"pieces/piece10",11:"pieces/piece11",12:"pieces/piece12",13:"pieces/piece13",14:"pieces/piece14",15:"pieces/piece15",
        16:"pieces/piece16",17:"pieces/piece17",18:"pieces/piece18",19:"pieces/piece19",20:"pieces/piece20",21:"pieces/piece21"}

    #retourne le contenu du dictionnaire
    def retourDictionnaire(self):
        return self.nom_Piece_Liste

    #suppression de la pièce utilisé
    def restePieces(self,piece_Utilisée):
        del self.nom_Piece_Liste[piece_Utilisée]
        print(self.nom_Piece_Liste)

    #récupération du modèle de la pièce et suppression de celle-ci dans le tableau 
    def creationPieces (self,piece_Numero):

        #référencement des pièces disponibles
        piece_Select = []

        #lecture du fichier choisit et récupération du modèle
        with open(self.nom_Piece_Liste[piece_Numero], "r") as f:
            for ligne in f:
                piece_Select.append(ligne.strip().split(' '))
            #suppression de la pièce dans la liste des pièces restantes
            self.restePieces(piece_Numero) 
        return piece_Select

bleu = Joueur("bleu")
rouge = Joueur("rouge")
print(bleu.retourDictionnaire())