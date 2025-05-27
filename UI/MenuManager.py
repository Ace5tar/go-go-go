"""
Belle Biery
MM/DD/YY
--Description--
https://stackoverflow.com/questions/13148975/tkinter-label-does-not-show-image
"""

from tkinter import *
from UI.GridCanavs import GridCanvas
from util.JsonParser import JsonParser
from BoardSim.PlayBoard import PlayBoard


class MenuManager:

    def __init__(self, root):
        self.root = root
        self.frames = []
        self.curMenu = None
        self.setMenu(MainMenu)

    def setMenu(self, menu):
        newMenu = menu(self, self.root)
        if self.curMenu != None:
            self.curMenu.destroy()
        self.curMenu = newMenu
        self.curMenu.pack()


class MainMenu(Frame):

    def __init__(self, manager, root):
        super().__init__(root)
        # images must be assigned to instance variable to prevent garbage collection from deleting it
        self.logo = PhotoImage(file="logo.png")
        Label(self, image=self.logo).pack()
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

    def selectSize(self, size):
        gameData = JsonParser("GameData.json")
        gameData["boardSize"] = size
        self.manager.setMenu(MainGameplay)


class MainGameplay(Frame):

    def __init__(self, manager, root):
        super().__init__(root)
        Label(self, text="Main Gameplay").pack()
        self.pb = PlayBoard()
        self.gc = GridCanvas(self, (400, 400))
        self.gc.pack()
        self.gc.drawBoard(self.pb)
        self.gc.bind("<Button-1>", self.playMove)
        self.gc.bind("<Motion>", self.previewMove)
        Button(self, text="Back", command=lambda: manager.setMenu(SizeSelection)).pack()

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

    def playMove(self, event):
        legalMove = self.pb.playMove(self.gc.canvasToCellPos((event.x, event.y)))
        if legalMove:
            self.gc.drawBoard(self.pb)
