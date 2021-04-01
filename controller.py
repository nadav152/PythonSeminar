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

            if self.model.winner() is not None:
                if self.model.winner() == WHITE:
                    print("WHITE WINS!!")
                else:
                    print("BLACK WINS!!")

                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_row_col_from_mouse(pos)
                    self.model.select(row, col)

            self.update()

        pygame.quit()

    def update(self):
        self.view.draw_board(WIN, self.model.board)
        self.view.draw_valid_moves(WIN, self.model.valid_moves)
        pygame.display.update()

    def remove(self, pieces):
        for piece in pieces:
            self.model.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == WHITE:
                    self.model.white_left -= 1
                else:
                    self.model.black_left -= 1

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
    WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    pygame.display.set_caption('Checkers')

    checkers = Controller()
    checkers.main()
