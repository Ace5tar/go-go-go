"""
Belle Biery
MM/DD/YY
--Description--
--Sources--
"""

from tkinter import *
from util.JsonParser import JsonParser
from math import floor


class GridCanvas(Canvas):

    def __init__(self, root, size):
        self.gameData = JsonParser("GameData.json")
        self.gridSize = self.gameData["boardSize"]
        self.width = size[0]
        self.height = size[1]
        super().__init__(root, width=self.width, height=self.height)
        self.create_rectangle(0, 0, self.width, self.height, fill="Tan")
        self.drawGameLines(self.gridSize)

    def drawGameLines(self, numLines):
        lineWidth = self.width / numLines
        lineHeight = self.height / numLines
        for l in range(numLines):
            self.create_line(
                (lineWidth / 2) + (lineWidth * l),
                0,
                (lineWidth / 2) + (lineWidth * l),
                self.height,
            )
        for l in range(numLines):
            self.create_line(
                0,
                (lineHeight / 2) + (lineHeight * l),
                self.height,
                (lineHeight / 2) + (lineHeight * l),
            )

        dotSize = 70 / self.gridSize
        for r in range(numLines):
            for c in range(numLines):
                dotPos = self.cellToCanvasPos((r, c))
                xpos = dotPos[0]
                ypos = dotPos[1]
                self.create_oval(
                    xpos + dotSize / 2,
                    ypos - dotSize / 2,
                    xpos - dotSize / 2,
                    ypos + dotSize / 2,
                    fill="Black",
                )

    def drawBoard(self, playBoard):
        stoneSize = 250 / self.gridSize
        for rownum, row in enumerate(playBoard.board):
            for colnum, cell in enumerate(row):
                cellPos = self.cellToCanvasPos((rownum, colnum))
                xpos = cellPos[0]
                ypos = cellPos[1]
                self.delete(f"({rownum}, {colnum})")
                if cell.value != "e":
                    self.create_oval(
                        xpos + stoneSize / 2,
                        ypos - stoneSize / 2,
                        xpos - stoneSize / 2,
                        ypos + stoneSize / 2,
                        fill="White" if cell.value == "w" else "Black",
                        tags=[f"({rownum}, {colnum})"],
                    )

    def cellToCanvasPos(self, cellPos):
        stonexDist = self.width / self.gridSize
        stoneyDist = self.width / self.gridSize
        xpos = stonexDist * cellPos[0] + stonexDist / 2
        ypos = stoneyDist * cellPos[1] + stoneyDist / 2
        return (xpos, ypos)

    def canvasToCellPos(self, canvasPos):
        canvasx = canvasPos[0]
        canvasy = canvasPos[1]
        x = floor((canvasx / self.width) * self.gridSize)
        y = floor((canvasy / self.height) * self.gridSize)
        return (x, y)

    def ghostStone(self, cellPos):
        self.delete("Ghost")
        if cellPos == None:
            return
        canvasPos = self.cellToCanvasPos(cellPos)
        xpos = canvasPos[0]
        ypos = canvasPos[1]

        stoneSize = 250 / self.gridSize

        self.create_oval(
            xpos + stoneSize / 2,
            ypos - stoneSize / 2,
            xpos - stoneSize / 2,
            ypos + stoneSize / 2,
            # fill = "White" if self.gameData['currentTurn'] == 'w' else "Grey",
            tags="Ghost",
        )
