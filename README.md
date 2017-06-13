# Battleship in the OOP way

## The story

    1. As users we would like to enter our names.
    2. Enter ships on our 2 different boards.
    3. Players will start randomly.
    4. Enter positions of shooting:
        - if player miss, he lost his turn
        - if player hit the ship of opponent, he can try another shot
    5. While player take down all parts of ship he get a message.
    6. While player take all ships of his opponent, he give a   message about WIN!


## Specification

__main.py__


_square.py_
### Class Square

__Attributes__

* `is_marked`

Bool with starting False value


__Instance methods__

* `__init__(self, row, column, is_marked)`
Construct a piece of ship, and checking if player try shoot on this positions before

* `life`
Check if player still have ships/squares on board



_ship.py_
###Class ship

__Attributes__

* `positions`
    - positions x, y

* `squares`
    - list of tuples positions of ships

__Instance Methods__

* `__init__(self, positions)`


_ocean.py_
### Class ocean

__Attributes__

* `ships`
list

* `board`
list

__Instance methods__

* `__init__(self, ships, board)`
Create an object is a game board.

* `fill_board`
Create a empty template, than fill it up with ships.

* `add_ship`
Take start position parameters and create ship.


_player.py_
###Class

__Attributes__

* `name`
Contain name of Players
