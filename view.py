from constants import *


class View:

    def __init__(self):
        pass

    #     TODO does the view needs to know the controller ?

    def draw_game(self, win, board):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = board[row][col]
                if piece != 0:
                    piece.draw_piece(win)

    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(COLS):
                if (col % 2 != 0 and row % 2 != 0) or (col % 2 == 0 and row % 2 == 0):
                    pygame.draw.rect(win, LIGHT_BROWN,
                                     (row * SQUARE_SIZE + 1, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(win, BROWN, (row * SQUARE_SIZE + 1, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        self.draw_board_borders(win)

    def draw_board_borders(self, win):
        pygame.draw.line(win, BLACK, [0, 0], [0, WIDTH], 8)
        pygame.draw.line(win, BLACK, [0, 0], [HEIGHT, 0], 8)
        pygame.draw.line(win, BLACK, [HEIGHT, WIDTH], [0, WIDTH], 8)
        pygame.draw.line(win, BLACK, [HEIGHT, WIDTH], [HEIGHT, 0], 12)

    def draw_valid_moves(self, win, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(win, RED,
                               ((col * SQUARE_SIZE + SQUARE_SIZE // 2), (row * SQUARE_SIZE + SQUARE_SIZE // 2)), 25,
                               width=4)

    def draw_winner(self, win, winner):
        self.draw_squares(win)
        large_font = pygame.font.SysFont('comics', 40)
        winner = large_font.render('The winner is : ' + str(winner), True, (255, 255, 255))
        win.blit(winner, (650 / 2 - winner.get_width() / 2, 200))

    def draw_rematch(self, win):
        win.fill(WHITE)
        font = pygame.font.SysFont('comics', 40)
        rematch = font.render('Would You Like A Rematch ?', True, BLACK)
        win.blit(rematch, (700 / 2 - rematch.get_width() / 2, 250))
        yes = font.render('Yes', True, WHITE)
        no = font.render('No', True, WHITE)
        pygame.draw.rect(win, GREEN, (150, 450, 100, 50))
        pygame.draw.rect(win, RED, (450, 450, 100, 50))
        win.blit(yes, (175, 460))
        win.blit(no, (482, 461))

    def draw_undo(self, win, player_turn):
        font = pygame.font.SysFont('comics', 23)
        turn = self.conver_turn_to_str(player_turn)
        player_undo = turn + ' Undo'
        rematch = font.render(player_undo, True, (36, 34, 34))
        pygame.draw.rect(win, GREY, (700, 100, 100, 50))
        win.blit(rematch, (710, 120))
        pygame.draw.line(win, BLACK, (700, 100), (800, 100), 2)
        pygame.draw.line(win, BLACK, (700, 100), (700, 150), 2)
        pygame.draw.line(win, BLACK, (700, 150), (800, 150), 2)
        pygame.draw.line(win, BLACK, (800, 100), (800, 150), 2)

    def draw_remain_undoes(self, win, white_player_undo, black_play_undo):
        font = pygame.font.SysFont('comics', 23)
        white_undoes = 'White Undo left : ' + str(white_player_undo)
        black_undoes = 'Black Undo left : ' + str(black_play_undo)
        white_render = font.render(white_undoes, True, (36, 34, 34))
        black_render = font.render(black_undoes, True, (36, 34, 34))
        win.blit(white_render, (680, 180))
        win.blit(black_render, (680, 210))

    def draw_timer(self, win, minutes, seconds):
        font = pygame.font.SysFont('comics', 23)
        min_str = str(int(minutes))
        if minutes < 10:
            min_str = "0" + str(int(minutes))
        sec_str = str(int(seconds))
        if seconds < 10:
            sec_str = "0" + str(int(seconds))
        time_str = min_str + ":" + sec_str
        time_render = font.render(time_str,True, (36, 34, 34))
        win.blit(time_render, (680, 400))


    def conver_turn_to_str(self, player_turn):
        if player_turn == WHITE:
            return 'Black'
        else:
            return 'White'
