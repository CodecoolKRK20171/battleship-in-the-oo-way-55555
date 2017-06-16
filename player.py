from ocean import Ocean
import os


class Player:
    '''
    class of Player objects

    Attributes:
    -----------
    name = str
    player_ships = dict
    starting_positions = list

    '''

    def __init__(self, name):
        self.name = name
        self.player_ships = {"Carrier(5)": 5, "Battleship(4)": 4, "Cruiser(3)": 3, "Submarine(3)": 3, "Destroyer(3)": 2}
        self.starting_positions = []

    def __str__(self):
        return self.name

    def starting_positions_ships(self):
        '''
        Method to put starting coordinate on board
        '''
        ocean_player = Ocean()
        os.system('clear')
        print(ocean_player)
        for key in self.player_ships:

            print("Enter coordinates of" + " " + key)
            print("(1) Horizontal\n(2) Vertical")

            is_connect = True
            while is_connect:

                horizontal = input("Select direction:\n")

                if horizontal == "1":
                    horizontal = True
                elif horizontal == "2":
                    horizontal = False
                else:
                    continue

                numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

                position_x = input("Enter x position:")

                while position_x not in numbers:
                    position_x = input("Enter x position:")

                position_y = input("Enter y position:")

                while position_y not in numbers:
                    position_y = input("Enter y position:")

                position_x = int(position_x)
                position_y = int(position_y)

                positions = (position_x,
                             position_y,
                             self.player_ships[key],
                             horizontal)

                if ocean_player.board[positions[1]][positions[0]-1].is_empty is False:
                    print("WRONG CORDS!")
                    continue

                else:

                    is_connect = False

            self.starting_positions.append(positions)
            os.system('clear')

            ocean_player.preview_ships(*positions)
            ocean_player.add_ships(*positions)

            print(ocean_player)

        return self.starting_positions
