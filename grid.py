class Grid:
    def __init__(self, x, y, sizeCell, arrayGrid, numberCells):
        self.offsetX = x
        self.offsetY = y
        self.sizeCell = sizeCell
        self.numberCells = numberCells
        self.creationArrayGrid(arrayGrid)

    def creationGridTk(self, game):
        for i in range(1, self.numberCells):
            game.create_line(i * self.sizeCell + self.offsetX,
                             self.offsetY,
                             i * self.sizeCell + self.offsetX,
                             800 + self.offsetY
                             )

        for i in range(1, self.numberCells):
            game.create_line(self.offsetX,
                             self.offsetY + i * self.sizeCell,
                             self.offsetX + 800,
                             self.offsetY + i * self.sizeCell
                             )

    def updateGridTk(self, game):
        game.delete('text')
        for i in range(len(self.arrayGrid)):
            for j in range(len(self.arrayGrid)):
                if self.arrayGrid[i][j] != '0':
                    game.create_text(i * self.sizeCell + self.offsetX + self.sizeCell / 2,
                                     j * self.sizeCell + self.offsetY + self.sizeCell / 2,
                                     text=self.arrayGrid[i][j],
                                     tags="text"
                                     )

    def creationArrayGrid(self, arrayGrid):
        if(arrayGrid==[]):
            for line in range(self.numberCells):
                nvline = []
                for col in range(self.numberCells):
                    nvline.append(('0'))
                arrayGrid.append(nvline)
        self.arrayGrid = arrayGrid

    def arrayGridDisplay(self):
        for i in range(len(self.arrayGrid)):
            for line in self.arrayGrid:
                print(line[i], end=' ')
            print()
