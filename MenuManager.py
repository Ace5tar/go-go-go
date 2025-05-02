"""
Belle Biery
MM/DD/YY
--Description--
--Sources--
"""

from tkinter import *


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
        super().__init__(root)
        Label(self, text="Size Selection").pack()
        Button(self, text="Continue", command=lambda: manager.setMenu(MainGameplay)).pack()
        Button(self, text="Back", command=lambda: manager.setMenu(MainMenu)).pack()    



class MainGameplay(Frame):

    def __init__(self, manager, root):
        super().__init__(root)
        Label(self, text="Main Gameplay").pack()    
        Button(self, text="Back", command=lambda: manager.setMenu(SizeSelection)).pack()