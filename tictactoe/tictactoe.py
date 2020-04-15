"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0
    for i in board:
        for j in i:
            if j == O:
                count_o += 1
            elif j == X:
                count_x += 1
    return O if count_x > count_o else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Can't place there!")
    pl = player(board)
    newB = copy.deepcopy(board)
    newB[i][j] = pl
    return newB

def row_win(board, player):
    '''
    Returns True if the player has filled a row else False
    '''
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
    return False

def column_win(board, player):
    '''
    Returns True if the player has filled a column else False
    '''
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    return False

def diag_win(board, player):
    '''
    Returns True if a player has filled a diagnol else False
    '''
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for p in (O, X):
        if row_win(board, p) or column_win(board, p) or diag_win(board, p):
            return p
    return None

def isfull(board):
    '''
    Check if board is full
    '''
    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or isfull(board):
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == None:
        return 0
    elif win == X:
        return 1
    else:
        return -1

def minplayer(board):
    """
    Returns the optimal action and utility value on taking the action for the min player on the board.
    """
    if terminal(board):
        return (utility(board),)

    v = float('inf')
    optA = None
    for a in actions(board):
        res = maxplayer(result(board, a))
        if res[0] < v:
            v = res[0]
            optA = a
    return v, optA

def maxplayer(board):
    """
    Returns the optimal action for the max player on the board.
    """
    if terminal(board):
        return (utility(board),)

    v = -1 * float('inf')
    optA = None
    for a in actions(board):
        res = minplayer(result(board, a))
        if res[0] > v:
            v = res[0]
            optA = a
    return v, optA

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    p = player(board)
    if p == X:
        return maxplayer(board)[1]
    else:
        return minplayer(board)[1]
