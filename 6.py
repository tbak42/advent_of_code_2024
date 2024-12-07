import numpy as np

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
BLOCK = 4
VISITED = 5

DATA_FILE = 'd6b.txt'
with open(DATA_FILE) as f:
    data = f.read().splitlines()

original_grid = np.zeros( (len(data[0]), len(data) ), np.int8)
grid_width = original_grid.shape[1]
grid_height = original_grid.shape[0]

original_dude_pos = None
data = list(map(list, data))
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '^':
            original_dude_pos = (x,y)
            # original_grid[x][y] = 1 << UP
        if data[y][x] == '#':
            original_grid[x][y] = 1 << BLOCK

print(original_grid)
assert( original_dude_pos is not None )


num_cycles = 0
for obs_y in range(grid_height):
    print('{}/{}'.format(obs_y,grid_height))
    for obs_x in range(grid_width):
        # print('obs {},{}'.format(obs_x,obs_y))

        if original_grid[obs_x][obs_y] & (1 << BLOCK) > 0:
            continue
        if original_dude_pos == (obs_x, obs_y):
            continue

        dude_pos = original_dude_pos
        dude_direction = UP
        grid = np.copy(original_grid)
        grid[obs_x][obs_y] += (1 << BLOCK)

        num_visited = 0
        done = False
        while(not done):
            #if dude_pos[0] < 0 or dude_pos[0] >= grid_width or dude_pos[1] < 0 or dude_pos[1] >= grid_height:
                #continue
            #print(grid)

            if grid[dude_pos[0]][dude_pos[1]] & (1 << dude_direction) > 0:
                # print('cycle found!')
                num_cycles += 1
                done = True

            grid[dude_pos[0]][dude_pos[1]] += 1 << dude_direction
            if grid[dude_pos[0]][dude_pos[1]] & (1<<VISITED) == 0:
                grid[dude_pos[0]][dude_pos[1]] += 1 << VISITED
                num_visited += 1

            if dude_direction == UP:
                next_dude_pos = (dude_pos[0], dude_pos[1]-1)
                if next_dude_pos[1] < 0:
                    done = True
                    continue
                if grid[next_dude_pos[0]][next_dude_pos[1]] & (1<<BLOCK) > 0:
                    dude_direction = RIGHT
                    next_dude_pos = dude_pos
            elif dude_direction == RIGHT:
                next_dude_pos = (dude_pos[0]+1, dude_pos[1])
                if next_dude_pos[0] >= grid_width:
                    done = True
                    continue
                if grid[next_dude_pos[0]][next_dude_pos[1]] & (1<<BLOCK) > 0:
                    dude_direction = DOWN
                    next_dude_pos = dude_pos
            elif dude_direction == DOWN:
                next_dude_pos = (dude_pos[0], dude_pos[1]+1)
                if next_dude_pos[1] >= grid_height:
                    done = True
                    continue
                if grid[next_dude_pos[0]][next_dude_pos[1]] & (1<<BLOCK) > 0:
                    dude_direction = LEFT
                    next_dude_pos = dude_pos
            elif dude_direction == LEFT:
                next_dude_pos = (dude_pos[0]-1, dude_pos[1])
                if next_dude_pos[0] < 0:
                    done = True
                    continue
                if grid[next_dude_pos[0]][next_dude_pos[1]] & (1<<BLOCK) > 0:
                    dude_direction = UP
                    next_dude_pos = dude_pos

            dude_pos = next_dude_pos
            # print(dude_pos)


print('done!')
print(num_visited)
print(num_cycles)
