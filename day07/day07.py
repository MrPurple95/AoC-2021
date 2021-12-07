f = open("day07_in.txt", "r")

input =[int(n) for n in f.readline().strip().split(',')]

f.close()
print(input)

input.sort()


print(input)

median = input[(len(input) //2)]

sums = []

#for n in range(min(input), max(input) + 1):
#    temp = []
#    for i in range(len(input)):
#        temp.append(sum(range(abs(n - input[i]) + 1)))
#    sums.append(sum(temp))

#print(min(sums))
#print(sorted(sums))

#print(input)

#test = [16,1,2,0,4,2,7,1,2,14]

mean = round(sum(input) / len(input))
# https://www.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/
res = [sum(((((k- n) * (k-n)) + abs(k-n)) // 2) for n in input) for k in range(mean-1, mean+2)]

print(mean)
print(res)
print(min(res))

# https://en.wikipedia.org/wiki/Triangular_number
def triangleNumber(n):
    return (n * (n +1)) // 2
# https://www.resetera.com/threads/advent-of-code-2021.521820/post-78259041

res = [sum(triangleNumber(abs(n-k)) for n in input) for k in range(mean-1, mean+2)]

print(res)

print(min(res))

#print(median)
#print(sum(input))



#print(sorted(test))

#print(sum(input) // len(input))