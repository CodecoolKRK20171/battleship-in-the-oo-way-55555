from ocean import Ocean
import player
import os


def main_menu():

    print("""
    Welcome in battle ship game!

    1. Start new game
    2. Exit
    """)


def main():
    os.system('clear')
    main_menu()
    chose_number = input("Enter number:\n")

    if chose_number == '1':
        os.system('clear')
<<<<<<< HEAD
        new_player = input("Enter name of player 1:\n")
        statek = player.Player(new_player)
        nowe_statki = statek.starting_positions_ships()
        ocean_player = Ocean()
        for s in nowe_statki:
            ocean_player.add_ships(*s)
=======

        new_player1 = input("Enter name of player 1:\n")
        new_player2 = input("Enter name of player 2:\n")

        ship1 = player.Player(new_player1)
        new_ships1 = ship1.starting_positions_ships()

        ocean_player1 = Ocean()
        for s in new_ships1:
            ocean_player1.add_ships(*s)
>>>>>>> 1c81ecf2333c49203b68c32e211fb2f68b0c21a5

        ship2 = player.Player(new_player2)
        new_ships2 = ship2.starting_positions_ships()

        ocean_player2 = Ocean()
        for s in new_ships2:
            ocean_player2.add_ships(*s)

        os.system('clear')
        print("GOOD LUCK")
        while True:

            turn = 1

            while turn == 1:
                radius = range(1, 11)
                print("==================================")
                print("Your ships", new_player1)
                print("==================================")
                print(ocean_player1)
                shot = (int(input("Enter x:\n")), int(input("Enter y:\n")))
                if shot[0] not in radius or shot[1] not in radius:
                    continue

                os.system('clear')
                ocean_player1.shot(shot[0], shot[1])
                print(ocean_player1)
                pauza = input()
                os.system('clear')

                turn = 2

            while turn == 2:
                radius = range(1, 11)
                print("==================================")
                print("Your ships", new_player2)
                print("==================================")
                print(ocean_player2)
                shot = (int(input("Enter x:\n")), int(input("Enter y:\n")))
                if shot[0] not in radius or shot[1] not in radius:
                    continue

                os.system('clear')
                ocean_player2.shot(shot[0], shot[1])
                print(ocean_player2)
                pauza = input()
                os.system('clear')

                break

    else:
        print('Wrong sign, try again')


if __name__ == "__main__":
    main()
