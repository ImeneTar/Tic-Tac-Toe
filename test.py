from tictactoe import player, initial_state, actions, result, terminal, utility, result
EMPTY = None


board = [['O', 'O', 'O'],
        ['O', 'X', 'X'],
        ['X', 'X', EMPTY]]

print(result(board, (2,2)))




print(terminal(board))
print(utility(board))


