import numpy as np

DATA_FILE = 'd6b.txt'
with open(DATA_FILE) as f:
    grid = f.read().splitlines()
    grid = list(map(list, grid))

print(grid)

dude_pos = None
for a in range(len(grid)):
    if '^' in grid[a]:
        i = grid[a].index('^') 
        dude_pos = (i,a)
        grid[a][i] = '.'

assert( dude_pos is not None )

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
print(dude_pos)
dude_direction = UP

num_visited = 0
done = False
while(not done):
    if dude_pos[0] < 0 or dude_pos[0] >= len(grid[0]) or dude_pos[1] < 0 or dude_pos[1] >= len(grid):
        done = True
        continue

    if grid[dude_pos[1]][dude_pos[0]] == '.':
        grid[dude_pos[1]][dude_pos[0]] = 'X'
        num_visited += 1

    if dude_direction == UP:
        next_dude_pos = (dude_pos[0], dude_pos[1]-1)
        if grid[next_dude_pos[1]][next_dude_pos[0]] == '#':
            dude_direction = RIGHT
            next_dude_pos = dude_pos
    elif dude_direction == RIGHT:
        next_dude_pos = (dude_pos[0]+1, dude_pos[1])
        if grid[next_dude_pos[1]][next_dude_pos[0]] == '#':
            dude_direction = DOWN
            next_dude_pos = dude_pos
    elif dude_direction == DOWN:
        next_dude_pos = (dude_pos[0], dude_pos[1]+1)
        if grid[next_dude_pos[1]][next_dude_pos[0]] == '#':
            dude_direction = LEFT
            next_dude_pos = dude_pos
    elif dude_direction == LEFT:
        next_dude_pos = (dude_pos[0]-1, dude_pos[1])
        if grid[next_dude_pos[1]][next_dude_pos[0]] == '#':
            dude_direction = UP
            next_dude_pos = dude_pos

    dude_pos = next_dude_pos
    print(dude_pos)

print('done!')
print(num_visited)
