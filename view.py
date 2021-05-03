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
        #self.draw_squares(win)
        large_font = pygame.font.SysFont('comics', 40)
        winner = large_font.render('The winner is : ' + str(winner), True, BLACK)
        win.blit(winner, (250, 200))

    def draw_rematch(self, win):
        win.fill(GREY)
        font = pygame.font.SysFont('comics', 40)
        rematch = font.render('Would you like a rematch?', True, BLACK)
        win.blit(rematch, (820 / 2 - rematch.get_width() / 2, 250))
        yes = font.render('Yes', True, WHITE)
        no = font.render('No', True, WHITE)
        pygame.draw.rect(win, GREEN, (250, 350, 100, 50))
        pygame.draw.rect(win, RED, (450, 350, 100, 50))
        win.blit(yes, (275, 362))
        win.blit(no, (482, 362))

    def draw_undo(self, win, player_turn):
        font = pygame.font.SysFont('comics', 23)
        turn = self.conver_turn_to_str(player_turn)
        player_undo = turn + ' Undo'
        player_undo = font.render(player_undo, True, (36, 34, 34))
        pygame.draw.rect(win, GREY, (700, 250, 100, 50))
        win.blit(player_undo, (710, 270))
        pygame.draw.line(win, BLACK, (700, 250), (800, 250), 2)
        pygame.draw.line(win, BLACK, (700, 250), (700, 300), 2)
        pygame.draw.line(win, BLACK, (700, 300), (800, 300), 2)
        pygame.draw.line(win, BLACK, (800, 250), (800, 300), 2)

    def draw_remain_undoes(self, win, white_player_undo, black_play_undo):

        font = pygame.font.SysFont('comics', 23)
        white_undoes = 'White Undo left : ' + str(white_player_undo)
        black_undoes = 'Black Undo left : ' + str(black_play_undo)
        white_render = font.render(white_undoes, True, (36, 34, 34))
        black_render = font.render(black_undoes, True, (36, 34, 34))
        win.blit(white_render, (680, 500))
        win.blit(black_render, (680, 100))

    def draw_timer(self, win, minutes_white, seconds_white, minutes_black, seconds_black):
        font = pygame.font.SysFont('David', 23)

        time_str_white = '{:02d}:{:02d}'.format(int(minutes_white), int(seconds_white))
        time_str_black = '{:02d}:{:02d}'.format(int(minutes_black), int(seconds_black))

        time_render_white = font.render(time_str_white, True, (36, 34, 34))
        time_render_black = font.render(time_str_black, True, (36, 34, 34))
        win.blit(time_render_white, (680, 550))
        win.blit(time_render_black, (680, 50))



    def conver_turn_to_str(self, player_turn):
        if player_turn == WHITE:
            return 'Black'
        else:
            return 'White'
