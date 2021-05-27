from constants import *


class View:

    def __init__(self):
        pass

    def draw_game(self, win, board):
        """"
        draw board with pieces and exit button
        :param board: matrix of pieces
        :param win: pygame screen
        :return:
        """
        win.fill(WHITE)
        win.blit(EXIT, (905, 12))
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = board[row][col]
                if piece != 0:
                    piece.draw_piece(win)

    def draw_squares(self, win):
        """"
        draw board squares
        :param win: pygame screen
        :return:
        """
        for row in range(ROWS):
            for col in range(COLS):
                if (col % 2 != 0 and row % 2 != 0) or (col % 2 == 0 and row % 2 == 0):
                    pygame.draw.rect(win, LIGHT_BROWN,
                                     (row * SQUARE_SIZE + 1, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(win, BROWN, (row * SQUARE_SIZE + 1, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        self.draw_board_borders(win)

    def draw_board_borders(self, win):
        """"
        draw board black borders
        :param win: pygame screen
        :return:
        """
        pygame.draw.line(win, BLACK, [0, 0], [0, WIDTH], 8)
        pygame.draw.line(win, BLACK, [0, 0], [HEIGHT, 0], 8)
        pygame.draw.line(win, BLACK, [HEIGHT, WIDTH], [0, WIDTH], 8)
        pygame.draw.line(win, BLACK, [HEIGHT, WIDTH], [HEIGHT, 0], 12)

    def draw_valid_moves(self, win, moves):
        """"
        draw red circles on squares the player can move on
        :param moves: player's valid moves
        :param win: pygame screen
        :return:
        """
        for move in moves:
            row, col = move
            pygame.draw.circle(win, RED,
                               ((col * SQUARE_SIZE + SQUARE_SIZE // 2), (row * SQUARE_SIZE + SQUARE_SIZE // 2)), 25,
                               width=4)

    def draw_winner(self, win, winner, no_moves, white_left, black_left):
        """"
        write on screen the winner color player
        :param black_left: for draw check
        :param white_left: for draw check
        :param win: pygame screen
        :param winner: winner player
        :param no_moves: True if Auto lose because no piece could move
        :return:
        """
        if no_moves and black_left != white_left:
            loser = "White"
            if winner == 'WHITE':
                loser = "Black"
            regular_font = pygame.font.SysFont('comics', 30)
            auto_lose = regular_font.render(str(loser) + ' had no moves!!' , True, BLACK)
            win.blit(auto_lose, (690, 160))
        large_font = pygame.font.SysFont('comics', 40)
        winner = large_font.render(str(winner) + " Wins!!!", True, BLACK)
        if white_left == black_left:
            winner = large_font.render('Draw!!!', True, BLACK)
            win.blit(winner, (750, 200))
        else:
            win.blit(winner, (700, 200))

    def draw_rematch(self, win, board):
        """"
        Draw last state of board. Who wins and "Rematch" button
        :param board: matrix of pieces
        :param win: pygame screen
        :return:
        """
        self.draw_game(win, board)
        x = 740
        y = 270
        pos = pygame.mouse.get_pos()
        color = BLUE
        if x + 100 > pos[0] > x and y + 50 > pos[1] > y:
            color = DARK_BLUE
        pygame.draw.rect(win, color, (x, y, 100, 50))

        text = " Rematch  "
        font = pygame.font.SysFont("David", 25)
        outline_font = pygame.font.SysFont("David", 25)

        outline_text = outline_font.render(text, True, BLACK)
        button_text = font.render(text, True, WHITE)
        win.blit(outline_text, (x + 3, y + 15))
        win.blit(button_text, (x + 2, y + 13))
        pygame.draw.line(win, BLACK, (x, y), (x, y + 50), 2)
        pygame.draw.line(win, BLACK, (x, y), (x + 100, y), 2)
        pygame.draw.line(win, BLACK, (x, y + 50), (x + 100, y + 50), 2)
        pygame.draw.line(win, BLACK, (x + 100, y), (x + 100, y + 50), 2)

    def draw_menu(self, win):
        """"
        Draw instructions and "Start" button
        :param win: pygame screen
        :return:
        """
        pos = pygame.mouse.get_pos()
        win.fill(WHITE)
        win.blit(INSTRUCTIONS, (10, 10))
        x = 430
        y = 500
        color = BLUE
        if x + 100 > pos[0] > x and y + 40 > pos[1] > y:
            color = DARK_BLUE

        pygame.draw.rect(win, color, (x, y, 100, 40))
        text = "  Start"
        font = pygame.font.SysFont("David", 32)
        outline_font = pygame.font.SysFont("David", 32)

        outline_text = outline_font.render(text, True, BLACK)
        button_text = font.render(text, True, WHITE)
        win.blit(outline_text, (x + 7, y + 10))
        win.blit(button_text, (x + 5, y + 8))
        pygame.draw.line(win, BLACK, (x, y), (x, y + 40), 2)
        pygame.draw.line(win, BLACK, (x, y), (x + 100, y), 2)
        pygame.draw.line(win, BLACK, (x, y + 40), (x + 100, y + 40), 2)
        pygame.draw.line(win, BLACK, (x + 100, y), (x + 100, y + 40), 2)

    def draw_undo(self, win, player_turn, first_turn, black_undo_left, white_undo_left):
        """"
        Draw Undo button
        :param white_undo_left: if 0, white can't undo
        :param black_undo_left: if 0, black can't undo
        :param first_turn: on first turn no one can undo
        :param player_turn: which one can do undo
        :param win: pygame screen
        :return:
        """
        if first_turn:
            return
        if player_turn == WHITE and black_undo_left == 0:
            return
        if player_turn == BLACK and white_undo_left == 0:
            return
        font = pygame.font.SysFont('comics', 23)
        turn = self.conver_turn_to_str(player_turn)
        player_undo = turn + ' Undo'
        player_undo = font.render(player_undo, True, (36, 34, 34))
        color = GREY
        pos = pygame.mouse.get_pos()
        x = 740
        y = 250
        if x + 100 > pos[0] > x and y + 50 > pos[1] > y:
            color = DARK_GREY
        pygame.draw.rect(win, color, (x, y, 100, 50))
        win.blit(player_undo, (x + 10, y + 20))
        pygame.draw.line(win, BLACK, (x, y), (x + 100, y), 2)
        pygame.draw.line(win, BLACK, (x, y), (x, y + 50), 2)
        pygame.draw.line(win, BLACK, (x, y + 50), (x + 100, y + 50), 2)
        pygame.draw.line(win, BLACK, (x + 100, y), (x + 100, y + 50), 2)

    def draw_remain_undoes(self, win, white_player_undo, black_play_undo):
        """"
        write on screen how much remain undoes for each player
        :param win: pygame screen
        :param black_play_undo: write num of black's undo
        :param white_player_undo: write num of white's undo
        :return:
        """
        font = pygame.font.SysFont('comics', 23)
        white_undoes = 'White Undo left : ' + str(white_player_undo)
        black_undoes = 'Black Undo left : ' + str(black_play_undo)
        white_render = font.render(white_undoes, True, (36, 34, 34))
        black_render = font.render(black_undoes, True, (36, 34, 34))
        win.blit(white_render, (730, 500))
        win.blit(black_render, (730, 100))

    def draw_timers(self, win, minutes_white, seconds_white, minutes_black, seconds_black):
        """"
        draw timers to each player
        :param win: pygame screen
        :return:
        """
        font = pygame.font.SysFont('David', 23)

        time_str_white = '{:02d}:{:02d}'.format(int(minutes_white), int(seconds_white))
        time_str_black = '{:02d}:{:02d}'.format(int(minutes_black), int(seconds_black))

        time_render_white = font.render(time_str_white, True, (36, 34, 34))
        time_render_black = font.render(time_str_black, True, (36, 34, 34))
        timer_x = 765
        white_timer_y = 550
        black_timer_y = 50
        win.blit(time_render_white, (timer_x, white_timer_y))
        win.blit(time_render_black, (timer_x, black_timer_y))
        # White Timer Border
        pygame.draw.line(win, BLACK, (timer_x - 5, white_timer_y - 5), (timer_x + 55, white_timer_y - 5), 2)
        pygame.draw.line(win, BLACK, (timer_x - 5, white_timer_y - 5), (timer_x - 5, white_timer_y + 25), 2)
        pygame.draw.line(win, BLACK, (timer_x - 5, white_timer_y + 25), (timer_x + 55, white_timer_y + 25), 2)
        pygame.draw.line(win, BLACK, (timer_x + 55, white_timer_y - 5), (timer_x + 55, white_timer_y + 25), 2)
        # Black Timer Border
        pygame.draw.line(win, BLACK, (timer_x - 5, black_timer_y - 5), (timer_x + 55, black_timer_y - 5), 2)
        pygame.draw.line(win, BLACK, (timer_x - 5, black_timer_y - 5), (timer_x - 5, black_timer_y + 25), 2)
        pygame.draw.line(win, BLACK, (timer_x - 5, black_timer_y + 25), (timer_x + 55, black_timer_y + 25), 2)
        pygame.draw.line(win, BLACK, (timer_x + 55, black_timer_y - 5), (timer_x + 55, black_timer_y + 25), 2)

    def conver_turn_to_str(self, player_turn):
        """"
        convert color to string
        :param player_turn: RGB color
        :return:
        """
        if player_turn == WHITE:
            return 'Black'
        else:
            return 'White'
