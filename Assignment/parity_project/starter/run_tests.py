import unittest
from tests.test_add_column import AddColumnTests
from tests.test_add_row import AddRowTests
from tests.test_find_flipped_cell import FindFlippedCellTests
from tests.test_flip_cell import FlipCellTests
from tests.test_load_grid import LoadGridTests
from tests.test_integration import IntegrationTests


runner = unittest.TextTestRunner()

print('Running Tests...\n')
runner.run(unittest.TestSuite((unittest.makeSuite(LoadGridTests))))
runner.run(unittest.TestSuite((unittest.makeSuite(AddColumnTests))))
runner.run(unittest.TestSuite((unittest.makeSuite(AddRowTests))))
runner.run(unittest.TestSuite((unittest.makeSuite(FindFlippedCellTests))))
runner.run(unittest.TestSuite((unittest.makeSuite(FlipCellTests))))
runner.run(unittest.TestSuite((unittest.makeSuite(IntegrationTests))))
