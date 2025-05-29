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
        self.gameData["currentTurn"] = "b"
        self.boardSize = self.gameData["boardSize"]
        self.whiteCaptures = 0
        self.blackCaptures = 0
        self.whiteScore = 0
        self.blackScore = 0
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

    def passMove(self):
        if self.passed:
            if (
                self.whiteCaptures + self.whiteScore
                > self.blackCaptures + self.blackScore
            ):
                self.gameData["winner"] = "w"
            elif (
                self.whiteCaptures + self.whiteScore
                < self.blackCaptures + self.blackScore
            ):
                self.gameData["winner"] = "b"
            else:
                self.gameData["winner"] = "d"
            return "GAMEOVER"
        self.gameData["currentTurn"] = (
            "b" if self.gameData["currentTurn"] == "w" else "w"
        )
        self.passed = True

    def playMove(self, cellPos):
        self.passed = False
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
                self.whiteCaptures += boardState.captures["w"]
                self.whiteScore = boardState.scores["w"]
                self.blackCaptures += boardState.captures["b"]
                self.blackScore = boardState.scores["b"]
                if self.blackScore > (self.boardSize * self.boardSize) / 2:
                    self.blackScore = 0

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
