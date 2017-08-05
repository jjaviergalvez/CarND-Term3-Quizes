# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]

    # initialization
    value[goal[0]][goal[1]] = 0
    closed[goal[0]][goal[1]] = 1
    
    lst = [goal]
    for e in lst:
        x = e[0]
        y = e[1]
        step = value[x][y] + cost
        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):                    
                if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                    value[x2][y2] = step
                    lst.append([x2,y2])
                    closed[x2][y2] = 1

    return value 

result = compute_value(grid, goal, cost)
for row in result:
    print(row)