"""
Belle Biery
MM/DD/YY
--Description--
--Sources--
"""

class PlayBoard(list):
    
    def __init__(self, boardSize):
        self.whiteCaptures = 0
        self.blackCaptures = 0
        self.board = [[Cell() for i in range(boardSize)] for j in range(boardSize)]

    def __repr__(self):
        return '\n'.join([' '.join([cell.value for cell in row]) for row in self.board])


class Cell:

    def __init__(self):
        self.value = 'e'
        self.animationState = 0

    def __repr__(self):
        return self.value