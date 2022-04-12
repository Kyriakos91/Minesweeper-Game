from src.minesweeperclasses import Board
import unittest

class TestBoard(unittest.TestCase):

    def test_board_defaults(self):
        size=4
        number_of_mines=2

        board=Board(size,number_of_mines)
        self.assertEqual(board.size,size,"Board size should be the size the user inputs")
        self.assertEqual(board.number_of_mines,number_of_mines,"Number of mines should be the number the user inputs")
        self.assertEqual(len(board.game_board)*len(board.game_board[0]),size*size,"game_board should be a cell matrix of board size x board size")

    def test_inbound_neighbours(self):
        size=4
        number_of_mines=2
        board=Board(size,number_of_mines)
        
        self.assertEqual(board.is_inbound_neighbour(1,3),True,"The cell the user wants should be inbound the board")
        self.assertEqual(board.is_inbound_neighbour(5,3),False,"The cell the user wants should be inbound the board")

    def test_the_number_of_hidden_cells(self):
        size=3
        number_of_mines=2
        board=Board(size,number_of_mines)

        self.assertEqual(board.number_of_hidden_cells(),size*size,"All cells created should be hidden")
        board.game_board[1][1].hidden=False
        board.game_board[0][0].hidden=False
        board.game_board[0][1].hidden=False
        board.game_board[0][2].hidden=False

        self.assertEqual(board.number_of_hidden_cells(),5,"The number of hidden cells is wrong")

    def test_initialization_of_board(self):
        size=4
        number_of_mines=2
        board=Board(size,number_of_mines)

        board.initialize()

        self.assertEqual(self.__count_number_of_mines(board.game_board),number_of_mines,"The  number of cells being mines is wrong")

    def __count_number_of_mines(self,board):
        number_of_assigned_mines=0
        for row in board:
            for cell in row:
                if cell.is_mine:
                    number_of_assigned_mines=number_of_assigned_mines+1
        return number_of_assigned_mines

    def test_replaced_neighbours(self):
        
        #test1
        size=3
        number_of_mines=2
        board=Board(size,number_of_mines)

        board.game_board[1][1].is_mine=True
        board.game_board[0][0].is_mine=True
        board.replace_the_neighbours_of_mines(0,0)
        board.replace_the_neighbours_of_mines(1,1)

        self.assertEqual(board.game_board[0][1].number_of_neighbour_mines,2,"the neighbour of test1 should be 2")
        self.assertEqual(board.game_board[1][0].number_of_neighbour_mines,2,"the neighbour of test1 should be 2")
        self.assertEqual(board.game_board[0][2].number_of_neighbour_mines,1,"the neighbour of test1 should be 1")
        self.assertEqual(board.game_board[1][2].number_of_neighbour_mines,1,"the neighbour of test1 should be 1")
        self.assertEqual(board.game_board[2][0].number_of_neighbour_mines,1,"the neighbour of test1 should be 1")
        self.assertEqual(board.game_board[2][1].number_of_neighbour_mines,1,"the neighbour of test1 should be 1")
        self.assertEqual(board.game_board[2][2].number_of_neighbour_mines,1,"the neighbour of test1 should be 1")

        #test2
        size=3
        number_of_mines=1
        board=Board(size,number_of_mines)

        board.game_board[0][0].is_mine=True
        board.replace_the_neighbours_of_mines(0,0)

        self.assertEqual(board.game_board[1][1].number_of_neighbour_mines,1,"the neighbour of test2 should be 1")
        self.assertEqual(board.game_board[0][1].number_of_neighbour_mines,1,"the neighbour of test2 should be 1")
        self.assertEqual(board.game_board[1][0].number_of_neighbour_mines,1,"the neighbour of test2 should be 1")
        self.assertEqual(board.game_board[0][2].number_of_neighbour_mines,0,"the neighbour of test2 should be 0")
        self.assertEqual(board.game_board[1][2].number_of_neighbour_mines,0,"the neighbour of test2 should be 0")
        self.assertEqual(board.game_board[2][0].number_of_neighbour_mines,0,"the neighbour of test2 should be 0")
        self.assertEqual(board.game_board[2][1].number_of_neighbour_mines,0,"the neighbour of test2 should be 0")
        self.assertEqual(board.game_board[2][2].number_of_neighbour_mines,0,"the neighbour of test2 should be 0")


        #test3
        size=3
        number_of_mines=4
        board=Board(size,number_of_mines)

        board.game_board[0][1].is_mine=True
        board.game_board[1][0].is_mine=True
        board.game_board[1][2].is_mine=True
        board.game_board[2][1].is_mine=True

        board.replace_the_neighbours_of_mines(0,1)
        board.replace_the_neighbours_of_mines(1,0)
        board.replace_the_neighbours_of_mines(1,2)
        board.replace_the_neighbours_of_mines(2,1)

        self.assertEqual(board.game_board[1][1].number_of_neighbour_mines,4,"the neighbour of test3 should be 4")
        self.assertEqual(board.game_board[0][2].number_of_neighbour_mines,2,"the neighbour of test3 should be 2")
        self.assertEqual(board.game_board[2][0].number_of_neighbour_mines,2,"the neighbour of test3 should be 2")
        self.assertEqual(board.game_board[0][0].number_of_neighbour_mines,2,"the neighbour of test3 should be 2")
        self.assertEqual(board.game_board[2][2].number_of_neighbour_mines,2,"the neighbour of test3 should be 2")

if __name__ == '__main__':
    unittest.main()