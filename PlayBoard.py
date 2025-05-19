"""
Belle Biery
MM/DD/YY
--Description--
--Sources--
"""

from JsonParser import JsonParser
from random import choice


class PlayBoard(list):

    def __init__(self):
        self.gameData = JsonParser("GameData.json")
        self.boardSize = self.gameData["boardSize"]
        self.whiteCaptures = self.gameData["whiteCaptures"]
        self.blackCaptures = self.gameData["blackCaptures"]
        self.board = [
            [Cell() for i in range(self.boardSize)] for j in range(self.boardSize)
        ]

    def __repr__(self):
        return "\n".join([" ".join([cell.value for cell in row]) for row in self.board])

    # for testing board display
    def randomizeBoard(self):
        for cellrow in self.board:
            for cell in cellrow:
                cell.value = choice(["e", "e", "w", "b"])

    def getCell(self, cellPos):
        try:
            return self.board[cellPos[0]][cellPos[1]]
        except:
            return None

    def playMove(self, cellPos):
        if not self.isLegal(cellPos) or self.getCell(cellPos) == None:
            return False
        self.getCell(cellPos).value = self.gameData["currentTurn"]
        self.gameData["currentTurn"] = (
            "b" if self.gameData["currentTurn"] == "w" else "w"
        )
        return True

    def isLegal(self, cellPos):
        return True


class Cell:

    def __init__(self):
        self.value = "e"
        self.animationState = 0

    def __repr__(self):
        return self.value
