class State:

    def __init__(self, board, black_left, white_left, black_kings, white_kings, turn):
        self.board = board
        self.black_left = black_left
        self.white_left = white_left
        self.black_kings = black_kings
        self.white_kings = white_kings
        self.turn = turn


class Memento:

    def __init__(self):
        self.states = []

    def push(self, board, black_left, white_left, black_kings, white_kings, turn):
        self.states.append(State(board, black_left, white_left, black_kings, white_kings, turn))

    def redo(self):
        if self.states:
            return self.states.pop()
        pass
