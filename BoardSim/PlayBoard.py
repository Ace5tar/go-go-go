"""
Belle Biery
MM/DD/YY
--Description--
--Sources--
"""

from util.JsonParser import JsonParser
from random import choice
from copy import deepcopy
from BoardSim.CheckMove import CheckMove


class PlayBoard(list):

    def __init__(self):
        self.gameData = JsonParser("GameData.json")
        self.boardSize = self.gameData["boardSize"]
        self.whiteCaptures = self.gameData["whiteCaptures"]
        self.blackCaptures = self.gameData["blackCaptures"]
        self.board = [
            [Cell() for i in range(self.boardSize)] for j in range(self.boardSize)
        ]
        self.oldBoardStates = []

    def __repr__(self):
        return "\n".join([" ".join([cell.value for cell in row]) for row in self.board])

    def getCell(self, cellPos):
        try:
            return self.board[cellPos[0]][cellPos[1]]
        except:
            return None

    def playMove(self, cellPos):
        if not self.isLegal(cellPos) or self.getCell(cellPos) == None:
            return False
        self.gameData["currentTurn"] = (
            "b" if self.gameData["currentTurn"] == "w" else "w"
        )
        self.oldBoardStates.append(self.board)
        return True

    def isLegal(self, cellPos):
        newBoard = deepcopy(self.board)
        if self.getCell(cellPos).value == "e":
            newBoard[cellPos[0]][cellPos[1]].value = self.gameData["currentTurn"]
            boardState = CheckMove(newBoard)
            if boardState not in self.oldBoardStates:
                self.board = deepcopy(boardState.newBoard)
                return True
            else:
                return False
        else:
            return False


class Cell:

    def __init__(self):
        self.value = "e"
        self.animationState = 0

    def __repr__(self):
        return str(self.value)
