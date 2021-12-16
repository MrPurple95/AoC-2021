f = open("day10.txt", "r")

input = [l.strip() for l in f.readlines()]

f.close()

print(input)
d = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">"
    }

o = {"(", "[", "{" ,"<"}

close = {")", "]", "}" ,">"}

ds = {
    ")":  3,
    "]": 57,
    "}": 1197,
    ">": 25137
    }

es = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
    }

corrupt = []

expected = []

def checkLine(e , i , line):
    if(i == len(line)):
        
        return True

    elif line[i] in o:
        e.insert(0,d[line[i]])
        return checkLine(e, i + 1, line)

    elif line[i] != e[0]:
        corrupt.append(ds[line[i]])
        return False

    elif line[i] == e[0]:
        e.pop(0)
        return checkLine(e, i + 1, line)
        
lines = []

for l in input:
    e = []
    if checkLine(e, 0, l):
        expected.append(e)
        lines.append(l)
    

print(corrupt)
print(sum(corrupt))
print(expected)

scores = []

for e in expected:
    score = 0
    for c in e:
        score = score * 5 
        score = score + es[c]
    
    scores.append(score)

scores.sort()
print(scores)
n = len(scores) // 2
print(scores[int(n)])
print(int(n))
print(len(expected))
print(len(corrupt))
print(len(input))