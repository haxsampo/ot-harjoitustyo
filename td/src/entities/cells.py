from global_values import SCREEN_HEIGHT, SCREEN_WIDTH, CELL_SIZE

class Cells:
    """
    Creates a list of lists that represent self.cell_size sized cells.
    The values in the lists represent whether the cell is blocked for building and pathing purposes.
    """

    def __init__(self, initial_value, scrn_height=SCREEN_HEIGHT,
                 scrn_width=SCREEN_WIDTH, cell_size=CELL_SIZE):
        """
        Args:
        initial_value (int): what value cells shall be given in initialization
        self.scrn_height (int): default from global_values, defines cells y len
        scrn_width (int):default from global_values, defines cells x len
        self.cell_size:default from global_values, defines the size of on rectangular cell
        """
        self.scrn_width = scrn_width
        self.scrn_height = scrn_height
        self.cell_size = cell_size
        self.cells = [0]* int(self.scrn_height/self.cell_size)
        for i in range(0, len(self.cells), 1):
            x_list = [initial_value] * int(scrn_width/self.cell_size)
            self.cells[i] = x_list

    def cell_value(self, x_pos, y_pos):
        """
        Takes any coordinates, and gets the value of the representative cell
        Args:
        x_pos (int): pixel width
        y_pos (int): pixel height
        return (int): the value of the cell in question
        0 = empty, 1 = tower/blocked
        """
        if x_pos < 0 or y_pos < 0:
            return 1
        if x_pos > self.scrn_width or y_pos > self.scrn_height:
            return 1
        x_cellified = int((x_pos - (x_pos % self.cell_size))/self.cell_size)
        y_cellified = int((y_pos - (y_pos % self.cell_size))/self.cell_size)
        if x_cellified > len(self.cells[0])-1 or y_cellified > len(self.cells)-1:
            return 1
        ret_val = self.cells[y_cellified][x_cellified]
        return ret_val

    def cell_value_in_cells(self, x_pos, y_pos):
        """
        Takes in the coordinates in cell numbers, not in pixels
        Args:
        x_pos (int): n:th cell in width
        y_pos (int): m:th cell in height
        return (int): the value of the cell in question
        0 = empty, 1 = tower/blocked
        """
        return self.cells[y_pos][x_pos]

    def tower_fits(self, x_pos, y_pos, tower_rect):
        """
        Test whether the given rect fits into the position
        Assumes that towers are rectangular
        Args:
        x_pos (int): position x of mouse click
        y_pos (int): position y of mouse click
        tower_rect (pygame.Rect):
        Returns true if it fits, False if it doesn't
        """

        if not self.tower_in_bounds(x_pos, y_pos, tower_rect):
            return False
        x_cellified, y_cellified = self.coords_to_cell_values(x_pos, y_pos)
        tower_cell_width = int(tower_rect.width / self.cell_size)
        tower_cell_height = int(tower_rect.height / self.cell_size)
        ret_val = True
        for y__ in range(y_cellified, y_cellified+tower_cell_height):
            for x__ in range(x_cellified, x_cellified+tower_cell_width):
                cell_value = self.cells[y__][x__]
                if cell_value != 0:
                    ret_val = False

        return ret_val

    def change_cells_to(self, x_pos, y_pos, rect_area, value):
        """
        Changes cell values of given area to given value
        Does not check whether the rect fits or not, use tower_fits()
            and tower_in_bounds() for that
        Args:
        x_pos, y_pos (int): click values, starting cell calculated from these
        rect_area (pygame.Rect): what area do we want to cover to be changed
        value (int): what value the cells should be after the change
        """
        x_cellified, y_cellified = self.coords_to_cell_values(x_pos, y_pos)
        tower_cell_width = int(rect_area.width / self.cell_size)
        tower_cell_height = int(rect_area.height / self.cell_size)
        range_for_y = self._roof_for_cell_index(y_cellified, [tower_cell_height], 'y')
        range_for_x = self._roof_for_cell_index(x_cellified, [tower_cell_width], 'x')
        for y__ in range(y_cellified, range_for_y):
            for x__ in range(x_cellified, range_for_x):
                self.cells[y__][x__] = value

    def _roof_for_cell_index(self, cellified_value, list_to_sum, x_or_y):
        """
        x_or_y (str): x or y
        """
        max_y = len(self.cells)
        max_x = len(self.cells[0])
        total = cellified_value
        for summ in list_to_sum:
            total += summ
        if x_or_y == 'x':
            if total > max_x:
                return max_x
            else:
                return total
        else:
            if total > max_y:
                return max_y
            else:
                return total


    def coords_to_cell_values(self, x_pos, y_pos):
        """
        Changes pixel coordinates to cell values
        """
        if x_pos < 0 or y_pos < 0:
            print("passing negative values to cells.coords_to_cell_values")
            return 0, 0
        x_cellified = int((x_pos - (x_pos % self.cell_size))/self.cell_size)
        y_cellified = int((y_pos - (y_pos % self.cell_size))/self.cell_size)
        if x_pos > self.scrn_width:
            new_x = self.scrn_width-1
            x_cellified = int((new_x - (new_x % self.cell_size))/self.cell_size)
        if y_pos > self.scrn_height:
            new_y = self.scrn_height -1
            y_cellified = int((new_y - (new_y % self.cell_size))/self.cell_size)
        return x_cellified, y_cellified

    def tower_in_bounds(self, event_x, event_y, rect):
        """
        Is the given rectangle within bounds of the screen width & height
        Args:
        event_x (int):
        event_y (int):
        rect (pygame.Rect):
        """
        twr_x = int(event_x - (event_x % 5))
        twr_y = int(event_y - (event_y % 5))
        if rect.width + twr_x > self.scrn_width:
            return False
        if rect.height + twr_y > self.scrn_height:
            return False
        return True

    def get_neighbours(self, location):
        """
        Returns a list of tuples, given loc neighbour cell left upper corner locations that
            are within bounds
        Args:
        location ((int,int), tuple): in cells
        Return:
        list of class Cell
        """
        x_pos = location[0]
        y_pos = location[1]
        ret = []
        if x_pos-5 >= 0:
            left = (x_pos-5, y_pos)
            ret.append(left)
        if y_pos-5 >= 0:
            up_ = (x_pos, y_pos-5)
            ret.append(up_)
        if x_pos+5 < self.scrn_width:
            right = (x_pos+5, y_pos)
            ret.append(right)
        if y_pos+5 < self.scrn_height:
            down = (x_pos, y_pos+5)
            ret.append(down)
        return ret

    def reconfirm_cell_values_per_sprite(self, sprites):
        """
        Takes a sprite list and affirms that the values
        in the sprite rect area are blocked
        sprites (pygame.sprite.group)
        """
        for sprite in sprites:
            self.change_cells_to(sprite.rect.x,
                                 sprite.rect.y,
                                 sprite.rect,
                                 1)
