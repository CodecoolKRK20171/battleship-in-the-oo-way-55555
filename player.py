

class Player:

    def __init__(self, name):
        self.name = name
        self.player_ships = {"Carrier": 5, "Battleship": 4, "Cruiser": 3,
                             "Submarine": 3, "Destroyer": 2}
        self.starting_positions = []

    def __str__(self):
        return self.name

    def starting_positions_ships(self):

        for key in self.player_ships:
            print("(1) Horizontal\n(2) Vertical")
            horizontal = input("Select direction:\n")

            if horizontal == "1":
                horizontal = True
            elif horizontal == "2":
                horizontal = False

            print("Enter coordinates of" + " " + key)
            positions = (int(input("Enter x position:\n")),
                         int(input("Enter y position:\n")),
                         self.player_ships[key],
                         horizontal)

            self.starting_positions.append(positions)

        print(self.starting_positions)
        return self.starting_positions
