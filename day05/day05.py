f = open("day05_input.txt", "r")

input = f.readlines()

f.close()

input = [line.strip().replace(' -> ', ' ').replace(',', ' ').split() for line in input]
input = [list(map(int, l)) for l in input]

diagram = [[0 for i in range(1000)] for j in range(1000)]

for l in input:
    x1 = l[0]
    y1 = l[1]
    x2 = l[2]
    y2 = l[3]
    if x1 != x2 and y1 != y2:
        if abs(x1 - x2) == abs(y1 - y2):
            if y2 > y1:
                stepy = 1
            else:
                stepy = -1
            if x2 > x1:
                stepx = 1
            else:
                stepx = -1
            c = x1
            for r in range(y1, y2 + stepy, stepy):
                diagram[r][c] += 1
                c += stepx
    if x1 == x2 and y1 != y2:
        if y2 > y1:
            step = 1
        else:
            step = -1
        for r in range(y1, y2 + step, step):
            diagram[r][x1] += 1
    elif x1 != x2 and y1 == y2:
        if x2 > x1:
            step = 1
        else:
            step = -1
        for c in range(x1, x2 + step, step):
            diagram[y1][c] += 1

count = 0
for r in diagram:
    for c in r:
        if c > 1:
            count += 1
print(count)