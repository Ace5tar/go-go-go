"""
Belle Biery
5/29/25
Manage a set of menus and switching between them
https://stackoverflow.com/questions/13148975/tkinter-label-does-not-show-image
"""

from tkinter import *
from UI.GridCanavs import GridCanvas
from util.JsonParser import JsonParser
from BoardSim.PlayBoard import PlayBoard


# Manages the UI and menu switching
class MenuManager:

    def __init__(self, root):
        self.root = root
        self.frames = []
        self.curMenu = None
        # starts on MainMenu
        self.setMenu(MainMenu)

    # sets the menu to menu
    def setMenu(self, menu):
        newMenu = menu(self, self.root)
        if self.curMenu != None:
            self.curMenu.destroy()
        self.curMenu = newMenu
        self.curMenu.pack()


# Main starting menu
class MainMenu(Frame):

    def __init__(self, manager, root):
        super().__init__(root)
        # images must be assigned to instance variable to prevent garbage collection from deleting it
        self.logo = PhotoImage(file="logo.png")
        # Logo image
        Label(self, image=self.logo).pack()
        # Start button
        Button(self, text="Play", command=lambda: manager.setMenu(SizeSelection)).pack()


class SizeSelection(Frame):

    def __init__(self, manager, root):
        self.manager = manager
        super().__init__(root)
        Label(self, text="Size Selection").pack()
        Button(self, text="9x9", command=lambda: self.selectSize(9)).pack()
        Button(self, text="13x13", command=lambda: self.selectSize(13)).pack()
        Button(self, text="19x19", command=lambda: self.selectSize(19)).pack()
        Button(self, text="Back", command=lambda: manager.setMenu(MainMenu)).pack()

    # Updates the selected size
    def selectSize(self, size):
        gameData = JsonParser("GameData.json")
        gameData["boardSize"] = size
        self.manager.setMenu(MainGameplay)


# Main gameplay menu
class MainGameplay(Frame):

    def __init__(self, manager, root):
        super().__init__(root)
        Label(self, text="Main Gameplay").pack()
        self.manager = manager
        self.pb = PlayBoard()
        self.gc = GridCanvas(self, (400, 400))
        self.gc.pack()
        self.gc.drawBoard(self.pb)
        self.gc.bind("<Button-1>", self.playMove)
        self.gc.bind("<Motion>", self.previewMove)
        self.whiteScore = Label(self, text="White: 0")
        self.whiteScore.pack()
        self.blackScore = Label(self, text="Black: 0")
        self.blackScore.pack()
        Button(self, text="Pass", command=self.passMove).pack()

    # tells canvas to draw preview stone at the mouse cursor
    def previewMove(self, event):
        cellPos = self.gc.canvasToCellPos((event.x, event.y))
        try:
            cellValue = self.pb.getCell(cellPos).value
        except:
            cellValue = None
        if cellValue == "e":
            self.gc.ghostStone(cellPos)
        else:
            self.gc.ghostStone(None)

    # tells playboard to pass
    def passMove(self):
        if self.pb.passMove():
            self.manager.setMenu(GameOver)

    # tells playboard to playmove and then updates the ui
    def playMove(self, event):
        legalMove = self.pb.playMove(self.gc.canvasToCellPos((event.x, event.y)))
        if legalMove:
            self.gc.drawBoard(self.pb)
            self.whiteScore.config(
                text=f"White: {self.pb.whiteCaptures + self.pb.whiteScore}"
            )
            self.blackScore.config(
                text=f"Black: {self.pb.blackCaptures + self.pb.blackScore}"
            )


# game over screen
class GameOver(Frame):

    def __init__(self, manager, root):
        winner = JsonParser("GameData.json")["winner"]
        self.manager = manager
        super().__init__(root)
        if winner == "w":
            Label(self, text="White Wins!").pack()
        elif winner == "b":
            Label(self, text="Black Wins!").pack()
        else:
            Label(self, text="It's a draw!").pack()
        Button(
            self, text="New Game", command=lambda: manager.setMenu(SizeSelection)
        ).pack()
