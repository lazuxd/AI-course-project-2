class Grid:

    MOVES = { 0: "Up", 1: "Down", 2: "Left", 3: "Right" }

    def __init__(self, tile1, row1, col1, tile2, row2, col2):
        self.matrix = [[0 for i in range(4)] for j in range(4)]
        self.placeTile(tile1, row1, col1)
        self.placeTile(tile2, row2, col2)

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
                    k = i
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
                    k = i
                    break
            if k > -1:
                for j in range(k, 3):
                    if self.matrix[i][j] == 0 or self.matrix[i][j] == self.matrix[i][j+1]:
                        return True
                if self.matrix[i][3] == 0:
                    return True
        return False
    
    def getAvailableMoves(self):
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
    
    def isGameOver(self):
        return len(self.getAvailableMoves()) == 0
    
    def getAvailablePlaces(self):
        places = []
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    places.append((i+1, j+1))
        return places
    
    def up(self):
        if not self.canMoveUp():
            return False
        # Do stuff
        return True
    
    def down(self):
        if not self.canMoveDown():
            return False
        # Do stuff
        return True
    
    def left(self):
        if not self.canMoveLeft():
            return False
        # Do stuff
        return True
    
    def right(self):
        if not self.canMoveRight():
            return False
        # Do stuff
        return True
