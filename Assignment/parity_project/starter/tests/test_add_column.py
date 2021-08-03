import unittest
import parity
import csv


class AddColumnTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None
        self.all_x_grid = self.load_grid_from_csv("tests/grids/all_x.csv")
        self.expected_all_x_grid = self.load_grid_from_csv("tests/grids/expected_all_x.csv")
        self.small_grid = self.load_grid_from_csv("tests/grids/small_grid.csv")
        self.expected_small_grid = self.load_grid_from_csv("tests/grids/expected_small_grid.csv")
        self.medium_grid = self.load_grid_from_csv("tests/grids/medium_grid.csv")
        self.expected_medium_grid = self.load_grid_from_csv("tests/grids/expected_medium_grid.csv")
        self.large_grid = self.load_grid_from_csv("tests/grids/large_grid.csv")
        self.expected_large_grid = self.load_grid_from_csv("tests/grids/expected_large_grid.csv")
        self.empty_grid = self.load_grid_from_csv("tests/grids/empty_grid.csv")

    def load_grid_from_csv(self, csv_file_path):
        grid = []
        with open(csv_file_path) as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                grid.append(line)
        return grid

    def test_add_column(self):

        result_grid = parity.add_column(self.small_grid)
        expected_small_grid = self.expected_small_grid[0:-1]
        self.assertListEqual(result_grid, expected_small_grid)

        result_grid = parity.add_column(self.medium_grid)
        expected_medium_grid = self.expected_medium_grid[0:-1]
        self.assertListEqual(result_grid, expected_medium_grid)

        result_grid = parity.add_column(self.large_grid)
        expected_large_grid = self.expected_large_grid[0:-1]
        self.assertListEqual(result_grid, expected_large_grid)

    def test_add_column_empty_grid(self):
        result_grid = parity.add_column([])
        self.assertListEqual(result_grid, [])

    def test_add_column_all_x(self):
        result_grid = parity.add_column(self.all_x_grid)
        expected_all_x_grid = self.expected_all_x_grid[0:-1]
        self.assertListEqual(result_grid, expected_all_x_grid)
