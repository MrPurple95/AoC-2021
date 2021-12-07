f = open("day03_input.txt", "r")

input = f.readlines()
f.close()

input = [x.strip() for x in input]
#print(input)

mostCommonBit = ''
leastCommonBit = ''

for i in range(len(input[0])):
    count0 = 0
    count1 = 0
    for j in range(len(input)):
        if input[j][i] == '0':
            count0 += 1
        elif input[j][i] == '1':
            count1 += 1
    #print(count0, count1)
    if count0 > count1:
        mostCommonBit += '0'
        leastCommonBit += '1'
    else:
        mostCommonBit += '1'
        leastCommonBit += '0'

print("mostCommonBit: ", mostCommonBit)

#leastCommonBit = ''.join(['1' if i == '0' else '0' for i in mostCommonBit])

print("leastCommonBit: ", leastCommonBit)

gammaRate = int(mostCommonBit, 2)
epsilonRate = int(leastCommonBit, 2)
powerConsumption = gammaRate * epsilonRate

print("gammaRate: ", gammaRate, "epsilonRate: ", epsilonRate, "powerConsumption: ", powerConsumption)

oxrate = input.copy()
scrubRating = input.copy()

for i in range(len(input[0])):
    count0 = 0
    count1 = 0
    for x in oxrate:
        if x[i] == '0':
            count0 += 1
        elif x[i] == '1':
            count1 += 1
    if count0 > count1:
        oxrate = [x for x in oxrate if x[i] == '0']
    else:
        oxrate = [x for x in oxrate if x[i] == '1']
    if len(oxrate) == 1:
        break

for i in range(len(input[0])):
    count0 = 0
    count1 = 0
    for x in scrubRating:
        if x[i] == '0':
            count0 += 1
        elif x[i] == '1':
            count1 += 1
    if count0 > count1:
        scrubRating = [x for x in scrubRating if x[i] == '1']
    else:
        scrubRating = [x for x in scrubRating if x[i] == '0']
    if len(scrubRating) == 1:
        break

#print(oxrate)
#print(scrubRating)

oxrate = int(oxrate[0], 2)
scrubRating = int(scrubRating[0], 2)

life = oxrate * scrubRating

print (oxrate, scrubRating, life)

#print(input)

