"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
turn = X


def initial_state():
    """
    Returns starting state of the board.
    """


    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def is_empty(board):
    """
    Tells if the board is empty or not.
    """

    return board == initial_state()

def board_counter(board):
    """
    Returns number of cells filled.
    """
    count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1

    return count

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #Empty board => X
    if is_empty(board):
        return X
    else:
        count = board_counter(board)

        #count even  => X, odd => O
        if (count % 2==0):
            return  X
        else :
            return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY :
                action.add((i, j))

    return action



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return (new_board)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    elif board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]

    else :
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!= None or board_counter(board)==9 :
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    else:
        return None

def max_value(board):
    if terminal(board):
        return utility(board)

    v = float('-inf')

    for a in actions(board):
        v = max(v, min_value(result(board, a)))

    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = float('inf')

    for a in actions(board):
        v = min(v, max_value(result(board, a)))

    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        v = max_value(board)
        for a in actions(board):
            if v == min_value(result(board, a)):
                return a

    else:
        v = min_value(board)
        for a in actions(board):
            if v == max_value(result(board, a)):
                return a

