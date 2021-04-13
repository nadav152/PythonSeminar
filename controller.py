from model import Model
from view import View
from constants import *


class Controller:

    def __init__(self):
        self.reset_self_values()

    def reset_self_values(self):
        self.model = Model(self)
        self.view = View(self)
        self.rematch = False

    def main(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(FPS)
            pos = pygame.mouse.get_pos()
            if self.model.check_winner() is not None:
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.MOUSEBUTTONDOWN and (
                        700 + 100 > pos[0] > 700 and 100 + 50 > pos[1] > 100):
                    self.model.re_do()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    row, col = self.get_row_col_from_mouse(pos)
                    self.model.select_area(row, col)

            self.update_game()

        self.show_winner()
        self.check_for_rematch()

    def check_for_rematch(self):
        if self.rematch:
            self.reset_self_values()
            self.main()
        else:
            pygame.quit()

    def show_winner(self):
        run = True
        while run:
            pygame.time.delay(100)
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                # mouse pressed on rematch
                if event.type == pygame.MOUSEBUTTONDOWN and (
                        150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450):
                    self.rematch = True
                    run = False

                # mouse pressed on end game
                if event.type == pygame.MOUSEBUTTONDOWN and (
                        450 + 100 > mouse[0] > 450 and 450 + 50 > mouse[1] > 450):
                    run = False

            self.view.draw_winner(WIN, self.model.winner)
            self.view.draw_rematch(WIN)
            pygame.display.update()

    def update_game(self):
        self.view.draw_game(WIN, self.model.board)
        self.view.draw_valid_moves(WIN, self.model.valid_moves)
        self.view.draw_redo(WIN)
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
    WIN = pygame.display.set_mode((WIDTH + 200, HEIGHT))
    pygame.display.set_caption('Checkers')

    checkers = Controller()
    checkers.main()
