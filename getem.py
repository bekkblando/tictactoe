import sys
import numpy


def debug_print(whattoprint, information):
    print("DEBUG: ", whattoprint, information, file=sys.stderr)

# get your team & get your board
"""board = []
team = input()
first_row = input()
first_row = list(first_row)
second_row = input()
second_row = list(second_row)
third_row = input()
third_row = list(third_row)
board = [first_row, second_row, third_row]

# print out the inputs you're getting
debug_print("Your Team is ", team)
debug_print("Your First row ", first_row)
debug_print("Your Second row ", second_row)
debug_print("Your third row ", third_row)
debug_print("Your board ", board)
# Outputting the coordinates of your board"""

board = [['X', '_', 'O'],
         ['_', 'Y', '_'],
         ['P', '_', 'X']]


def find_team():
    pass


def get_col(board, which):
    answer = []
    init_list = [0 for x in range(len(board))]
    for n, num in enumerate(board):
        # print("Run")
        # print(init_list)
        for number, value in enumerate(num):
            # print(num[col_num])
            init_list[n] = num[which]
            # print(init_list)
    return init_list


print("Column 1", get_col(board, 0))
print("Column 2", get_col(board, 1))
print("Column 3", get_col(board, 2))

def get_row(board, which):
    return board[which]

print(get_row(board, 0))
print(get_row(board, 1))
print(get_row(board, 2))


def get_diags(board):
    diagonal = numpy.diagonal(board)
    new_diagonal = numpy.diagonal(board[::-1])
    return (diagonal, new_diagonal)

a, b = get_diags(board)
print(a)
print(b)
# get_diag(board)


def check_for_team_win(board, team):
    left = get_diags(board)[0]
    right = get_diags(board)[1]
    row0 = get_row(board, 0)
    row1 = get_row(board, 1)
    row2 = get_row(board, 2)
    col0 = get_col(board, 0)
    col1 = get_col(board, 1)
    col2 = get_col(board, 2)
    if left.count(team) == 2:
        execute_diag_win(board, team, left)
    if right.count(team) == 2:
        execute_diag_win(board, team, right)
    if row0.count(team) == 2:
        execute_row_win(board, team, 0)
    if row1.count(team) == 2:
        execute_row_win(board, team, 1)
    if row2.count(team) == 2:
        execute_row_win(board, team, 2)
    if col0.count(team) == 2:
        execute_col_win(board, team, 0)
    if col1.count(team) == 2:
        execute_col_win(board, team, 1)
    if col2.count(team) == 2:
        execute_col_win(board, team, 2)


def check_for_enemy_win():
    left = get_diags(board)[0]
    right = get_diags(board)[1]
    row0 = get_row(board, 0)
    row1 = get_row(board, 1)
    row2 = get_row(board, 2)
    col0 = get_col(board, 0)
    col1 = get_col(board, 1)
    col2 = get_col(board, 2)
    if left.count(team) == 2:
        execute_diag_block(board, team, left)
    if right.count(team) == 2:
        execute_diag_block(board, team, right)
    if row0.count(team) == 2:
        execute_row_block(board, team, 0)
    if row1.count(team) == 2:
        execute_row_block(board, team, 1)
    if row2.count(team) == 2:
        execute_row_block(board, team, 2)
    if col0.count(team) == 2:
        execute_col_block(board, team, 0)
    if col1.count(team) == 2:
        execute_col_block(board, team, 1)
    if col2.count(team) == 2:
        execute_col_block(board, team, 2)


def execute_diag_win(board, team, side):
    if side == "left":
        place_move(find_diag_spot(get_diags(board)[0]))
    if side == "right":
        place_move(find_diag_spot(get_diags(board)[1]))


def execute_row_win(board, team, row):
    place_move(find_row_spot(get_row(board, row)))


def execute_col_win(board, team, col):
    place_move(find_col_spot(get_row(board, col)))


def execute_row_block(board, team, row):
    place_move(find_row_spot(get_row(board, row)))


def execute_col_block(board, team, col):
    place_move(find_col_spot(get_row(board, col)))


def execute_diag_block(board, team, side):
    if side == "left":
        place_move(find_diag_spot(get_diags(board)[0]))
    if side == "right":
        place_move(find_diag_spot(get_diags(board)[1]))


def place_move():
    pass


def find_row_spot(list):
    pass

def find_col_spot(list):
    pass


def find_diag_spot(list)
    pass


import random
if random.random() > .5:
    print("0 1")
else:
    print("0 0")
