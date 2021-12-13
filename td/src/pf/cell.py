import collections

class Cell:
    '''
    Args:
    x_pos (int)
    y_pos (int)
    value (int): 0 empy; 1 full
    '''

    def __init__(self, x_pos, y_pos, value):
        self.x = int((x_pos - (x_pos % 5))/5)
        self.y = int((y_pos - (y_pos % 5))/5)
        self.pos = (self.x, self.y)
        self.value = value

    def get_pos(self):
        '''
        Returns tuple(int, int)
        '''
        return self.pos
