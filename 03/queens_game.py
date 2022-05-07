class Point:
    """
    Represents a point on a board
    A point has an x and y coordinate
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()


class Board:
    """
    An 8x8 chess board.
    Only queens can be placed on the board in a way that they do not attack each other
    the goal is to find all configuration in which you can place 8 queens on the board
    without attacking each other
    """

    def __init__(self):
        """
        Draw an empty board
        setup an array that holds the positons of all of the queens
        setup a cursor
        """
        
        self.queens = []

        # set the cursor to the first point
        self.cursor = None
        
        self.draw_empty_board()

    def draw_empty_board(self):
        self.board = [['E' for x in range(0,8)] for x in range(0,8)]

    def getTile(self, point):
        return self.board[point.x][point.y]

    def setTile(self, point, input):
        self.board[point.x][point.y] = input 

    def getNumberOfEmptySpots(self):
        if self.cursor == None:
            return 64

        counter = 0
        # first row
        for y in range(self.cursor.y, len(self.board[0])):
            if (self.getTile(Point(self.cursor.x, y)) == 'E'):
                counter += 1

        # rest of the board
        for x in range(self.cursor.x + 1, len(self.board)):
            for y in range(0, len(self.board[0])):
                if (self.getTile(Point(x,y)) == 'E'):
                    counter += 1
        return counter

    def draw_queen(self, point = None):
        """
        Draws a queen at the position of the cursor and marks all of the points
        that the queens attacks
        """
        if point == None:
            point = self.cursor

        # if it is not empty, don't move on
        if (self.getTile(point) != 'E'):
            return False
        
        self.draw_attacked_fields(point)

        # draw queen
        self.setTile(point, 'Q')

        # push queen onto the stack
        self.queens.append(Point(point.x, point.y))

    def draw_attacked_fields_horizontal(self, point):
        # marks horizontal
        for x in range(0,len(self.board)):
            self.setTile(Point(x,point.y), "A")

    def draw_attacked_fields_vertical(self, point):
         # marks vertically
        for y in range(0,len(self.board[0])):
            self.setTile(Point(point.x, y), "A")

    def draw_attacked_fields_diagonal(self, point):
        #marks diagonal (from lower left to upper right)
        min_subtract = min(point.x, point.y)
        starting_point = Point(point.x - min_subtract, point.y - min_subtract)

        for i in range(0, 8 - max(starting_point.x, starting_point.y)):
            self.setTile(Point(starting_point.x + i, starting_point.y + i), 'A')

        # marks diagonal from lower right to upper right
        distance_top = point.x
        distance_right = len(self.board[0]) -1 - point.y
        min_top_right = min(distance_right, distance_top)

        new_starting_point = Point(point.x - min_top_right, point.y + min_top_right)

        for i in range(0, min(len(self.board) - new_starting_point.x, new_starting_point.y + 1)):
            self.setTile(Point(new_starting_point.x + i, new_starting_point.y - i), 'A')

    def draw_attacked_fields(self, point):
        """
        marks all of the fields, that would be attacked by a queen on a specified point
        """
        self.draw_attacked_fields_horizontal(point)
        self.draw_attacked_fields_vertical(point)
        self.draw_attacked_fields_diagonal(point)

    def move_cursor_to_next_position(self):
        """
        moves the cursor to the next position, that is not attacked by any queen
        """
        if self.cursor == None:
            self.cursor = Point(0,0)
            return True

        # first row
        for y in range(self.cursor.y + 1, len(self.board)):
            if (self.getTile(Point(self.cursor.x, y)) == 'E'):
                self.cursor = Point(self.cursor.x, y)
                return True

        # rest of the board
        for x in range(self.cursor.x + 1, len(self.board)):
            for y in range(0, len(self.board[0])):
                if (self.getTile(Point(x,y)) == 'E'):
                    self.cursor = Point(x,y)
                    return True

        return False


    def revert_last_queen_move(self):
        """takes the last queen move back and remarks all of the board"""
        
        # get the last placed queen and removed it from the queens array
        last_queen = self.queens.pop()

        self.setTile(last_queen, 'E')
        self.recalculate_board() 

        # set the cursor to the last queen point
        self.cursor = last_queen


    def recalculate_board(self):
        """recalculates all of the queen positions and the positions that are attacked by any queen"""
        
        self.draw_empty_board()

        # copy the queens array
        queens = self.queens
        self.queens = []

        for queen in queens:
            self.draw_queen(queen)
    
    def __str__(self):
        str = ""
        for x in range(0,len(self.board)):
            for y in range(0,len(self.board[0])):
                str +=self.getTile(Point(x,y)) + " "
            str += "\n"

        str += f"number of queens: {len(self.queens)}\n"
        str += f"queens: {self.queens}\n"
        str += f"cursors: {self.cursor}\n"
        str += f"all_queens_placed: {self.all_queens_placed()}\n"
        str += f"board is still achievable {self.stillAchievable()} \n"
        str += f"number of empty spots {self.getNumberOfEmptySpots()}"
        return str
    
    def all_queens_placed(self):
        return len(self.queens) == 8

    def board_finished(self):
        if self.cursor == None:
            return False

        return self.cursor.x == len(self.board) -1  and self.cursor.y == 0 and len(self.queens) == 0

    def write_board_to_file(self, path):
        with open(path, "w") as f:
            f.write(board.__str__())

    def stillAchievable(self):
        return self.getNumberOfEmptySpots() >= 8 - len(self.queens)

board = Board()


def draw_queen_board():
    number_solutions = 0
    # while loop
    while True:

        # all possibilities tested
        if (board.board_finished()):
            return
        
        ## all 8 queens are placed but there might be more solutions
        if (board.all_queens_placed()):
            number_solutions += 1
            board.write_board_to_file(f"solutions/{number_solutions}.txt")
            board.revert_last_queen_move()
            continue
    
        # place a new queen
        if board.move_cursor_to_next_position() and board.stillAchievable():
            board.draw_queen()
            continue
        # revert the last queen
        else:
            board.revert_last_queen_move()
            continue

draw_queen_board()

