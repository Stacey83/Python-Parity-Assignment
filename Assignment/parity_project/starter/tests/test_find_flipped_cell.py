import unittest
import parity
import csv


class FindFlippedCellTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None
        self.small_grid_flipped = self.load_grid_from_csv("tests/grids/small_grid_flipped.csv")
        self.medium_grid_flipped = self.load_grid_from_csv("tests/grids/medium_grid_flipped.csv")
        self.large_grid_flipped = self.load_grid_from_csv("tests/grids/large_grid_flipped.csv")
        self.medium_grid = self.load_grid_from_csv("tests/grids/expected_medium_grid.csv")

    def load_grid_from_csv(self, csv_file_path):
        grid = []
        with open(csv_file_path) as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                grid.append(line)
        return grid

    def test_find_flipped_cell(self):
        result_coordinates = parity.find_flipped_cell(self.small_grid_flipped)
        expected_coordinates = [1, 2]
        self.assertListEqual(result_coordinates, expected_coordinates)     

        result_coordinates = parity.find_flipped_cell(self.medium_grid_flipped)
        expected_coordinates = [7, 9]
        self.assertListEqual(result_coordinates, expected_coordinates)     

        result_coordinates = parity.find_flipped_cell(self.large_grid_flipped)
        expected_coordinates = [26, 75]
        self.assertListEqual(result_coordinates, expected_coordinates)     

    def test_find_flipped_cell_no_cell_flipped(self):
        result_coordinates = parity.find_flipped_cell(self.medium_grid)
        expected_coordinates = [None, None]
        self.assertListEqual(result_coordinates, expected_coordinates)     

