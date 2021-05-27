from constants import *
from piece import Piece
from memento import Memento
from pygame import mixer


class Model:
    def __init__(self):
        self.board = []
        self.black_left = self.white_left = 12
        self.black_undo_left = self.white_undo_left = 3
        self.black_kings = self.white_kings = 0
        self.create_board_array()
        self.valid_moves = {}
        self.turn = WHITE
        self.selected_piece = None
        self.winner = None
        self.board_stack = []
        self.first_turn = True
        self.memento = Memento()

    def undo(self):
        """"
        return board's state to last turn
        """
        state = self.memento.undo()

        if state:

            if self.player_can_undo(self.turn):
                self.board = state.board
                self.black_left = state.black_left
                self.white_left = state.white_left
                self.black_kings = state.black_kings
                self.white_kings = state.white_kings
                self.turn = state.turn
                self.first_turn = state.first_turn
                self.valid_moves = {}

    def create_board_array(self):
        """"
        initialize board with pieces
        """
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, WHITE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def select_area(self, row, col):
        """"
        select square and check moves
        :param col: column location
        :param row: row location
        :return True if can move
        """
        if self.selected_piece and (row, col) in self.valid_moves:
            self.memento.push(self.board, self.black_left, self.white_left, self.black_kings, self.white_kings,
                              self.turn, self.first_turn)
            result = self.check_possible_movement(row, col)

            if not result:
                self.selected_piece = None
                self.select_area(row, col)

        piece = self.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected_piece = piece
            self.valid_moves = self.get_valid_moves(piece)
            return True

        return False

    def check_possible_movement(self, row, col):
        """"
        check if piece can move to the square in (row, col)
        :param col: new column location
        :param row: new row location
        :return: True if can move
        """
        piece = self.get_piece(row, col)  # check if square is empty
        if self.selected_piece and piece == 0 and (row, col) in self.valid_moves:
            self.update_model_location(self.selected_piece, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.remove(skipped)
                mixer.music.load('Assets/KillSound.mp3')
                mixer.music.play(1)
            self.change_turn()
        else:
            return False

        return True

    def update_model_location(self, piece, row, col):
        """"
        move piece to new square
        :param col: new column location
        :param row: new row location
        :param piece: one piece on board
        :return:
        """
        # update board array
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], \
                                                                 self.board[piece.row][piece.col]
        # update the current piece values
        piece.move_piece(row, col)

        if row == (ROWS - 1) or row == 0:
            if piece.king is False:
                piece.make_king()
                if piece.color == WHITE:
                    self.white_kings += 1
                else:
                    self.black_kings += 1

    def remove(self, pieces):
        """"
        remove dead pieces from the board
        :param pieces: list of killed pieces
        :return:
        """
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == WHITE:
                    self.white_left -= 1
                else:
                    self.black_left -= 1

    def get_valid_moves(self, piece):
        """"
        get piece's all valid moves
        :param piece: one piece on board
        :return: all piece's valid moves
        """
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == WHITE or piece.king:
            moves.update(self.travese_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self.travese_right(row - 1, max(row - 3, -1), -1, piece.color, right))

        if piece.color == BLACK or piece.king:
            moves.update(self.travese_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self.travese_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def travese_left(self, start, stop, step, color, left, skipped=None):
        """"
        get piece's valid moves to left
        :param skipped: pieces list
        :param left: direction
        :param color: piece color
        :param step: piece step
        :param stop: where piece stop
        :param start: where piece start
        :return: all piece's valid moves to left
        """
        if skipped is None:
            skipped = []
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self.travese_left(r + step, row, step, color, left - 1, skipped=moves[(r, left)]))
                    moves.update(self.travese_right(r + step, row, step, color, left + 1, skipped=moves[(r, left)]))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        return moves

    def travese_right(self, start, stop, step, color, right, skipped=None):
        """"
        get piece's valid moves to right
        :param skipped: pieces list
        :param right: direction
        :param color: piece color
        :param step: piece step
        :param stop: where piece stop
        :param start: where piece start
        :return: all piece's valid moves to right
        """
        if skipped is None:
            skipped = []
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self.travese_left(r + step, row, step, color, right - 1, skipped=moves[(r, right)]))
                    moves.update(self.travese_right(r + step, row, step, color, right + 1, skipped=moves[(r, right)]))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        return moves

    def change_turn(self):
        """"
        change player turn
        """
        self.valid_moves = {}
        if self.first_turn:
            self.first_turn = False
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def check_winner(self):
        """"
       check if game is finished and who is the winner
        """
        if self.white_left == 0:
            self.winner = 'BLACK'
            return BLACK
        elif self.black_left == 0:
            self.winner = 'WHITE'
            return WHITE

        return None

    def check_no_piece_can_move(self, color):
        """"
        Check for situation no piece can move in player turn. means automatic lose. checks draw also.
        :param color: player's turn
        :return: True if no possible moves to any piece -> auto lose.
        """
        if self.white_left == 0 or self.black_left == 0:
            return False

        white_can_move = False
        black_can_move = False
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    moves = self.get_valid_moves(piece)
                    if moves:
                        if piece.color is WHITE:
                            white_can_move = True
                        else:
                            black_can_move = True

        if not black_can_move and not white_can_move:
            self.white_left = 0
            self.black_left = 0
            return True

        if not black_can_move and color == BLACK:
            self.black_left = 0
        elif not white_can_move and color == WHITE:
            self.white_left = 0

        return True

    def get_piece(self, row, col):
        return self.board[row][col]

    def player_can_undo(self, turn):
        """"
        check if player can undo
        :param turn: player's turn
        :return true if the player can do undo
        """
        if turn == BLACK and self.white_undo_left > 0:
            self.white_undo_left -= 1
            return True

        elif turn == WHITE and self.black_undo_left > 0:
            self.black_undo_left -= 1
            return True
        else:
            return False
