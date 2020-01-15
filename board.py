class Board:
    counters = {
        0: "X",
        1: "O"
    }

    def __init__(self, size):
        try:
            self.__board_size = max(1, size)
            self.__board = [
                [' '] * self.__board_size for _ in range(self.__board_size)]
            self.__NUM_OF_CELLS = pow(size, 2)
        except:
            raise TypeError(f"size must be int, found {type(size)}")

    def __str__(self):
        return ('\n' + '- ' * self.__board_size + '\n').join(["|".join(row) for row in self.__board])

    def display_board(self):
        return self.__str__()

    def __set_cell(self, counter, position):
        self.__board[position // self.__board_size][position %
                                                    self.__board_size] = Board.counters.get(counter, 'X')

    def __check_cell(self, position):
        return self.__board[position // self.__board_size][position % self.__board_size] == ' '

    """Sets the cell to the counter"""

    def make_move(self, counter, cell):
        # clamp function to validate choice
        position = max(min(self.__NUM_OF_CELLS, cell - 1), 0)
        if self.__check_cell(position):
            self.__set_cell(counter, position)
            return True
        return False

    def check_win(self):

        def check_set(value_line): return set(value_line) == {
            'X'} or set(value_line) == {'O'}

        for col, row in enumerate(self.__board):
            if check_set(row):  # check horizontal win
                return True

            elif check_set([x[col] for x in self.__board]):  # check vertical win
                return True

        # check forward diagonal
        if check_set([self.__board[x][x] for x in range(self.__board_size)]):
            return True

        # check backward diagonal
        if check_set([self.__board[x][self.__board_size - 1 - x] for x in range(self.__board_size)]):
            return True
        return False
