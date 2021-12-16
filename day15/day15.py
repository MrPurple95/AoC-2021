f = open("day15.txt", "r")

import heapq

input = [list(map(int,list(l.strip()))) for l in f.readlines()]

#input = [int(c) for l in input for c in l]

f.close()

print(input)

def recontruct_path(cameFrom :dict, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.insert[0, current]
    return total_path

def A_star(start, goal, h):
    openSet = []
    heapq.heappush(openSet, start)
    cameFrom = [[0 for i in range(len(input[0]))] for j in range(len(input))]

    gScore = [[(float("inf"),i ,j) for i in range(len(input[0]))] for j in range(len(input))]
    gScore[start[2]][start[1]] = (0, start[1], start[2])
    heapq.heapify(gScore)
    print(gScore)

    fScore = [[(float("inf"),i,j) for i in range(len(input[0]))] for j in range(len(input))]
    fScore[start[2]][start[1]] = h(start, goal)
    heapq.heapify(fScore)

    print(fScore)

    while openSet:
        current = fScore[0][0]
        print(current)
        if current[1] == len(input) - 1 and current[2] == len(input) - 1:
            return recontruct_path(cameFrom, current)
        
        openSet.remove(current)
        for i in range(current[1] -1, current[1] +2):
            for j in range(current[2] -1, current[2] +2):
                if i < 0 or j < 0 or i >= len(input) or j >= len(input):
                    continue
                tentative_gScore = gScore[current[1]][current[2]] + input[i][j]
                if tentative_gScore < gScore[i][j]:
                    cameFrom[i][j] = current
                    gScore[i][j] = tentative_gScore
                    fScore[i][j] = tentative_gScore + heuristic()
                    
                    

def heuristic(n, goal):
    c = (goal[0] - n[1]) + (goal[1] - n[2])
    c = (c, n[1],  n[2])
    return c

A_star((0,0,0),(100,100),heuristic)



print(len(input[0]))
print(len(input))