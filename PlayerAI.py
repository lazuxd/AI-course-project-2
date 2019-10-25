from typing import Tuple
from sys import maxsize as MAX_INT
from Grid import Grid

def maximize(state: Grid, a: int, b: int) -> Tuple[Grid, int]:
    (maxChild, maxUtility) = (None, -1)

    if state.isTerminal():
        return (state, state.utility())
    
    for child in state.getChildren(who = "max"):
        grid = Grid(matrix=state.getMatrix())
        grid.move(child)
        (_, utility) = minimize(grid, a, b)
        if utility > maxUtility:
            (maxChild, maxUtility) = (child, utility)
        if maxUtility >= b:
            break
        if maxUtility > a:
            a = maxUtility

    return (maxChild, maxUtility)

def minimize(state: Grid, a: int, b: int) -> Tuple[Grid, int]:
    (minChild, minUtility) = (None, MAX_INT)

    if state.isTerminal():
        return (state, state.utility())
    
    for child in state.getChildren(who = "min"):
        grid = Grid(matrix=state.getMatrix())
        grid.placeTile(child[2], child[0], child[1])
        (_, utility) = maximize(grid, a, b)
        if utility < minUtility:
            (minChild, minUtility) = (child, utility)
        if minUtility <= a:
            break
        if minUtility < b:
            b = minUtility

    return (minChild, minUtility)

class PlayerAI:
    def __init__(self, grid: Grid):
        self.grid = grid

    def getBestMove(self) -> int:
        (child, _) = maximize(Grid(matrix=self.grid.getMatrix()), -1, MAX_INT)
        return self.grid.getMoveTo(child)
    