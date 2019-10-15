from Grid import Grid
from random import randint, seed

class PlayerAI:
    def __init__(self, grid: Grid):
        seed()
        self.grid = grid

    def getBestMove(self):
        moves = self.grid.getAvailableMoves()
        l = len(moves)
        # TODO
        return moves[randint(0, l-1)]