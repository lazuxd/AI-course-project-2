from typing import Tuple
from sys import maxsize as MAX_INT
from Grid import Grid

def maximize(state: Grid, a: int, b: int, d: int) -> Tuple[Grid, int]:
    (maxChild, maxUtility) = (None, -1)

    if d == 0:
        return (None, state.utilityEstimate())
    elif state.isTerminal(who="max"):
        return (None, state.utility())
    
    d -= 1
    
    for child in state.getChildren(who = "max"):
        grid = Grid(matrix=state.getMatrix())
        grid.move(child)
        (_, utility) = minimize(grid, a, b, d)
        if utility > maxUtility:
            (maxChild, maxUtility) = (grid, utility)
        if maxUtility >= b:
            break
        if maxUtility > a:
            a = maxUtility

    return (maxChild, maxUtility)

def minimize(state: Grid, a: int, b: int, d: int) -> Tuple[Grid, int]:
    (minChild, minUtility) = (None, MAX_INT)

    if d == 0:
        return (None, state.utilityEstimate())
    elif state.isTerminal(who="min"):
        return (None, state.utility())

    d -= 1
    
    for child in state.getChildren(who = "min"):
        grid = Grid(matrix=state.getMatrix())
        grid.placeTile(child[2], child[0], child[1])
        (_, utility) = maximize(grid, a, b, d)
        if utility < minUtility:
            (minChild, minUtility) = (grid, utility)
        if minUtility <= a:
            break
        if minUtility < b:
            b = minUtility

    return (minChild, minUtility)

class PlayerAI:
    # @params:
    #         grid  - a valid Grid object
    #         depth - a positive integer (should NOT be equal to 0) 
    def __init__(self, grid: Grid, depth: int = 5):
        self.grid = grid
        self.maxDepth = depth

    def getBestMove(self) -> int:
        (child, _) = maximize(Grid(matrix=self.grid.getMatrix()), -1, MAX_INT, self.maxDepth)
        return self.grid.getMoveTo(child)
    