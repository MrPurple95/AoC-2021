def checkDown(i, j, input):
    if input[i+1][j] > input[i][j]:
        return True
    else: 
        return False

def checkUp(i,j,input):
    if input[i-1][j] > input[i][j]:
        return True
    else:
        return False

def checkRight(i,j,input):
    if input[i][j+1] > input[i][j]:
        return True
    else:
        return False

def checkLeft(i,j,input):
    if input[i][j-1] > input[i][j]:
        return True
    else:
        return False
f = open("day09_in.txt", "r")

input = [l.strip() for l in f.readlines()]

f.close()
#print(input)

nrRows = len(input) -1
rowLength = len(input[0]) -1

risks = []
lowpoints = []

for i in range(nrRows +1):
    for j in range(rowLength +1):
        if j > 0 and j < rowLength:
            if i > 0 and i < nrRows:
                if checkUp(i,j,input) and checkLeft(i,j,input) and checkDown(i,j,input) and checkRight(i,j,input):
                    risks.append(int(input[i][j]) + 1)
                    lowpoints.append((i,j))
            elif i == 0:
                if checkLeft(i,j,input) and checkDown(i,j,input) and checkRight(i,j,input):
                    risks.append(int(input[i][j]) + 1)
                    lowpoints.append((i,j))
            elif i == nrRows :
                if checkUp(i,j,input) and checkLeft(i,j,input) and checkRight(i,j,input):
                    risks.append(int(input[i][j]) + 1)
                    lowpoints.append((i,j))
        elif j == 0:
            if i > 0 and i < nrRows:
                if checkDown(i,j,input) and checkRight(i,j,input) and checkUp(i,j,input):
                    risks.append(int(input[i][j]) + 1)
                    lowpoints.append((i,j))
            elif i == 0:
                if checkDown(i,j,input) and checkRight(i,j,input):
                    risks.append(int(input[i][j]) + 1)
                    lowpoints.append((i,j))
            elif i == nrRows:
                if checkUp(i,j,input) and checkRight(i,j,input):
                    risks.append(int(input[i][j]) + 1)
                    lowpoints.append((i,j))
        elif j == rowLength:
            if i > 0 and i < nrRows:
                if checkDown(i,j,input) and checkLeft(i,j,input) and checkUp(i,j,input):
                    risks.append(int(input[i][j]) + 1)
                    lowpoints.append((i,j))
            if i == 0:
                if checkDown(i,j,input) and checkLeft(i,j,input):
                    risks.append(int(input[i][j]) + 1)
                    lowpoints.append((i,j))
            elif i == nrRows:
                if checkUp(i,j,input) and checkLeft(i,j,input):
                    risks.append(int(input[i][j]) + 1)
                    lowpoints.append((i,j))
                

#print(risks)
print(sum(risks))
#print(lowpoints)

basins = []

def checkBasin(i : int, j : int, basin : dict, input: list) -> None:
    if int(input[i][j]) == 9:
        return
    else:
        basin[(i,j)] = input[i][j]

        ui = i-1
        di = i+1
        lj = j-1
        rj = j+1
        if ui > 0:
            if (ui,j) not in basin:
                checkBasin(ui, j, basin, input)
        if di <= nrRows:
            if (di,j) not in basin:
                checkBasin(di, j, basin, input)
        if lj > 0:
            if (i,lj) not in basin:
                checkBasin(i, lj, basin, input)
        if rj <= rowLength:
            if (i,rj) not in basin:
                checkBasin(i, rj, basin, input)


for l in lowpoints:
    b = {}
    checkBasin(l[0], l[1], b, input)
    basins.append(b)

#print(len(basins))

sizes = [len(b) for b in basins]
sizes.sort(reverse=True)
print(sizes)
print(sizes[0] * sizes[1] * sizes[2])

def BFS(G, root):
    queue = []
    explored = [root]
    queue.append(root)
    while queue:
        v = queue.pop(0)

        up = (v[0] -1, v[1])
        down = (v[0] +1, v[1])
        left = (v[0] , v[1] -1)
        right = (v[0] , v[1] +1)
        if up[0] >= 0:
            if up not in explored and int(G[up[0]][up[1]]) != 9:
                explored.append(up)
                queue.append(up)
        if down[0] < nrRows:
            if down not in explored and int(G[down[0]][down[1]]) != 9:
                explored.append(down)
                queue.append(down)
        if left[1] >= 0:
            if left not in explored and int(G[left[0]][left[1]]) != 9:
                explored.append(left)
                queue.append(left)
        if right[1] < rowLength:
            if right not in explored and int(G[right[0]][right[1]]) != 9:
                explored.append(right)
                queue.append(right)
    
    return len(explored)

sizes = []

for l in lowpoints:
    sizes.append(BFS(input, l))


print(sizes)
print(len(sizes))
#print(basins)

sizes.sort(reverse=True)
print(sizes)

print(sizes[0] * sizes[1] * sizes[2])