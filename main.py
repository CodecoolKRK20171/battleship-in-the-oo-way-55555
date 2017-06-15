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

        player1 = input("Enter name of player 1:\n")
        player2 = input("Enter name of player 2:\n")

        if player1 == player1:

            ocean_player1 = Ocean()
            player1_board = player.Player(player1)
            add_ships = player1_board.starting_positions_ships()

            for ships in add_ships:
                ocean_player1.add_ship(*ships)
            ocean_player1.fill_board()

        os.system('clear')

        if player2 == player2:

            ocean_player2 = Ocean()
            player2_board = player.Player(player2)
            add_ships = player2_board.starting_positions_ships()

            for ships in add_ships:
                ocean_player2.add_ship(*ships)
            ocean_player2.fill_board()

        while True:
            os.system('clear')
            print("===================================================")
            print("Try hit ship of your opponent")
            print("===================================================")
            print(ocean_player2)

            print("===================================================")
            print("Your ships")
            print("===================================================")
            print(ocean_player1)

            print("Enter coordinates to fire commander!")
            turn_player1 = (int(input("Enter x coordinate:\n")), int(input("Enter y coordinate:\n")))
            ocean_player2.shot(*turn_player1)

            ocean_player2.fill_board_shot()
            print(ocean_player2)

    else:
        print('Wrong sign, try again')


if __name__ == "__main__":
    main()
