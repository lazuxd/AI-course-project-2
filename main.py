from Grid import Grid, MOVES
from PlayerAI import PlayerAI

if __name__ == '__main__':
    print('Please enter initial grid configuration:')

    line1 = input()
    line2 = input()
    line1 = list(map(lambda x: int(x), line1.split(',')))
    line2 = list(map(lambda x: int(x), line2.split(',')))
    
    grid = Grid(line1[0], line1[1], line1[2], line2[0], line2[1], line2[2])
    player = PlayerAI(grid)

    while not grid.isGameOver():
        move = player.getBestMove()
        print(f'Best move: {MOVES[move]}')
        grid.move(move)
        grid.print()
        line = input('Enter new tile:')
        line = list(map(lambda x: int(x), line.split(',')))
        grid.placeTile(line[0], line[1], line[2])
    
    print('Game Over!')
