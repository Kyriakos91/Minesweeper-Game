from src.minesweeperclasses import Minesweeper, Board
import unittest

class TestMinesweeper(unittest.TestCase):
    def test_minesweeper_defaults(self):
        size=4
        number_of_mines=2
        minesweeper=Minesweeper(size,number_of_mines)
        
        self.assertEqual(minesweeper.board.size,size,"Board size should be the size the user inputs")
        self.assertEqual(minesweeper.board.number_of_mines,number_of_mines,"Number of mines should be the number the user inputs")
        self.assertEqual(minesweeper.is_game_over,False,"The game should not be over")

    def test_user_has_no_more_moves(self):
        size=2
        number_of_mines=2
        minesweeper=Minesweeper(size,number_of_mines)

        minesweeper.board.game_board[1][1].hidden=False
        minesweeper.board.game_board[0][0].hidden=True
        minesweeper.board.game_board[0][1].hidden=False
        minesweeper.board.game_board[1][0].hidden=False
        
        self.assertEqual(minesweeper.has_no_more_moves(),False,"the user should has more moves")

        minesweeper.board.game_board[1][1].hidden=False
        minesweeper.board.game_board[0][0].hidden=True
        minesweeper.board.game_board[0][1].hidden=True
        minesweeper.board.game_board[1][0].hidden=False
        
        self.assertEqual(minesweeper.has_no_more_moves(),True,"the user should not has more moves")


    def test_revealing_cells(self):
        
        size=3
        number_of_mines=2
        minesweeper=Minesweeper(size,number_of_mines)
        board=Board(size,number_of_mines)
        board.game_board[0][0].number_of_neighbour_mines=0
        board.game_board[0][1].number_of_neighbour_mines=0
        board.game_board[0][2].number_of_neighbour_mines=0
        board.game_board[1][0].number_of_neighbour_mines=1
        board.game_board[1][1].number_of_neighbour_mines=2
        board.game_board[1][2].number_of_neighbour_mines=2
        board.game_board[2][0].number_of_neighbour_mines=1
        board.game_board[2][1].set_as_mine()
        board.game_board[2][2].set_as_mine()
        minesweeper.board=board

        minesweeper.reveal(1,1)
        self.assertEqual(board.game_board[1][1].hidden,False)

        self.assertTrue(board.game_board[0][0].hidden)
        self.assertTrue(board.game_board[0][1].hidden)
        self.assertTrue(board.game_board[0][2].hidden)
        self.assertTrue(board.game_board[1][0].hidden)
        self.assertTrue(board.game_board[1][2].hidden)
        self.assertTrue(board.game_board[2][0].hidden)
        self.assertTrue(board.game_board[2][1].hidden)
        self.assertTrue(board.game_board[2][2].hidden)


        minesweeper.reveal(0,0)
        self.assertEqual(board.game_board[0][0].hidden,False)
        self.assertEqual(board.game_board[0][1].hidden,False)
        self.assertEqual(board.game_board[0][2].hidden,False)
        self.assertEqual(board.game_board[1][0].hidden,False)
        self.assertEqual(board.game_board[1][1].hidden,False)
        self.assertEqual(board.game_board[1][2].hidden,False)

        self.assertTrue(board.game_board[2][0].hidden)
        self.assertTrue(board.game_board[2][1].hidden)
        self.assertTrue(board.game_board[2][2].hidden)

        minesweeper.reveal(2,0)
        self.assertEqual(board.game_board[0][0].hidden,False)
        self.assertEqual(board.game_board[0][1].hidden,False)
        self.assertEqual(board.game_board[0][2].hidden,False)
        self.assertEqual(board.game_board[1][0].hidden,False)
        self.assertEqual(board.game_board[1][1].hidden,False)
        self.assertEqual(board.game_board[1][2].hidden,False)
        self.assertEqual(board.game_board[2][0].hidden,False)
        self.assertTrue(board.game_board[2][1].hidden)
        self.assertTrue(board.game_board[2][2].hidden)

        minesweeper.reveal(2,1)
        self.assertEqual(board.game_board[0][0].hidden,False)
        self.assertEqual(board.game_board[0][1].hidden,False)
        self.assertEqual(board.game_board[0][2].hidden,False)
        self.assertEqual(board.game_board[1][0].hidden,False)
        self.assertEqual(board.game_board[1][1].hidden,False)
        self.assertEqual(board.game_board[1][2].hidden,False)
        self.assertEqual(board.game_board[2][0].hidden,False)
        self.assertEqual(board.game_board[2][1].hidden,False)
        self.assertTrue(board.game_board[2][2].hidden)

    #def test_playing_function(self):
     #   from unittest import mock

      #  size=4
      #  number_of_mines=2
     #   minesweeper=Minesweeper(size,number_of_mines)
     #   minesweeper.play()

      #  mock.builtins.input = lambda _: "yes"



if __name__ == '__main__':
    unittest.main()

