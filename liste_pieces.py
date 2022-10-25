class Pieces_reste:
    
    def __init__(self) -> None:
        self.piecesMain = [i for i in range(1,22)]

    def restePieces(self,piece_Utilisée):
        self.piecesMain[piece_Utilisée-1] = 0
        return self.piecesMain