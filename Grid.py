from typing import List, Tuple
from copy import deepcopy

MOVES = { 0: "Up", 1: "Down", 2: "Left", 3: "Right" }

class Grid:

    def __init__(self, tile1 = 2, row1 = 1, col1 = 1, tile2 = 2, row2 = 1, col2 = 2, matrix = None):
        if matrix is None:
            self.matrix = [[0 for i in range(4)] for j in range(4)]
            self.placeTile(tile1, row1, col1)
            self.placeTile(tile2, row2, col2)
        else:
            self.matrix = matrix
    
    def __eq__(self, other: 'Grid'):
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def getMatrix(self):
        return deepcopy(self.matrix)
    
    def print(self):
        for i in range(4):
            for j in range(4):
                print(self.matrix[i][j], end=' ')
            print()

    def placeTile(self, tile, row, col):
        self.matrix[row-1][col-1] = tile
    
    def canMoveUp(self):
        for j in range(4):
            k = -1
            for i in range(3, -1, -1):
                if self.matrix[i][j] > 0:
                    k = i
                    break
            if k > -1:
                for i in range(k, 0, -1):
                    if self.matrix[i][j] == 0 or self.matrix[i][j] == self.matrix[i-1][j]:
                        return True
                if self.matrix[0][j] == 0:
                    return True
        return False

    def canMoveDown(self):
        for j in range(4):
            k = -1
            for i in range(4):
                if self.matrix[i][j] > 0:
                    k = i
                    break
            if k > -1:
                for i in range(k, 3):
                    if self.matrix[i][j] == 0 or self.matrix[i][j] == self.matrix[i+1][j]:
                        return True
                if self.matrix[3][j] == 0:
                    return True
        return False

    def canMoveLeft(self):
        for i in range(4):
            k = -1
            for j in range(3, -1, -1):
                if self.matrix[i][j] > 0:
                    k = j
                    break
            if k > -1:
                for j in range(k, 0, -1):
                    if self.matrix[i][j] == 0 or self.matrix[i][j] == self.matrix[i][j-1]:
                        return True
                if self.matrix[i][0] == 0:
                    return True
        return False

    def canMoveRight(self):
        for i in range(4):
            k = -1
            for j in range(4):
                if self.matrix[i][j] > 0:
                    k = j
                    break
            if k > -1:
                for j in range(k, 3):
                    if self.matrix[i][j] == 0 or self.matrix[i][j] == self.matrix[i][j+1]:
                        return True
                if self.matrix[i][3] == 0:
                    return True
        return False
    
    def getAvailableMovesForMax(self) -> List[int]:
        moves = []

        if self.canMoveUp():
            moves.append(0)
        if self.canMoveDown():
            moves.append(1)
        if self.canMoveLeft():
            moves.append(2)
        if self.canMoveRight():
            moves.append(3)
        
        return moves
    
    def isGameOver(self) -> bool:
        return len(self.getAvailableMoves()) == 0
    
    def getAvailableMovesForMin(self) -> List[Tuple]:
        places = []
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    places.append((i+1, j+1, 2))
                    places.append((i+1, j+1, 4))
        return places
    
    def up(self):
        for j in range(4):
            w = 0
            k = 0
            for i in range(4):
                if self.matrix[i][j] == 0:
                    continue
                if k == 0:
                    k = self.matrix[i][j]
                elif k == self.matrix[i][j]:
                    self.matrix[w][j] = 2*k
                    w += 1
                    k = 0
                else:
                    self.matrix[w][j] = k
                    w += 1
                    k = self.matrix[i][j]
            if k != 0:
                self.matrix[w][j] = k
                w += 1
            for i in range(w, 4):
                self.matrix[i][j] = 0
    
    def down(self):
        for j in range(4):
            w = 3
            k = 0
            for i in range(3, -1, -1):
                if self.matrix[i][j] == 0:
                    continue
                if k == 0:
                    k = self.matrix[i][j]
                elif k == self.matrix[i][j]:
                    self.matrix[w][j] = 2*k
                    w -= 1
                    k = 0
                else:
                    self.matrix[w][j] = k
                    w -= 1
                    k = self.matrix[i][j]
            if k != 0:
                self.matrix[w][j] = k
                w -= 1
            for i in range(w+1):
                self.matrix[i][j] = 0
    
    def left(self):
        for i in range(4):
            w = 0
            k = 0
            for j in range(4):
                if self.matrix[i][j] == 0:
                    continue
                if k == 0:
                    k = self.matrix[i][j]
                elif k == self.matrix[i][j]:
                    self.matrix[i][w] = 2*k
                    w += 1
                    k = 0
                else:
                    self.matrix[i][w] = k
                    w += 1
                    k = self.matrix[i][j]
            if k != 0:
                self.matrix[i][w] = k
                w += 1
            for j in range(w, 4):
                self.matrix[i][j] = 0
    
    def right(self):
        for i in range(4):
            w = 3
            k = 0
            for j in range(3, -1, -1):
                if self.matrix[i][j] == 0:
                    continue
                if k == 0:
                    k = self.matrix[i][j]
                elif k == self.matrix[i][j]:
                    self.matrix[i][w] = 2*k
                    w -= 1
                    k = 0
                else:
                    self.matrix[i][w] = k
                    w -= 1
                    k = self.matrix[i][j]
            if k != 0:
                self.matrix[i][w] = k
                w -= 1
            for j in range(w+1):
                self.matrix[i][j] = 0
    
    def move(self, mv):
        if mv == 0:
            self.up()
        elif mv == 1:
            self.down()
        elif mv == 2:
            self.left()
        else:
            self.right()
    
    def getMoveTo(self, child: 'Grid') -> int:
        if self.canMoveUp():
            g = Grid(matrix=self.getMatrix())
            g.up()
            if g == child:
                return 0
        if self.canMoveDown():
            g = Grid(matrix=self.getMatrix())
            g.down()
            if g == child:
                return 1
        if self.canMoveLeft():
            g = Grid(matrix=self.getMatrix())
            g.left()
            if g == child:
                return 2
        return 3
    
    def utility(self):
        max = 2
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] > max:
                    max = self.matrix[i][j]
        return max
    
    def isTerminal(self, who: str) -> bool:
        if who == "max":
            return len(self.getAvailableMovesForMax()) == 0
        elif who == "min":
            return len(self.getAvailableMovesForMin()) == 0
    
    def getChildren(self, who: str) -> List:
        if who == "max":
            return self.getAvailableMovesForMax()
        elif who == "min":
            return self.getAvailableMovesForMin()
