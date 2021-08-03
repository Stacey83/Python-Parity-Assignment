import unittest
import parity
import csv


class LoadGridTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None
        self.small_grid = self.load_grid_from_csv("tests/grids/small_grid.csv")
        self.medium_grid = self.load_grid_from_csv("tests/grids/medium_grid.csv")
        self.large_grid = self.load_grid_from_csv("tests/grids/large_grid.csv")
        self.empty_grid = self.load_grid_from_csv("tests/grids/empty_grid.csv")

    def load_grid_from_csv(self, csv_file_path):
        grid = []
        with open(csv_file_path) as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                grid.append(line)
        return grid

    def test_load_grid(self):
        result = parity.load_grid("tests/grids/small_grid.csv")
        self.assertListEqual(result, self.small_grid)

        result = parity.load_grid("tests/grids/medium_grid.csv")
        self.assertListEqual(result, self.medium_grid)

        result = parity.load_grid("tests/grids/large_grid.csv")
        self.assertListEqual(result, self.large_grid)

    def test_load_empty_grid(self):
        result = parity.load_grid("tests/grids/empty_grid.csv")
        self.assertListEqual(result, self.empty_grid)
