"""
Belle Biery
MM/DD/YY
--Description--
--Sources--
"""

from tkinter import *
from UI.MenuManager import MenuManager
from BoardSim.PlayBoard import PlayBoard
import sys

sys.setrecursionlimit(10000)

root = Tk()
root.minsize(1080, 720)

mm = MenuManager(root)

root.mainloop()
