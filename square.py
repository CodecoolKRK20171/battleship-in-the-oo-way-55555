class Square:
    '''
    class of Square objects

    Attributes:
    -----------
    row = int
    column = int
    is_empty = bool
    is_ship = bool

    '''
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.is_empty = True
        self.is_ship = False

    def fill_square(self):
        '''
        Method to fill boad with square
        '''
        self.is_empty = False


    def set_as_ship(self):
        '''
        Method to put ship on board
        '''
        self.is_ship = True


    def __str__(self):
        h = []

        if self.is_empty:
            mark = ' ~ '
        else:
            if self.is_ship:

                mark = ' X '
                h.append(mark)

            else:
                mark = ' 0 '

        return mark
