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

    def draw_redo(self, win):
        font = pygame.font.SysFont('comics', 25)
        rematch = font.render('ReDo', True, (36, 34, 34))
        pygame.draw.rect(win, GREY, (700, 100, 100, 50))
        win.blit(rematch, (725, 120))
        pygame.draw.line(win, BLACK, (700, 100), (800, 100), 2)
        pygame.draw.line(win, BLACK, (700, 100), (700, 150), 2)
        pygame.draw.line(win, BLACK, (700, 150), (800, 150), 2)
        pygame.draw.line(win, BLACK, (800, 100), (800, 150), 2)
