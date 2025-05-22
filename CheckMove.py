"""
Belle Biery
MM/DD/YY
--Description--
--Sources--
"""

from copy import deepcopy


class CheckMove:

    directions = [
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1),
    ]

    def __init__(self, boardState):
        self.scores = {"b": 0, "w": 0}
        self.captures = {"b": 0, "w": 0}
        self.legalMove = True
        self.board = boardState
        self.newBoard = deepcopy(self.board)
        self.testBoard = deepcopy(self.board)
        self.visitedCells = []
        self.similarCells = []
        self.checkBoard()

    def checkBoard(self):
        for row, r in enumerate(self.board):
            for col, c in enumerate(r):
                # self.newBoard[row][col].value = "b"
                if (row, col) not in self.visitedCells:
                    self.similarCells = []
                    self.surroundingColor = ""
                    self.checkCell((row, col), c.value)
                    if self.surroundingColor != None:
                        if c.value == "e":
                            self.scores[self.surroundingColor] += len(self.similarCells)
                        elif self.surroundingColor != "e":
                            for c2 in self.similarCells:
                                self.newBoard[c2[0]][c2[1]].value = "e"
                                self.captures[self.surroundingColor] += 1

    def checkCell(self, cellPos, initCell):
        self.visitedCells.append(cellPos)
        if self.getCell(cellPos) == initCell:
            self.similarCells.append(cellPos)
        for dir in CheckMove.directions:
            try:
                nextCellPos = (cellPos[0] + dir[0], cellPos[1] + dir[1])
                nextCell = self.getCell(nextCellPos)

                if nextCell == initCell:
                    if nextCellPos not in self.visitedCells:
                        self.checkCell(nextCellPos, initCell)
                elif self.surroundingColor == "":
                    self.surroundingColor = nextCell
                elif nextCell != self.surroundingColor:
                    self.surroundingColor = None
            except IndexError:
                None

    def getCell(self, cellPos):
        return self.board[cellPos[0]][cellPos[1]].value
