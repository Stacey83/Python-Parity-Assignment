import csv
import csv
import random

# grid = []

# for i in range(0, 9):
#     row = []
#     for j in range(0, 9):
#         num = random.randrange(0, 2, 1)
#         if num % 2 == 0:
#             row.append("X")
#         else:
#             row.append("O")
#     grid.append(row)

column_count = 0
row_count = 0

with open("expected_large_grid.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        row_count = 0
        for item in line:
            if item == "X":
                row_count += 1
        print(row_count)
        if line[-1] == "X":
            column_count += 1
print()
print(column_count)


# with open("expected_medium_grid.csv", "w") as csv_file:
#     writer = csv.writer(csv_file)
#     for line in grid:
#         writer.writerow(line)

