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

        player1 = input("Enter name of player 1:\n")
        player2 = input("Enter name of player 2:\n")

        if player1 == player1:
            player1_board = player.Player(player1)
            add_ships = player1_board.starting_positions_ships()

            ocean_player1 = Ocean()
            for s in add_ships:
                print(s)
                ocean_player1.add_ship(*s)

        os.system('clear')
        if player2 == player2:
            player2_board = player.Player(player2)
            add_ships = player2_board.starting_positions_ships()

            ocean_player2 = Ocean()
            for item in add_ships:
                ocean_player2.add_ship(*item)

        # print("===================================================")
        # print("Your ships")
        # print("===================================================")
        #
        # ocean_player.fill_board()
        # print(ocean_player)
        # print(" ")
        #
        # shot = (int(input("Enter x:\n")), int(input("Enter y:\n")))
        # print(shot)
        # ocean_player.shot(*shot)
        # ocean_player.fill_board()
        # print(ocean_player)
        #
        # print("===================================================")
        # print("Try hit ship of your opponent")
        # print("===================================================")

    else:
        print('Wrong sign, try again')


if __name__ == "__main__":
    main()
