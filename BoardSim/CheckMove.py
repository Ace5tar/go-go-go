"""
Belle Biery
5/29/25
Takes a board and updates all of the stones that need to be removed
"""

from copy import deepcopy


# class to check the results of a certain move if it was made
class CheckMove:

    # cardinal directions
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

    # runs through board positions and runs a flood fill algorithm for each one
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
                                self.scores[self.surroundingColor] += 1

    # recursive function - checks neighboring cells and if they are the same calls this function again
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
