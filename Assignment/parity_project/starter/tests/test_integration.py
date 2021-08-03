import unittest
import parity
import csv


class IntegrationTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None
        self.all_x_grid = self.load_grid_from_csv("tests/grids/all_x.csv")
        self.expected_all_x_grid = self.load_grid_from_csv("tests/grids/expected_all_x.csv")
        self.small_grid = self.load_grid_from_csv("tests/grids/small_grid.csv")
        self.small_grid_flipped = self.load_grid_from_csv("tests/grids/small_grid_flipped.csv")
        self.expected_small_grid = self.load_grid_from_csv("tests/grids/expected_small_grid.csv")
        self.medium_grid = self.load_grid_from_csv("tests/grids/medium_grid.csv")
        self.medium_grid_flipped = self.load_grid_from_csv("tests/grids/medium_grid_flipped.csv")
        self.expected_medium_grid = self.load_grid_from_csv("tests/grids/expected_medium_grid.csv")
        self.large_grid = self.load_grid_from_csv("tests/grids/large_grid.csv")
        self.large_grid_flipped = self.load_grid_from_csv("tests/grids/large_grid_flipped.csv")
        self.expected_large_grid = self.load_grid_from_csv("tests/grids/expected_large_grid.csv")
        self.empty_grid = self.load_grid_from_csv("tests/grids/empty_grid.csv")

    def load_grid_from_csv(self, csv_file_path):
        grid = []
        with open(csv_file_path) as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                grid.append(line)
        return grid

    def test_add_row_then_column(self):
        added_row = parity.add_row(self.small_grid)
        result_grid = parity.add_column(added_row)
        self.assertListEqual(result_grid, self.expected_small_grid)

        added_row = parity.add_row(self.medium_grid)
        result_grid = parity.add_column(added_row)
        self.assertListEqual(result_grid, self.expected_medium_grid)

        added_row = parity.add_row(self.large_grid)
        result_grid = parity.add_column(added_row)
        self.assertListEqual(result_grid, self.expected_large_grid)

    def test_add_column_then_row(self):
        added_column = parity.add_column(self.small_grid)
        result_grid = parity.add_row(added_column)
        self.assertListEqual(result_grid, self.expected_small_grid)

        added_column = parity.add_column(self.medium_grid)
        result_grid = parity.add_row(added_column)
        self.assertListEqual(result_grid, self.expected_medium_grid)

        added_column = parity.add_column(self.large_grid)
        result_grid = parity.add_row(added_column)
        self.assertListEqual(result_grid, self.expected_large_grid)

    def test_add_column_and_row_flip_cell(self):
        added_column = parity.add_column(self.small_grid)
        result_grid = parity.add_row(added_column)
        result_flipped = parity.flip_cell(1, 2, result_grid)
        self.assertListEqual(result_flipped, self.small_grid_flipped)

        added_column = parity.add_column(self.medium_grid)
        result_grid = parity.add_row(added_column)
        result_flipped = parity.flip_cell(7, 9, result_grid)
        self.assertListEqual(result_flipped, self.medium_grid_flipped)

        added_column = parity.add_column(self.large_grid)
        result_grid = parity.add_row(added_column)
        result_flipped = parity.flip_cell(26, 75, result_grid)
        self.assertListEqual(result_flipped, self.large_grid_flipped)

    def test_flip_cell_find_flipped_cell(self):
        result_flipped = parity.flip_cell(1, 2, self.expected_small_grid)
        result_coordinates = parity.find_flipped_cell(result_flipped)
        expected_coordinates = [1, 2]
        self.assertListEqual(result_coordinates, expected_coordinates)

        result_flipped = parity.flip_cell(7, 9, self.expected_medium_grid)
        result_coordinates = parity.find_flipped_cell(result_flipped)
        expected_coordinates = [7, 9]
        self.assertListEqual(result_coordinates, expected_coordinates)

        result_flipped = parity.flip_cell(26, 75, self.expected_large_grid)
        result_coordinates = parity.find_flipped_cell(result_flipped)
        expected_coordinates = [26, 75]
        self.assertListEqual(result_coordinates, expected_coordinates)

    def test_add_column_and_row_flip_cell_find_flipped_cell(self):
        added_column = parity.add_column(self.small_grid)
        result_grid = parity.add_row(added_column)
        result_flipped = parity.flip_cell(1, 2, result_grid)
        result_coordinates = parity.find_flipped_cell(result_flipped)
        expected_coordinates = [1, 2]
        self.assertListEqual(result_coordinates, expected_coordinates)

        added_column = parity.add_column(self.medium_grid)
        result_grid = parity.add_row(added_column)
        result_flipped = parity.flip_cell(7, 9, self.expected_medium_grid)
        result_coordinates = parity.find_flipped_cell(result_flipped)
        expected_coordinates = [7, 9]
        self.assertListEqual(result_coordinates, expected_coordinates)

        added_column = parity.add_column(self.large_grid)
        result_grid = parity.add_row(added_column)
        result_flipped = parity.flip_cell(26, 75, self.expected_large_grid)
        result_coordinates = parity.find_flipped_cell(result_flipped)
        expected_coordinates = [26, 75]
        self.assertListEqual(result_coordinates, expected_coordinates)
