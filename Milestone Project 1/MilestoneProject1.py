# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:40:44 2017

@author: koteo
"""
# Imports
from IPython.display import clear_output
from random import randint


# Def´s 
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
example_board = [' ','1','2','3','4','5','6','7','8','9']

def display_board(board):
    clear_output()
    print board[1] + " | " + board[2] + " | " + board[3]
    print "---------"
    print board[4] + " | " + board[5] + " | " + board[6]
    print "---------"
    print board[7] + " | " + board[8] + " | " + board[9]


def player_input():
    while True:
        play1mark = ''
        play2mark = ''
        marker = raw_input("Player 1, provide the correct mark X or O: ").upper()
        if marker == "X":
                play1mark = "X"
                global play1mark
                play2mark = "O"
                global play2mark
                break
        elif marker == "O":
                play1mark = "O"
                global play1mark
                play2mark = "X"
                global play2mark
                break

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False

def choose_first():
    first = randint(1,2)
    if first == 1:
        return "Player1"
    else:
        return "Player2"

def space_check(board, position):
    return board[position] == ' '
    
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i) == True:
            return False
    return True

def player_choice(board):
    
    while True:
        ask_pos = input('Please input the next position 1-9: ')
        if ask_pos > 0 and ask_pos < 10 and space_check(board, ask_pos) == True:
            return ask_pos
            break

def replay():
    while True:
        play_again = raw_input('Do you want to play again? (Y/N) ')
        if play_again.upper() == 'Y':
            return True
        elif play_again.upper() == 'N':
            return False
        else:
            True

### HERE THE GAME START´S!! ###

print 'This is an example of the board, with the positions\n'
display_board(example_board)

while True:
    player_input()
    
    turn = choose_first()
    print '%s goes first' % (turn)
    game_on = True
    
    while game_on:
        if turn == 'Player1':
            
            display_board(board)
            position = player_choice(board)
            place_marker(board, play1mark, position)

            if win_check(board, play1mark):
                display_board(board)
                print('Congratulations! You have won the game!!!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is draw')
                    break
                else:
                    turn = 'Player2'
        
        else:
            
            display_board(board)
            position = player_choice(board)
            place_marker(board, play2mark, position)
            
            if win_check(board, play2mark):
                display_board(board)
                print('Player 2 has won!!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is Tie!')
                    break
                else:
                    turn = 'Player1'
                

    if not replay():
        break
                
        
            
            
            
    



    