def sliding_window_compare(input: list, n: int) -> int:
    if n < 0:
        return 0

    sum = 0
    for i in range(len(input) - n):
        if input[i+n] > input[i]:
            sum += 1
    return sum

f = open("advent of code input.txt", "r")
input: list = f.readlines()
f.close() 

input = list(map(int, input))

print(input)

print(sliding_window_compare(input, 1))
print(sliding_window_compare(input, 3))
print(sliding_window_compare(input, -1))