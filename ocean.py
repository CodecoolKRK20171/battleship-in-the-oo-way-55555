from ship import Ship
import player


class Ocean:

    def __init__(self):
        self.ships = []
        self.board = []

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.board])

    def add_ship(self, position_x, position_y, size, is_horizontal=False):
        positions = []

        for i in range(size):
            if is_horizontal:
                print("ok")
                position_x += 1
            else:
                print("nie sok")
                position_y += 1
            positions.append((position_x, position_y))
            print(positions)

        positions = tuple(positions)
        print(positions)
        self.ships.append(Ship(positions))

    def fill_board(self):

        letters = [' A ', ' B ', ' C ', ' D ', ' E ', ' F ', ' G ', ' H ', ' I ', ' J ']
        print(' '.join(letters))
        for i in range(0, 10):
            self.board.append([' ~ ']*10 + [str(i+1)])

        for ship in self.ships:
            for square in ship.squares:
                self.board[square.column][square.row] = str(square)
