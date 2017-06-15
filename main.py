from ocean import Ocean
import ship
import square
from player import Player
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

        player1 = Player(new_player)
        player2 = Player(new_player2)

        ocean_opponent = Ocean()
        ocean_player = Ocean()

        print("===================================================")
        print("Your ships")
        print("===================================================")

        ocean_player.fill_board()
        print(ocean_player)

        print("===================================================")
        print("Try hit ship of your opponent")
        print("===================================================")

        ocean_opponent.add_ship(4, 3, 3, True)
        ocean_opponent.fill_board()
        print(ocean_opponent)

    else:
        print('Wrong sign, try again')


if __name__ == "__main__":
    main()
