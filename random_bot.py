import random
from board import Board, import_tic_tac_toe_board

player, text_board = import_tic_tac_toe_board()
board = Board(text_board)
coords = (1, 1)
while True:
    coords = (random.randint(0, 2), random.randint(0, 2))
    if board.get_value(coords) == "_":
        break

print('{} {}'.format(coords[0], coords[1]))
