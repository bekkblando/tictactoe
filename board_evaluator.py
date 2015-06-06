from board import Board


def detect_victory_chance(line):
    if line.count("_") != 1 or line.count("X") == 1:
        return ("", -1)
    win_index = line.index("_")
    return (line[(win_index + 1) % 3], win_index)


def row_victory_chance(board, row_number):
    victory = detect_victory_chance(board.get_row(row_number))
    return (victory[0], (row_number, victory[1]))


def col_victory_chance(board, col_number):
    victory = detect_victory_chance(board.get_col(col_number))
    return (victory[0], (victory[1], col_number))


def diag_victory_chance(board, diag_number):
    victory = detect_victory_chance(board.get_diag(diag_number))
    return (victory[0], board.get_coord_diag(diag_number, victory[1]))


def victory_chances(board):
    victories = []
    for index in range(3):
        victory = row_victory_chance(board, index)
        if victory[0]:
            victories.append(victory)
        victory = col_victory_chance(board, index)
        if victory[0]:
            victories.append(victory)
        if index < 2:
            victory = diag_victory_chance(board, index)
            if victory[0]:
                victories.append(victory)
    return victories

if __name__ == "__main__":
    text_state = ["XO_",
                  "_OX",
                  "X_O"]
    board = Board(text_state)
    for row in board.text_state:
        print(row)
    print(victory_chances(board))
