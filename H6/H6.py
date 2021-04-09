def fill(grid, old_value, new_value, seed): 
    ct=0

    for i in range(len(grid)):
        for j in range(seed[1],len(grid[i])):
            if grid[i][j] == old_value :
                if grid[i][j-1] == old_value :
                    grid[i][j-1] = new_value
                grid[i][j] = new_value
            elif grid[i][j-1] == old_value :
                    grid[i][j-1] = new_value



