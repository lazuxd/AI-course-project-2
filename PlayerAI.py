from typing import Tuple
from sys import maxsize as MAX_INT
from Grid import Grid

def maximize(state: Grid, a: int, b: int) -> Tuple[Grid, int]:
    ''# TODO
    return (state, 1)

def minimize(state: Grid, a: int, b: int) -> Tuple[Grid, int]:
    ''# TODO
    return (state, 1)

class PlayerAI:
    def __init__(self, grid: Grid):
        self.grid = grid

    def getBestMove(self) -> int:
        (child, _) = maximize(Grid(matrix=self.grid.getMatrix()), -1, MAX_INT)
        return self.grid.getMoveTo(child)
    