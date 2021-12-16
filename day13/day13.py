f = open("day13.txt", "r")

input = [l.strip() for l in f.read().split("\n\n")]

f.close()

#print(input)

cords = [list(map(int,l.split(","))) for l in input[0].split("\n")]

folds = [l.split()[2].split("=") for l in input[1].split("\n")]

#print(cords)
#print(folds)

for j in range(len(folds)):
    for i in range(len(cords)):
        if folds[j][0] == "x":
            if cords[i][0] > int(folds[j][1]):
                cords[i][0] =  (int(folds[j][1])) - (cords[i][0] - int(folds[j][1]))

        else:
            if cords[i][1] > int(folds[j][1]):
                cords[i][1] =  (int(folds[j][1])) - (cords[i][1] - int(folds[j][1]))

tuple_cords = []
for c in cords:
    tuple_cords.append((c[0],c[1]))

set_cords = {c for c in tuple_cords}
#print(set_cords)

max_x = 0
max_y = 0

for c in set_cords:
    if c[0] > max_x:
        max_x = c[0]
    if c[1] > max_y:
        max_y = c[1]

#print(max_x,max_y)

grid = [["." for i in range(max_y+1)] for j in range(max_x+1) ]

for c in set_cords:
    grid[c[0]][c[1]] = "#"

s = "\n"
for j in range(len(grid[0])):
    for i in range(len(grid)):
        s = s + grid[i][j]
    s = s + "\n"
    
print(s)

f = open("day13_2.txt", "r")

input = [l.strip() for l in f.read().split("\n\n")]

f.close()

#print(input)

cords = [list(map(int,l.split(","))) for l in input[0].split("\n")]

folds = [l.split()[2].split("=") for l in input[1].split("\n")]

#print(cords)
#print(folds)

for j in range(len(folds)):
    for i in range(len(cords)):
        if folds[j][0] == "x":
            if cords[i][0] > int(folds[j][1]):
                cords[i][0] =  (int(folds[j][1])) - (cords[i][0] - int(folds[j][1]))

        else:
            if cords[i][1] > int(folds[j][1]):
                cords[i][1] =  (int(folds[j][1])) - (cords[i][1] - int(folds[j][1]))

tuple_cords = []
for c in cords:
    tuple_cords.append((c[0],c[1]))

set_cords = {c for c in tuple_cords}
#print(set_cords)

max_x = 0
max_y = 0

for c in set_cords:
    if c[0] > max_x:
        max_x = c[0]
    if c[1] > max_y:
        max_y = c[1]

#print(max_x,max_y)

grid = [["." for i in range(max_y+1)] for j in range(max_x+1) ]

for c in set_cords:
    grid[c[0]][c[1]] = "#"

s = "\n"
for j in range(len(grid[0])):
    for i in range(len(grid)):
        s = s + grid[i][j]
    s = s + "\n"
    
print(s)