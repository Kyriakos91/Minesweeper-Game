import random


class Cell:
    def __init__(self, is_mine=False, number_of_neighbour_mines=0):
        self.is_mine = is_mine
        self.number_of_neighbour_mines = number_of_neighbour_mines
        self.hidden = True

    def has_neighbour_mines(self):
        return self.number_of_neighbour_mines >0

    def set_as_mine(self):
        self.is_mine = True
        self.number_of_neighbour_mines = 0

    def increment_neighbour_mines(self):
        self.number_of_neighbour_mines = self.number_of_neighbour_mines + 1

    def __str__(self):
        if self.is_mine:
            return "0"
        return str(self.number_of_neighbour_mines)
    
class Board:
    def __init__(self, size, number_of_mines):
        self.size = size
        self.number_of_mines = number_of_mines
        self.game_board = [[Cell() for _ in range(size)] for _ in range(size)]
        self.REVEILING_NEIGHBOURS =[(-1,0),(0,-1),(1,0),(0,1)]
        self.NEIGHBOURS =[(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,0),(0,1),(1,1)]

    def is_inbound_neighbour (self,x,y):
        return 0<= x and x <self.size and 0<= y and y <self.size

    def number_of_hidden_cells(self):
        amount_of_unreveiled_cells=0
        for row in self.game_board:
            for cell in row:
                if cell.hidden:
                    amount_of_unreveiled_cells=amount_of_unreveiled_cells+1
        return amount_of_unreveiled_cells

    def print_game_board(self):
        n = self.size
        print()
        print("\t\t\tMINESWEEPER\n")

        st = "   "
        for i in range(n):
            st = st + "     " + str(i + 1)
        print(st)

        for r in range(n):
            st = "     "
            if r == 0:
                for col in range(n):
                    st = st + "______"
                print(st)

            st = "     "
            for col in range(n):
                st = st + "|     "
            print(st + "|")

            st = "  " + str(r + 1) + "  "
            for col in range(n):
                if self.game_board[r][col].hidden:
                    st = st + "|     "
                elif self.game_board[r][col].is_mine:
                    st = st + "|  M  "
                else:
                    st = st + "|  " + str(self.game_board[r][col]) + "  "
            print(st + "|")

            st = "     "
            for col in range(n):
                st = st + "|_____"
            print(st + '|')

        print()

    def initialize(self):
        number_of_mines = self.number_of_mines
        while number_of_mines != 0:
            random_x = random.randint(0, self.size - 1)
            random_y = random.randint(0, self.size - 1)
            if not self.game_board[random_x][random_y].is_mine:
                self.game_board[random_x][random_y].set_as_mine()
                number_of_mines = number_of_mines - 1
                self.replace_the_neighbours_of_mines(random_x,random_y)

    def replace_the_neighbours_of_mines(self,random_x,random_y):
        for neighbour in self.NEIGHBOURS:
            next_state_x = random_x+neighbour[0]
            next_state_y = random_y+neighbour[1]
            if self.is_inbound_neighbour (next_state_x,next_state_y) and not self.game_board[next_state_x][next_state_y].is_mine:
                self.game_board[next_state_x][next_state_y].increment_neighbour_mines()

class Minesweeper:
    def __init__(self, size, number_of_mines):
        self.board = Board(size, number_of_mines)
        self.is_game_over=False
        self.board.initialize()

    def has_no_more_moves(self):
        return self.board.number_of_hidden_cells()==self.board.number_of_mines

    def reveal(self,x,y):
        self.board.game_board[x][y].hidden=False
        if self.board.game_board[x][y].has_neighbour_mines():
            return
        for neighbour in self.board.REVEILING_NEIGHBOURS:
            next_state_x = x+neighbour[0]
            next_state_y = y+neighbour[1]
            if not self.board.is_inbound_neighbour (next_state_x,next_state_y)\
                or not self.board.game_board[next_state_x][next_state_y].hidden\
                or self.board.game_board[next_state_x][next_state_y].is_mine:
                continue
            if self.board.game_board[next_state_x][next_state_y].has_neighbour_mines():
                self.board.game_board[next_state_x][next_state_y].hidden=False
            else:
                self.reveal(next_state_x,next_state_y)

    def play(self):
        self.board.print_game_board()
        
        while not self.is_game_over:
            
            x=int(input("Please select a row you want to open: "))-1
            y=int(input("Please select a column you want to open: "))-1
        
            if self.board.game_board[x][y].is_mine:
                self.board.game_board[x][y].hidden=False
                self.board.print_game_board()
                print ("Game over -  you hit a bomb!!")
                self.is_game_over=True 
            else:
                self.reveal(x,y)
            self.board.print_game_board()

            if self.has_no_more_moves():
                print ("WOW -you did it!!")
                self.is_game_over=True
