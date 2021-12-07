f = open("day02_input.txt", "r")

input = f.readlines()
f.close()

print(input)

direction = [x.split(' ')[0] for x in input]
length = [int(x.split(' ')[1]) for x in input]

print(direction)
print(length)
print(len(direction), len(length))

horizontal = 0
depth = 0

for i in range(len(direction)):
    if direction[i] == 'forward':
        horizontal += length[i]
    elif direction[i] == 'down':
        depth += length[i]
    elif direction[i] == 'up':
        depth -= length[i]

print(horizontal, depth, horizontal*depth)

horizontal = 0
depth = 0
aim = 0

for i in range(len(direction)):
    if direction[i] == 'forward':
        horizontal += length[i]
        depth += aim * length[i]
    elif direction[i] == 'down':
        aim += length[i]
    elif direction[i] == 'up':
        aim -= length[i]

print(horizontal, depth, horizontal*depth)