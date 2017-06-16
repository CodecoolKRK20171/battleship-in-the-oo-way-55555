from ocean import Ocean
import os


class Player:

    def __init__(self, name):
        self.name = name
        self.player_ships = {"Carrier(5)": 5, "Battleship(4)": 4, "Cruiser(3)": 3,
                             "Submarine(3)": 3, "Destroyer(3)": 2}
        self.starting_positions = []

    def __str__(self):
        return self.name

    def starting_positions_ships(self):
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

                positions = (int(input("Enter x position:\n")),
                             int(input("Enter y position:\n")),
                             self.player_ships[key],
                             horizontal)

                if ocean_player.board[positions[1]][positions[0]-1].is_empty == False:
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
