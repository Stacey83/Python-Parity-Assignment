import unittest
import parity
import csv


class FlipCellTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None
        self.small_grid = self.load_grid_from_csv("tests/grids/expected_small_grid.csv")
        self.small_grid_flipped = self.load_grid_from_csv("tests/grids/small_grid_flipped.csv")
        self.medium_grid = self.load_grid_from_csv("tests/grids/expected_medium_grid.csv")
        self.medium_grid_flipped = self.load_grid_from_csv("tests/grids/medium_grid_flipped.csv")
        self.large_grid = self.load_grid_from_csv("tests/grids/expected_large_grid.csv")
        self.large_grid_flipped = self.load_grid_from_csv("tests/grids/large_grid_flipped.csv")

    def load_grid_from_csv(self, csv_file_path):
        grid = []
        with open(csv_file_path) as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                grid.append(line)
        return grid

    def test_flip_cell(self):
        result_grid = parity.flip_cell(1, 2, self.small_grid)
        self.assertListEqual(result_grid, self.small_grid_flipped)

        result_grid = parity.flip_cell(7, 9, self.medium_grid)
        self.assertListEqual(result_grid, self.medium_grid_flipped)

        result_grid = parity.flip_cell(26, 75, self.large_grid)
        self.assertListEqual(result_grid, self.large_grid_flipped)
