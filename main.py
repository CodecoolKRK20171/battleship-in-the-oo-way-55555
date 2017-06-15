from ocean import Ocean
import ship
import square
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

        new_player = input("Enter name of player 1:\n")
        new_player2 = input("Enter name of player 2:\n")

        statek = player.Player(new_player)
        nowe_statki = statek.starting_positions_ships()

        ocean_player = Ocean()
        print(nowe_statki[0])
        # nowe_statki[0][0], nowe_statki[0][1], nowe_statki[0][2], nowe_statki[0][3]
        ocean_player.add_ship(*nowe_statki[0])
        ocean_player.fill_board()
        print(ocean_player)

        print(statek)

        # ocean_opponent = Ocean()
        # ocean_player = Ocean()
        #
        # print("===================================================")
        # print("Your ships")
        # print("===================================================")
        #
        # ocean_player.fill_board()
        # print(ocean_player)
        #
        # print("===================================================")
        # print("Try hit ship of your opponent")
        # print("===================================================")
        #
        # ocean_opponent.fill_board()
        # print(ocean_opponent)
        ocean_player.add_ship()
    else:
        print('Wrong sign, try again')


if __name__ == "__main__":
    main()
