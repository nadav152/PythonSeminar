from copy import deepcopy


class State:

    def __init__(self, board, black_left, white_left, black_kings, white_kings, turn, first_turn):
        """"
       save as arguments all turn information
        """
        self.board = deepcopy(board)
        self.black_left = black_left
        self.white_left = white_left
        self.black_kings = black_kings
        self.white_kings = white_kings
        self.turn = turn
        self.first_turn = first_turn


class Memento:

    def __init__(self):
        """"
        init stack to save states
        """
        self.states = []

    def push(self, board, black_left, white_left, black_kings, white_kings, turn, first_turn):
        """"
        push state to stack
        """
        self.states.append(State(board, black_left, white_left, black_kings, white_kings, turn, first_turn))

    def undo(self):
        """"
        return last state
        """
        if self.states:
            return self.states.pop()
        pass
