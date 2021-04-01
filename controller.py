from model import Model
from view import View
import pygame
from constants import *


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(FPS)

            if self.model.check_winner() is not None:
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_row_col_from_mouse(pos)
                    self.model.select(row, col)

            self.update()

        self.show_winner()

    def show_winner(self):
        run = True
        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.view.reset_screen(WIN)
            large_font = pygame.font.SysFont('comicsans', 40)
            winner = large_font.render('The winner is : ' + str(self.model.winner), True, (255, 255, 255))
            WIN.blit(winner, (650 / 2 - winner.get_width() / 2, 200))
            pygame.display.update()
        pygame.quit()

    def update(self):
        self.view.draw_board(WIN, self.model.board)
        self.view.draw_valid_moves(WIN, self.model.valid_moves)
        pygame.display.update()

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        print(x, y)
        if y >= HEIGHT - 5 or x >= WIDTH - 5:
            return 0, 0
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col


if __name__ == '__main__':
    FPS = 60
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Checkers')

    checkers = Controller()
    checkers.main()
