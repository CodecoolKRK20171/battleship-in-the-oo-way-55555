from ship import Ship

from square import Square
import sys


class Ocean:
    '''
    class of Ocean objects

    Attributes:
    -----------
    ocean - Ocean obj
    ships = list of Square obj
    h_p = int
    health_points = int
    board = list

    '''

    def __init__(self):
        self.ships = []
        self.hp = 0
        self.board = self.fill_board()
        self.health_points = 17


    def __str__(self):
        ocean_str = ""
        i = -1
        for lista in self.board:
            i += 1
            ocean_str += '|'
            for item in lista:
                ocean_str += str(item)
            ocean_str += '|' + str(i) + "|" + '\n'

        return ocean_str


    def preview_ships(self, position_x, position_y, size, is_horizontal=False):
        '''
        Display board during putting ships on player ocean/board
        '''


    def preview_ships(self, position_x, position_y, size, is_horizontal=False):
        '''
        Method to preview ships coordinates
        '''

        is_hor_good = all([self.board[position_y][position_x-1+j].is_empty for j in range(size)])

        is_ver_good = all([self.board[position_y+j][position_x-1].is_empty for j in range(size)])

        if is_hor_good == False or is_ver_good == False:
            print("zle")

        for i in range(size):

            if is_horizontal:
                if is_hor_good:
                    self.board[position_y][position_x-1].fill_square()
                    self.board[position_y][position_x-1].set_as_ship()
                    position_x += 1
            else:
                if is_ver_good:
                    self.board[position_y][position_x-1].fill_square()
                    self.board[position_y][position_x-1].set_as_ship()
                    position_y += 1


    def add_ships(self, position_x, position_y, size, is_horizontal=False):
        '''
        Method take starting position of ship and append it to ocean board
        '''

        for i in range(size):

            if is_horizontal:
                self.board[position_y][position_x-1].set_as_ship()
                position_x += 1

            else:
                self.board[position_y][position_x-1].set_as_ship()
                position_y += 1


    def shot(self, position_x, position_y):
        '''
        Method take coordinates to put square on board, check if player hit ship or not and return message
        Method also check if players still have ships on board
        '''

        self.board[position_y][position_x-1].fill_square()
        if self.board[position_y][position_x-1].is_ship is False:
            print("MISS")

        else:
            print("HIT !")
            self.health_points -= 1
            print(str(self.health_points) + " Health points left")
            if self.health_points == 0:
                sys.exit("GAME OVER")


    def fill_board(self):
        '''
        Fill board with X which represents our ships
        '''

        self.board = []

        letters = [' A ', ' B ', ' C ', ' D ', ' E ', ' F ', ' G ', ' H ', ' I ', ' J ']
        self.board.append(letters)
        for i in range(1, 11):
            self.board.append([])
            for j in range(0,10):

                self.board[i].append(Square(i,j))

        return self.board
