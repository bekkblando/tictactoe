Class Forsight:

    def forsight(board, team, enemy_team):
        pass

    def generate_attack(board, team, enemy_team):
        pass

    def generate_defense(board, team, enemy_team):
        pass

    def check_possible_moves(board, team, enemy_team):
        left = list(get_diags(board)[0])
        right = list(get_diags(board)[1])
        row0 = get_row(board, 0)
        row1 = get_row(board, 1)
        row2 = get_row(board, 2)
        col0 = get_col(board, 0)
        debug_print("Col0", col0)
        col1 = get_col(board, 1)
        debug_print("Col1", col1)
        col2 = get_col(board, 2)
        debug_print("Col2", col2)
        moves = []
        for num in range(right.count('_')):
            moves.append(find_diag_spot(right, "right"))
        for num in range(left.count('_')):
            moves.append(find_diag_spot(left, "left"))
        for num in range(row0.count('_')):
            moves.append(find_row_spot(row0, 0))
        for num in range(row1.count('_')):
            moves.append(find_row_spot(row1, 1))
        for num in range(row2.count('_')):
            moves.append(find_row_spot(row2, 2))
        for num in range(col0.count('_')):
            moves.append(find_col_spot(col0, 0))
        for num in range(col1.count('_')):
            moves.append(find_col_spot(col1, 1))
        for num in range(col2.count('_')):
            moves.append(find_col_spot(col2, 2))
        debug_print("Possible Moves ", moves)
        check_forced_moves_agro(test_board, team, enemy_team, moves)

    def check_forced_moves_agro(test_board, team, enemy_team, moves):
        for item in moves:
            test_board[item[0]][item[1]] = 'X'
            debug_print("Test Board", test_board)

    def check_forced_moves_defense(board, team, enemy_team):
        pass

    def check_for_team_win(board, team):
        debug_print("Check for Team Win ", "Ran")
        left = list(get_diags(board)[0])
        right = list(get_diags(board)[1])
        row0 = get_row(board, 0)
        row1 = get_row(board, 1)
        row2 = get_row(board, 2)
        col0 = get_col(board, 0)
        debug_print("Col0", col0)
        col1 = get_col(board, 1)
        debug_print("Col1", col1)
        col2 = get_col(board, 2)
        debug_print("Col2", col2)
        if left.count(team) == 2:
            if check_empty(left):
                debug_print("Left Win Possible", left.count(team))
                execute_diag_win(board, team, "left")
                return "diag_win"
        if right.count(team) == 2:
            if check_empty(right):
                execute_diag_win(board, team, "right")
        if row0.count(team) == 2:
            if check_empty(row0):
                execute_row_win(board, team, 0)
        if row1.count(team) == 2:
            if check_empty(row1):
                execute_row_win(board, team, 1)
        if row2.count(team) == 2:
            if check_empty(row2):
                execute_row_win(board, team, 2)
        if col0.count(team) == 2:
            debug_print("win check", "col0")
            if check_empty(col0):
                execute_col_win(board, team, 0)
        if col1.count(team) == 2:
            debug_print("win check", "col1")
            if check_empty(col1):
                execute_col_win(board, team, 1)
        if col2.count(team) == 2:
            debug_print("win check", "col2")
            if check_empty(col2):
                execute_col_win(board, team, 2)

    def check_for_enemy_win(board, enemy_team, team):
        debug_print("Check for Enemy Team Win", "Ran")
        debug_print("Enemy", enemy_team)
        debug_print("team", team)
        left = list(get_diags(board)[0])
        right = list(get_diags(board)[1])
        row0 = get_row(board, 0)
        row1 = get_row(board, 1)
        row2 = get_row(board, 2)
        col0 = get_col(board, 0)
        debug_print("Col0 b", col0)
        col1 = get_col(board, 1)
        debug_print("Col1 b", col1)
        col2 = get_col(board, 2)
        debug_print("Col2 b", col2)
        if left.count(enemy_team) == 2:
            if check_empty(left):
                debug_print("block", "Left diag")
                execute_diag_block(board, enemy_team, "left")
                return("Left")
        if right.count(enemy_team) == 2:
            if check_empty(right):
                debug_print("block", "right diag")
                execute_diag_block(board, enemy_team, "right")
                return("Right")
        if row0.count(enemy_team) == 2:
            if check_empty(row0):
                debug_print("block", "row0")
                execute_row_block(board, enemy_team, 0)
                return("row0")
        if row1.count(enemy_team) == 2:
            if check_empty(row1):
                debug_print("block", "row1")
                execute_row_block(board, enemy_team, 1)
                return("row1")
        if row2.count(enemy_team) == 2:
            if check_empty(row2):
                debug_print("block", "row2")
                execute_row_block(board, enemy_team, 2)
                return("row2")
        if col0.count(enemy_team) == 2:
            debug_print("block check", "col2")
            if check_empty(col0):
                debug_print("block", "col0")
                execute_col_block(board, enemy_team, 0)
                return("Col0")
        if col1.count(enemy_team) == 2:
            debug_print("block check", "col2")
            if check_empty(col1):
                debug_print("block", "col1")
                execute_col_block(board, enemy_team, 1)
                return("Col1")
        if col2.count(enemy_team) == 2:
            debug_print("block check", "col2")
            if check_empty(col2):
                debug_print("block", "col2")
                execute_col_block(board, enemy_team, 2)
                return("Col2")
        debug_print("Early", "Game")
        early_game(board, team)
        debug_print("Made", "It")


    def execute_diag_win(board, team, side):
        debug_print("Execute diagonal", "Win")
        if side == "left":
            debug_print("Left", "Win")
            place_move(find_diag_spot(get_diags(board)[0], "left"))
        if side == "right":
            debug_print("Right", "Win")
            place_move(find_diag_spot(get_diags(board)[1], "right"))

    def execute_row_win(board, team, row_num):
        place_move(find_row_spot(get_row(board, row_num), row_num))

    def execute_col_win(board, team, col_num):
        place_move(find_col_spot(get_col(board, col_num), col_num))

    def execute_row_block(board, team, row_num):
        place_move(find_row_spot(get_row(board, row_num), row_num))

    def execute_col_block(board, team, col_num):
        place_move(find_col_spot(get_col(board, col_num), col_num))

    def execute_diag_block(board, team, side):
        if side == "left":
            place_move(find_diag_spot(get_diags(board)[0], "left"))
        if side == "right":
            place_move(find_diag_spot(get_diags(board)[1], "right"))
