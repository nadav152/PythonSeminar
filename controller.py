from model import Model
from view import View
from constants import *
import time as time1
import time as time2
from ResumableTimer import ResumableTimer
class Controller:

    def __init__(self):
        self.reset_self_values()
        self.seconds_black = 0
        self.minutes_black = 20
        self.seconds_white = 0
        self.minutes_white = 0

    def reset_self_values(self):
        self.model = Model()
        self.view = View()
        self.rematch = False

    def main(self):
        run = True
        clock = pygame.time.Clock()

        time_white = ResumableTimer()
        time_black = ResumableTimer()
        time_white.start()
        time_white.pause()
        time_black.start()
        time_black.pause()
        white_timer_flag = False
        black_timer_flag = False
        while run:
            clock.tick(FPS)

            if self.model.turn == WHITE:
                if not black_timer_flag:
                    time_black.pause()
                    black_timer_flag = True

                white_timer_flag = False
                time_white.resume()
                timer_white = time_white.get()

                self.seconds_white = 60 - (timer_white % 60)
                self.minutes_white = MINUTES_PER_PLAYER - timer_white / 60

            else:
                if not white_timer_flag:
                    time_white.pause()
                    white_timer_flag = True

                black_timer_flag = False
                time_black.resume()
                timer_black = time_black.get()

                self.seconds_black = 60 - (timer_black % 60)
                self.minutes_black = MINUTES_PER_PLAYER - timer_black / 60


            pos = pygame.mouse.get_pos()
            if self.model.check_winner() is not None:
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.MOUSEBUTTONDOWN and (
                        700 + 250 > pos[0] > 700 and 250 + 50 > pos[1] > 100):
                    self.model.undo()

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
        self.view.draw_undo(WIN, self.model.turn)
        self.view.draw_remain_undoes(WIN, self.model.white_undo_left, self.model.black_undo_left)
        self.view.draw_timer(WIN, self.minutes_white, self.seconds_white, self.minutes_black, self.seconds_black)
        pygame.display.update()

    def get_row_col_from_mouse(self, pos):
        x, y = pos
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
