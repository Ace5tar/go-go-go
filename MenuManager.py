"""
Belle Biery
MM/DD/YY
--Description--
--Sources--
"""

from tkinter import *
from GridCanavs import GridCanvas
from JsonParser import JsonParser


class MenuManager:

    def __init__(self, root):
        self.root = root
        self.frames = []
        self.curMenu = None
        self.setMenu(MainMenu)


    def setMenu(self, menu):
        newMenu = menu(self, self.root)
        if self.curMenu != None: self.curMenu.destroy()
        self.curMenu = newMenu
        self.curMenu.pack()


class MainMenu(Frame):

    def __init__(self, manager, root):
        super().__init__(root)
        Label(self, text="Main Menu").pack()
        Button(self, text="Play", command=lambda: manager.setMenu(SizeSelection)).pack()

class SizeSelection(Frame):

    def __init__(self, manager, root):
        self.manager = manager
        super().__init__(root)
        Label(self, text="Size Selection").pack()
        Button(self, text="9x9", command=lambda: self.selectSize(9)).pack()
        Button(self, text="13x13", command=lambda: self.selectSize(13)).pack()
        Button(self, text="17x17", command=lambda: self.selectSize(17)).pack()
        Button(self, text="Back", command=lambda: manager.setMenu(MainMenu)).pack()    

    def selectSize(self, size):
        gameData = JsonParser("GameData.json")
        gameData["boardSize"] = size
        self.manager.setMenu(MainGameplay)



class MainGameplay(Frame):

    def __init__(self, manager, root):
        gameData = JsonParser("GameData.json")
        super().__init__(root)
        Label(self, text="Main Gameplay").pack() 
        gc = GridCanvas(self, (400, 400), gameData['boardSize'])
        gc.pack()
        Button(self, text="Back", command=lambda: manager.setMenu(SizeSelection)).pack()