inputs = """
[P]     [L]         [T]            
[L]     [M] [G]     [G]     [S]    
[M]     [Q] [W]     [H] [R] [G]    
[N]     [F] [M]     [D] [V] [R] [N]
[W]     [G] [Q] [P] [J] [F] [M] [C]
[V] [H] [B] [F] [H] [M] [B] [H] [B]
[B] [Q] [D] [T] [T] [B] [N] [L] [D]
[H] [M] [N] [Z] [M] [C] [M] [P] [P]
 1   2   3   4   5   6   7   8   9 """

with open('input_sample.txt') as f:
    data = f.readlines()
    inputs = data[:4]
    moves = data[5:]





"""
    The grid is a list of lists, where each list is a row of the grid.
Each line is 11 characters long.
We split the line into 3 groups, since that is the highest number in the last row.

line_lenght = 11
max_number = 3
group_size = max_number + (max_number - 1)
number_of_groups = line_lenght // group_size
"""

def print_grid(grid):
    print("  Raw:",grid)
    grid = grid[::-1]
    for row in grid:
        print(row)

def load_grid(inputs):
    grid = []
    for line in inputs[:-1]:
        grid.append([line[i+1:i+2] for i in range(0, len(line), 4)])
        
    return grid[::-1]

def solution_1():
    grid = load_grid(inputs)

    for move in moves:
        move = move.split()
        #print(grid)
        to_move = int(move[1])
        from_col = int(move[3])-1
        to_col = int(move[5])-1
        height = len(grid)

        for i in range(to_move):
            t,f = 0,0
            # Find the top of the stack in the "from" column
            # The top of the stack is the first empty space
            while f < height and grid[f][from_col] != " ":
                f += 1
            f -= 1

            # Find the top of the stack in the "to" column
            # The top of the stack is the first empty space
            while t < height and grid[t][to_col] != " ":
                t += 1
            t -= 1
            
            # If the stack is as high as the grid, we add a new row
            if f == height-1:
                grid.append([" "] * len(grid[0]))
                height += 1
            
            if t == height-1:
                grid.append([" "] * len(grid[0]))
                height += 1

            # Move the top of the stack
            grid[t+1][to_col] = grid[f][from_col]
            grid[f][from_col] = " "

    # Print the bottom row
    print_grid(grid)

def solution_2():
    grid = load_grid(inputs)
    print_grid(grid)
    print("\n")

    for move in moves:
        move = move.split()
        #print(grid)
        print("> ", move)
        to_move = int(move[1])
        from_col = int(move[3])-1
        to_col = int(move[5])-1
        height = len(grid)
        print("Height:", height)

        t,f = 0,0
        print_grid(grid)
        # Find the top of the stack in the "from" column
        # The top of the stack is the first empty space
        while f < height and grid[f][from_col] != " ":
            f += 1
        f -= 1

        # Find the top of the stack in the "to" column
        # The top of the stack is the first empty space
        while t < height and grid[t][to_col] != " ":
            t += 1
        
        # If the stack is as high as the grid, we add a new row       
        if t == height:
            grid.append([" "] * len(grid[0]))
            height += 1

        # Move the to_move number of blocks
        for i in range(to_move)[::-1]:
            grid[t+1+i][to_col] = grid[f-i][from_col]
            grid[f-i][from_col] = " "

        print_grid(grid)
solution_1()
#solution_2()