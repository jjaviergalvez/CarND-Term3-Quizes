# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

import sys

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']



def expand(pos):
    n_row = len(grid)
    n_col = len(grid[0])

    x = pos[1]
    y = pos[2]

    g_val = pos[0] + 1
    
    expand_list = []
    for i in delta:
        x_ = i[0] + x
        y_ = i[1] + y
        #if are between the bounds of the map
        if (x_>=0 and x_<n_row and y_>=0 and y_<n_col):
            value = grid[x_][y_]
            if (value != 1 and value != -1):
                expand_list.append([g_val, x_, y_])
                grid[x_][y_] = -1 #mark as value already taken

    return expand_list

def smallest(open_list):
    lowest_value = 100000
    i_lowest_value = -1
    i = 0
    for element in open_list:
        print
        if element[0] < lowest_value:
            lowest_value = element[0]
            i_lowest_value = i
        i += 1

    
    if i_lowest_value != -1:
        return i_lowest_value
    else:
        print("fail")
        sys.exit(0)


def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    # intitialization
    grid[init[0]][init[1]] = -1

    open_list = init[:]
    open_list.insert(0,0)
    open_list = [open_list]

    #print("initial open list:")
    #print(open_list)
    
    list_item = [0,0,0]
    while (list_item[1:]!= goal):
        #print("----")

        #print("take list item")
        index = smallest(open_list)
        list_item = open_list.pop(index)
        #print(list_item)
        
        #print("new open list")
        open_list += expand(list_item)
        #print(open_list)


    return list_item


print(search(init, goal, cost))