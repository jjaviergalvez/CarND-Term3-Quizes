# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):

  
  closed = [[[0 for col in range(len(grid[0]))] for row in range(len(grid))],
           [[0 for col in range(len(grid[0]))] for row in range(len(grid))],
           [[0 for col in range(len(grid[0]))] for row in range(len(grid))],
           [[0 for col in range(len(grid[0]))] for row in range(len(grid))]]

  policy = [[999 for col in range(len(grid[0]))] for row in range(len(grid))]

  value = [[[0 for col in range(len(grid[0]))] for row in range(len(grid))],
           [[0 for col in range(len(grid[0]))] for row in range(len(grid))],
           [[0 for col in range(len(grid[0]))] for row in range(len(grid))],
           [[0 for col in range(len(grid[0]))] for row in range(len(grid))]]

  policy = [[[999 for col in range(len(grid[0]))] for row in range(len(grid))],
           [[999 for col in range(len(grid[0]))] for row in range(len(grid))],
           [[999 for col in range(len(grid[0]))] for row in range(len(grid))],
           [[999 for col in range(len(grid[0]))] for row in range(len(grid))]]           

  policy2D = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

  #closed[init[2]][init[0]][init[1]] = 1
  #value[init[2]][init[0]][init[1]] = 0

  #closed[goal[0]][goal[1]] = 1
  #value[goal[0]][goal[1]] = 0
  
  for i in range(4):
    policy[i][goal[0]][goal[1]] = '*'
    closed[i][goal[0]][goal[1]] = 1

  lst = [goal]
  
  """
  for i in range(4):
    policy[i][init[0]][init[1]] = '*'
    closed[i][init[0]][init[1]] = 1

  lst = [init]
  """

  for item in lst:
    x = item[0]
    y = item[1]
    for orientation in range(4):
      for i in range(3):
        o2 = (orientation + action[i]) % 4
        #print("o2", o2)
        x2 = x + forward[o2][0]
        y2 = y + forward[o2][1]
        #print("[x,y]", [x,y])
        #print("[x2,y2]", [x2,y2])
        #input("Press Enter to continue...")
        if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
          if closed[o2][x2][y2] == 0 and grid[x2][y2] == 0:
            """
            v2 = value[o2][x2][y2] + cost[i]
            value[orientation][x][y] = v2
            policy[orientation][x][y] = action_name[i]
            closed[o2][x2][y2] = 1
            """
            v2 = value[orientation][x][y] + cost[i]
            value[orientation][x2][y2] = v2
            policy[orientation][x2][y2] = action_name[i]
            closed[orientation][x2][y2] = 1

            lst.append([x2,y2])

    for row in policy[0]:
      print(row)
    print(" ")
    for row in value[0]:
      print(row)
    print(" ")

  """
  for n in range(4):
    for row in policy[n]:
      print(row)
    print(" ")

  for n in range(4):
    for row in value[n]:
      print(row)
    print(" ")
  """

  return policy

result = optimum_policy2D(grid,init,goal,cost)
#for row in result:
#  print(row)