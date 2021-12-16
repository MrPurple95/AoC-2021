f = open("day11.txt", "r")

input = [l.strip() for l in f.readlines()]

f.close()

print(input)

grid = []

for l in input:
    line = []
    for c in l:
        line.append(int(c))
    grid.append(line)

print(grid)

flashes = 0
step = 0
while True:
    flashQueue = []
    step = step + 1

    # 1 Increase all by one then count flashes.
    for j in range(10):
        for k in range(10):
            grid[j][k] = grid[j][k] +1
            if grid[j][k] == 10:
                flashQueue.append((j,k))
    # 2
    while flashQueue:
        f = flashQueue.pop(0)
        j = f[0]
        k = f[1]
        for row in range(j-1,j+2):
            for col in range(k-1,k+2):
                if row < 10 and col < 10 and row > -1 and col > -1:
                    grid[row][col] = grid[row][col] + 1
                    if grid[row][col] == 10:
                        flashQueue.append((row,col))

    # 3 count flashes and reset to 0
    for j in range(10):
        for k in range(10):
            if grid[j][k] > 9:
                flashes = flashes + 1
                grid[j][k] = 0

    flashed = [True if c == 0 else False for l in grid for c in l]
    if all(flashed):
        break

    

    
    
print(flashes)
print(grid)
print(step)

