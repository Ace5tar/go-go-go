"""
Belle Biery
MM/DD/YY
--Description--
--Sources--
"""

from tkinter import *

class GridCanvas(Canvas):

    def __init__(self, root, size, gridSize):
        self.width = size[0]
        self.height = size[1]
        super().__init__(root, width=self.width, height=self.height)
        self.drawGameLines(gridSize)

    def drawGameLines(self, numLines):
        lineWidth = self.width/numLines
        lineHeight = self.height/numLines
        for l in range(numLines):
            self.create_line((lineWidth/2) + (lineWidth * l),
                             0,
                             (lineWidth/2) + (lineWidth * l),
                             self.height)
        for l in range(numLines):
            self.create_line(0,
                             (lineHeight/2) + (lineHeight * l),
                             self.height,
                             (lineHeight/2) + (lineHeight * l))
        