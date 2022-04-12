from src.minesweeperclasses import Cell
import unittest

class TestCell(unittest.TestCase):
    def test_cell_defaults(self):
        cell=Cell()
        self.assertEqual(cell.hidden,True,"New cells should be created hidden")
        self.assertEqual(cell.is_mine,False,"New cells should be created not mines")
        self.assertEqual(cell.number_of_neighbour_mines,0,"New cells should be created with zero neighbours")

    def test_cell_is_set_as_mine(self):
        cell=Cell()
        cell.set_as_mine()
        self.assertEqual(cell.is_mine,True,"Cells should be a mine when it's set as mine")
        self.assertEqual(cell.number_of_neighbour_mines,0,"Cell's neighbours should be zero when cell is set as mine")

    def test_increment_of_the_neighbours(self):
        cell=Cell()
        cell.increment_neighbour_mines()
        self.assertEqual(cell.number_of_neighbour_mines,1,"Cell's neighbours should be increased by one when cell is set as mine")

if __name__ == '__main__':
    unittest.main()