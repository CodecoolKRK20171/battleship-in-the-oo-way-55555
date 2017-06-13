from ocean import Ocean
from ship import Ship
from square import Square
from player import Player
import os


def main_menu():

    print("""
    Welcome in battle ship game!

    1. Start new game
    2. Exit
    """)


def main():
    main_menu()
    chose_number = input("Enter number:\n")

    if chose_number == '1':
        os.system('clear')

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

        ocean_opponent.fill_board()
        print(ocean_opponent)

    else:
        print('Wrong sign, try again')


if __name__ == "__main__":
    main()
