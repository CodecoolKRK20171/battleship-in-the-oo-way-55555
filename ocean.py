from ship import Ship
# import square


class Ocean:

    def __init__(self):
        self.ships = []
        self.board = []
        self.shots = []

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.board])

    def add_ship(self, position_x, position_y, size, is_horizontal=False):
        positions = []

        for i in range(size-1):
            positions.append((position_x-1, position_y-1))
            if is_horizontal:
                position_x += 1
            else:
                position_y += 1
            positions.append((position_x-1, position_y-1))

        positions = tuple(positions)
        self.ships.append(Ship(positions))

    def shot(self, position_x, position_y):

        positions = [(position_x-1, position_y-1)]
        positions = tuple(positions)

        self.shots.append(Ship(positions))

    def fill_board(self):
        self.board = []

        letters = [' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' I', ' J']
        print(' '.join(letters))
        for i in range(0, 10):
            self.board.append([' ~ ']*10 + [str(i+1)])

        for ship in self.ships:
            for square in ship.squares:
                self.board[square.column][square.row] = str(square)

    def fill_board_shot(self):

        for shot in self.shots:
            for square in shot.squares:
                square.mark()
                self.board[square.column][square.row] = str(square)
