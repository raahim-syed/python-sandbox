import numpy as np


board_size = int(input("Enter Board Size:"))

game_board = np.zeros((board_size, board_size))

def is_safe(board, i, j):
    pass


def backtracking(board, depth):
    # Checking If Tree Is Fully Branched (Base Condition)
    if depth == board_size - 1:
        return (1, True, board)

    # Make a Copy of the board
    board_copy = board[:, :]
    
    # Storing Number of possible combinations
    number_combinations = 0
    
    # Looping through state tree
    for j in range(board_size):
        # Placing Queen
        board_copy[]
        
        # Checking if position is safe
        if is_safe(board_copy, depth, j):
            depth += 1
            result = backtracking(board_copy, depth)
        else:
            continue
    
    # if is_safe(board, depth, j): 
  
    #     # Make a Copy of the board
    #     board_copy = board[:, :]
        
    #     for i in range(board_size):
    #         depth += 1
            
    #         result = backtracking(board_copy, depth)
    # else:
    #     return False    