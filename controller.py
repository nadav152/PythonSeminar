from model import Model
from view import View
from constants import *
from ResumableTimer import ResumableTimer


class Controller:

    def __init__(self):
        self.reset_self_values()

    def reset_self_values(self):
        """"
        reset all values for new game
        """
        self.model = Model()
        self.view = View()
        self.seconds_black = 0
        self.minutes_black = 20
        self.seconds_white = 0
        self.minutes_white = 0
        self.rematch = False

    def start_game(self):
        """"
        Start Screen, Instructions and "Start" button
        """
        run = True
        start = False
        while run:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                # mouse pressed on start game
                if event.type == pygame.MOUSEBUTTONDOWN and (
                        380 + 100 > mouse[0] > 380 and 500 + 40 > mouse[1] > 500):
                    start = True
                    run = False

            self.view.draw_menu(WIN)
            pygame.display.update()
        if start:
            self.main()
        pygame.quit()

    def main(self):
        """"
        Run the checkers game
        """
        run = True
        clock = pygame.time.Clock()

        time_white = ResumableTimer()
        time_black = ResumableTimer()
        self.start_timers(time_black, time_white)
        white_timer_flag = False
        black_timer_flag = False
        instructions = False
        quit_game = False
        while run:
            clock.tick(FPS)
            # Updating player timers
            run, black_timer_flag, white_timer_flag = \
                self.update_players_timers(black_timer_flag, run, time_black, time_white, white_timer_flag)

            pos = pygame.mouse.get_pos()
            if self.model.check_winner() is not None:
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 810 + 30 > pos[0] > 810 and 12 + 30 > pos[1] > 12:
                        run = False
                        instructions = True
                        break
                self.check_game_events(event, pos)
            self.update_game()
        if instructions:
            self.reset_self_values()
            self.start_game()
        elif quit_game:
            pygame.quit()
        else:
            self.show_winner()
            self.check_for_rematch()

    def start_timers(self, time_black, time_white):
        """"
        Initialize timers to pause and resume
        """
        time_white.start()
        time_white.pause()
        time_black.start()
        time_black.pause()

    def check_game_events(self, event, pos):
        """"
        check if undo or player movement
        """
        if event.type == pygame.MOUSEBUTTONDOWN and (
                700 + 250 > pos[0] > 700 and 250 + 50 > pos[1] > 250):
            self.model.undo()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            row, col = self.get_row_col_from_mouse(pos)
            self.model.select_area(row, col)

    def update_players_timers(self, black_timer_flag, run, time_black, time_white, white_timer_flag):
        """"
        update resume and pause timers for each player
        """
        if self.model.turn == WHITE:
            black_timer_flag, run, white_timer_flag = self.set_white_player_timer(black_timer_flag, run, time_black,
                                                                                  time_white, white_timer_flag)
        else:
            black_timer_flag, run, white_timer_flag = self.set_black_player_timer(black_timer_flag, run, time_black,
                                                                                  time_white,
                                                                                  white_timer_flag)
        return run, black_timer_flag, white_timer_flag

    def set_white_player_timer(self, black_timer_flag, run, time_black, time_white, white_timer_flag):
        """"
        pause and resume white timer
        """
        if not black_timer_flag:
            time_black.pause()
            black_timer_flag = True
        white_timer_flag = False
        time_white.resume()
        timer_white = time_white.get()
        self.seconds_white = 60 - (timer_white % 60)
        self.minutes_white = MINUTES_PER_PLAYER - timer_white / 60
        if int(self.minutes_white) == 0 and int(self.seconds_white) == 0:
            self.model.winner = "BLACK"
            run = False
        return black_timer_flag, run, white_timer_flag

    def set_black_player_timer(self, black_timer_flag, run, time_black, time_white, white_timer_flag):
        """"
        pause and resume black timer
        """
        if not white_timer_flag:
            time_white.pause()
            white_timer_flag = True
        black_timer_flag = False
        time_black.resume()
        timer_black = time_black.get()
        self.seconds_black = 60 - (timer_black % 60)
        self.minutes_black = MINUTES_PER_PLAYER - timer_black / 60
        if int(self.minutes_black) == 0 and int(self.seconds_black) == 0:
            self.model.winner = "WHITE"
            run = False
        return black_timer_flag, run, white_timer_flag

    def check_for_rematch(self):
        """"
        run new game if selected rematch
        """
        if self.rematch:
            self.reset_self_values()
            self.main()
        else:
            pygame.quit()

    def show_winner(self):
        """"
        Run winner screen with buttons "YES", "NO".
        """
        run = True
        while run:
            pygame.time.delay(100)
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                # mouse pressed on rematch
                if event.type == pygame.MOUSEBUTTONDOWN and (
                        250 + 100 > mouse[0] > 250 and 400 > mouse[1] > 350):
                    self.rematch = True
                    run = False

                # mouse pressed on end game
                if event.type == pygame.MOUSEBUTTONDOWN and (
                        450 + 100 > mouse[0] > 450 and 350 + 50 > mouse[1] > 350):
                    run = False
            self.view.draw_rematch(WIN)
            self.view.draw_winner(WIN, self.model.winner)
            pygame.display.update()

        self.check_for_rematch()

        pygame.quit()

    def update_game(self):
        """"
        update and draw game screen
        """
        self.view.draw_game(WIN, self.model.board)
        self.view.draw_valid_moves(WIN, self.model.valid_moves)
        self.view.draw_undo(WIN, self.model.turn, self.model.first_turn, self.model.black_undo_left, self.model.white_undo_left)
        self.view.draw_remain_undoes(WIN, self.model.white_undo_left, self.model.black_undo_left)
        self.view.draw_timers(WIN, self.minutes_white, self.seconds_white, self.minutes_black, self.seconds_black)
        pygame.display.update()

    def get_row_col_from_mouse(self, pos):
        """"
        calculate x, y by mouse's postion
        """
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
    checkers.start_game()
