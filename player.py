from ocean import Ocean


class Player:

    def __init__(self, name):
        self.name = name
        self.player_ships = {"Carrier(5)": 5}
        """Battleship(4)": 4, "Cruiser(3)": 3, "Submarine(3)": 3, "Destroyer(3)": 2}"""
        self.starting_positions = []

    def __str__(self):
        return self.name

    def starting_positions_ships(self):
        ocean_player = Ocean()

        for key in self.player_ships:

            print("Enter coordinates of" + " " + key)

            while True:
                print("(1) Horizontal\n(2) Vertical")

                horizontal = input("Select direction:\n")

                if horizontal == "1":
                    horizontal = True
                    break
                elif horizontal == "2":
                    horizontal = False
                    break
                else:
                    continue

            while True:
                pos_x = int(input("Enter x position:\n"))
                if pos_x > 10 or pos_x <= 0:
                    continue
                else:
                    break

            while True:
                pos_y = int(input("Enter y position:\n"))
                if pos_y > 10 or pos_y <= 0:
                    continue
                else:
                    break

            positions = (pos_x, pos_y, self.player_ships[key], horizontal)
            print(positions)

            self.starting_positions.append(positions)

            print("")
            ocean_player.add_ship(*positions)
            ocean_player.fill_board()
            print(ocean_player)
            print("")

        print(self.starting_positions)
        return self.starting_positions
