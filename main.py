from grid import *
from piece import *
from tkinter import *

jeu = Grid(100, 30, 40, [])

game = Canvas(window, width=1000, height=860)

jeu.creationGrid(game, numberCases)

game.grid(row=0, column=0)
game.create_rectangle(100, 30, 900, 830)

informations = Canvas(window, width=528, height=860)
informations.grid(row=0, column=1)

window.bind('<Escape>', lambda e: window.destroy())

window.mainloop()