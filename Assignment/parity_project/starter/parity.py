import csv
from os import X_OK
from typing import Counter


def load_grid(csv_file_path):
    """Loads data from a csv file.

    Args:
        csv_file_path: string representing the path to a csv file.
    Returns:
        A list of lists, where each sublist is a line in the csv file.
    """
    grid = []
    with open(csv_file_path) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            grid.append(line)
    return grid
    

def add_column(grid):
    """Adds a new column to a grid. For each row, if there is an even
    number of X characters, a O is added to the row, otherwise a X is added
    to the row.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.

    Returns:
        The same grid, with a new column added.
    """
    #adds extra index postion to each list (line).  To work out the character of that index, count frequency of other indexes.  If 'X" count divisable % by 2, new index = "O" else "X"
    
    for newcolumn in grid:
        count = Counter(newcolumn)
        if count['X'] % 2 == 0:
            newcolumn.append('O')
        else:
            newcolumn.append('X')

    # print(grid)
    return(grid)



def add_row(grid):
    """Adds a new row to a grid. For each column, if there is an even
    number of X characters, a O is added to the column, otherwise a X is added
    to the column.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.

    Returns:
        The same grid, with a new row added.
    """
    new_list = list(map(list, zip(*grid))) #transposes the original grid
    
    for row in new_list:
        rowCount = Counter(row) #counts the occurances of each value in row
        if rowCount['X'] % 2 == 0: #determines if row has even number of "X"
            row.append('O')
        else:
            row.append('X')
    

    return(list(map(list, zip(*new_list))))


def flip_cell(x_pos, y_pos, grid):
    """Prompts the user to choose a cell to swap from X to O (or vice versa).

    Arguments:
        x_pos: An integer representing the x coordinate of the cell.
        y_pos: An integer representing the y coordinate of the cell.
        grid: A list of lists, where each sublist represents a row in a grid.

        In the following grid:
            a b
            c d
        These are the coordinates of each letter:
            a = x: 0, y: 0
            b = x: 1, y: 0
            c = x: 0, y: 1
            d = x: 1, y: 1

    Returns:
        The same grid, with a cell switched.
    """

    if grid[y_pos][x_pos] == "X":
        grid[y_pos][x_pos] = "O"
    else: grid[y_pos][x_pos] = "X"
    return grid



def find_flipped_cell(grid):
    """Determines which cell/cell in the grid was flipped.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.

    Returns:
        A list containing the coordinates of the cell with the flipped cell.
        In the following grid:
            a b
            c d
        These are the coordinates of each letter:
            a = (0, 0)
            b = (1, 0)
            c = (0, 1)
            d = (1, 1)
        If 'a' was the flipped letter, this function would return: [0, 0]
    """

    new_list = list(map(list, zip(*grid)))
    xcoord = None
    ycoord = None

    for column in grid:
        columncount = Counter(column)
        if columncount['X'] % 2 != 0:
            xcoord = grid.index(column)
    for row in new_list: 
        rowcount = Counter(row)
        if rowcount['X'] % 2 != 0:
            ycoord = new_list.index(row)

    return ([ycoord, xcoord])
