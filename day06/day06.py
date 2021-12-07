f = open("day06_in.txt", "r")

input = f.readline().strip().split(',')

input = [int(n) for n in input]

print(input)

"""for i in range(256):
    count = 0
    for j in range(len(input)):
        if input[j] == 0:
            input[j] = 6
            count += 1
        else:
            input[j] -= 1
    for j in range(count):
        input.append(8)"""

fish = []

for i in range(9):
    fish.append(input.count(i))

print(fish)

for i in range(256):
    reset = fish[0]
    fish[0] = 0
    for j in range(8):
        fish[j] = fish[j + 1]
    fish[8] = reset
    fish[6] += reset

print(fish)
print(sum(fish))

fish = []

for i in range(9):
    fish.append(input.count(i))

print(fish)

for i in range(80):
    reset = fish[0]
    fish[0] = 0
    for j in range(8):
        fish[j] = fish[j + 1]
    fish[8] = reset
    fish[6] += reset

print(fish)
print(sum(fish))

#for i in range(256):
    
#print(input)
#print(len(input))

