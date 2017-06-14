class Player:
    def player_add_ship (player="player1"): #tak samo bedzie dla player2
        print("Welcome")
        ship_list = ["1. Destroyer", "2. Submarine", "3. Cruiser", "4. Battleship", "5. Carrier"]

        while ship_list != []:
            for i in ship_list:
                print(i)
            chose_ship = (input("Chose ship to input:\n"))
            if chose_ship == "1" and "1. Destroyer" in ship_list:
                #potrzebna funkcja wstawiania statku
                #prawdopodobnie ocean.add_ship()
                ship_list.remove("1. Destroyer")

            elif chose_ship == "2" and "2. Submarine" in ship_list:
                #potrzebna funkcja wstawiania statku
                ship_list.remove("2. Submarine")

            elif chose_ship == "3" and "3. Cruiser" in ship_list:
                #potrzebna funkcja wstawiania statku
                ship_list.remove("3. Cruiser")

            elif chose_ship == "4" and "4. Battleship" in ship_list:
                #potrzebna funkcja wstawiania statku
                ship_list.remove("4. Battleship")

            elif chose_ship == "5" and "5. Carrier" in ship_list:
                #potrzebna funkcja wstawiania statku
                ship_list.remove("5. Carrier")

            if ship_list != []: print("Next choose\n")
            pass
    pass
