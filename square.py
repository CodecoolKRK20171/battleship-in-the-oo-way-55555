import ship


class Square:
    def __init__(self, row, column):
        self.is_marked = True
        self.row = row
        self.column = column

    def __str__(self):

        if self.is_marked:
            mark = ' X '
        else:
            mark = ' 0 '
        return mark

    def mark(self):
        self.is_marked = False
