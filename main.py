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
        new_player = input("Enter name of player 1:\n")
        statek = player.Player(new_player)
        nowe_statki = statek.starting_positions_ships()
        ocean_player = Ocean()
        for s in nowe_statki:
            ocean_player.add_ships(*s)



        os.system('clear')
        print("GOOD LUCK")
        while True:
            radius = range(1,11)
            print("==================================")
            print("Your ships")
            print("==================================")
            print(ocean_player)
            shot = (int(input("Enter x:\n")), int(input("Enter y:\n")))
            if shot[0] not in radius or shot [1] not in radius:
                continue
            os.system('clear')
            ocean_player.shot(shot[0],shot[1])



    else:
        print('Wrong sign, try again')


if __name__ == "__main__":
    main()
