import copy

namePieceList = {1: "pieces/piece1", 2: "pieces/piece2", 3: "pieces/piece3", 4: "pieces/piece4",
                              5: "pieces/piece5", 6: "pieces/piece6", 7: "pieces/piece7", 8: "pieces/piece8",
                              9: "pieces/piece9", 10: "pieces/piece10", 11: "pieces/piece11", 12: "pieces/piece12",
                              13: "pieces/piece13", 14: "pieces/piece14", 15: "pieces/piece15", 16: "pieces/piece16",
                              17: "pieces/piece17", 18: "pieces/piece18", 19: "pieces/piece19", 20: "pieces/piece20",
                              21: "pieces/piece21"
                              }

namePieceList1 = copy.deepcopy(namePieceList)
namePieceList2 = copy.deepcopy(namePieceList)
namePieceList3 = copy.deepcopy(namePieceList)


namePieceList1.pop(1)

print(namePieceList1)
print(namePieceList2)
print(namePieceList3)