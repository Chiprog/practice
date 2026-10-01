'''
TIC TAC TOE
This is a rather common game involving a 3x3 board abd its played by two players.
Each player gets to put their representative card (usually O and X) in any of the box
present in the grid. the goal of each player is to align their peices 3 in  a line.
This can be done diagonally, vertically or horizontally.
Some sample boards
1.  | |      2. X|O|X    3.O|X|O 
   -----        -----      -----
    | |          |O|       O|X|X 
   -----        -----      -----
    | |          |O|X      X|O|X
in code this is ussually represented by a 2X2 matrix or a list.
'''

import random
def win(p,board):
    for i in range(3):
        if board[0][i] == p and board[1][i] == p and board[2][i] == p:
            return True
        if board[i][0] == p and board[i][1] == p and board[i][2] == p:
            return True
    if (board[0][0] == p and board[1][1] == p and board[2][2] == p) or (board[0][2] == p and board[1][1] == p and board[2][0] == p):
        return True

def play(player,grid,sy):
    print (f'{player}, your turn')
    row = int(input("enter row number: ")) - 1
    column = int(input ("enter column number: ")) - 1
    while grid[row][column] != ' ':
        print("column already taken, Input another")
        row = int(input("enter row number: ")) - 1
        column = int(input ("enter column number: ")) - 1
    grid[row][column] = sy
    display(grid)
    if win(sy,grid):
        print(f'{player} wins')
        return True
    return False


def display(grid):
    for r in grid:
        print(r[0]+'|'+r[1]+'|'+r[2])
        print('------')
        

        
def TTT():
    grid = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
        ]
    
    player1 = input("welcome player1. Input your name : ").title()
    player2 = input("welcome player2. Input your name : ").title()


    display(grid)
    # i represents the number of turns which is usually 5 turns with only the first player playing the last turn
    i = 1
    while i <= 5 :
        if play(player1,grid,'O'):
            break
        if i == 4:
            print("draw")
            break
        if play(player2,grid,'X'):
            break
        i += 1
    
'''
TODO:
check if column is empty
display board
'''
