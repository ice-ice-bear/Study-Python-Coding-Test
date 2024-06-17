import sys
sys.stdin = open('in1.txt', 'r')

# Read the Sudoku puzzle from the input file and store it in a 2D list
sudoku = [list(map(int, input().split())) for _ in range(9)]

# Initialize a counter to keep track of the number of invalid 3x3 sub-grids
cnt = 0

# Iterate through each 3x3 sub-grid in the Sudoku puzzle
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        # Extract the values in the current 3x3 sub-grid
        sub_grid = [sudoku[x][y] for x in range(i, i+3) for y in range(j, j+3)]
        print(sub_grid)
        
        # Check if the current 3x3 sub-grid contains all unique values (1-9)
        if len(set(sub_grid)) != 9:
            # If the sub-grid is invalid, increment the counter
            cnt += 1


# Determine the final result based on the counter value
if cnt == 0:
    print('YES')  # All 3x3 sub-grids are valid
else:
    print('NO')   # At least one 3x3 sub-grid is invalid
