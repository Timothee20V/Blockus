


class Grid:
    def __init__(self, x, y, sizeCase, arrayGrid, numberCases):
        self.offsetX = x
        self.offsetY = y
        self.sizeCase = sizeCase
        self.arrayGrid = arrayGrid
        self.numberCases = numberCases

        self.creationArrayGrid(numberCases, arrayGrid)

        window = Tk()
        window.title("Blokus")
        window.attributes('-fullscreen', True)



    def creationGrid(self, game, numberCases):
        for i in range(1, numberCases):
            game.create_line(i * self.sizeCase + self.offsetX,
                             self.offsetY,
                             i * self.sizeCase + self.offsetX,
                             800 + self.offsetY
                             )

        for i in range(1, numberCases):
            game.create_line(self.offsetX,
                             self.offsetY + i * self.sizeCase,
                             self.offsetX + 800,
                             self.offsetY + i * self.sizeCase
                             )

    def creationArrayGrid(self, numberCases, arrayGrid):
        for line in range(numberCases):
            nvline = []
            for col in range(numberCases):
                nvline.append((0))
            arrayGrid.append(nvline)
        self.arrayGrid = arrayGrid

    def arrayGridDisplay(self):
        for line in self.arrayGrid:
            print(' '.join(str(e) for e in line))


"""jeu = Grid(100, 30, 40, [])
jeu.arrayGridDisplay()"""