f = open("day08_in.txt", "r")

input = [l.strip().split(" | ") for l in f.readlines()]
outputVals = [l[1].split() for l in input]
mapVals = [sorted(l[0].split(), key=len) for l in input]

f.close()
print(outputVals)
print(mapVals)


count = 0
for l in outputVals:
    for v in l:
        n = len(v)
        if n == 2 or n == 3 or n == 4 or n == 7:
            count +=1
            
dicts = []

for l in mapVals:
    d= {}
    d[8] = l[-1]
    l.pop(-1)
    d[1] = l[0]
    l.pop(0)
    d[7] = l[0]
    l.pop(0)
    d[4] = l[0]
    l.pop(0)
    d[3] = [s for s in l if len(s) == 5 and all([x in s for x in d[1]])][0]
    l.remove(d[3])
    d[9] = [s for s in l if len(s) == 6 and all([x in s for x in d[4]])][0]
    l.remove(d[9])
    d[5] = [s for s in l if len(s) == 5 and all([x in d[9] for x in s])][0]
    l.remove(d[5])
    d[2] = [s for s in l if len(s) == 5][0]
    l.remove(d[2])
    d[6] = [s for s in l if all([x in s for x in d[5]])][0]
    l.remove(d[6])
    d[0] = l[0]
    nd = {}
    for key, value in d.items():
        nd["".join(sorted(value))] = key
        
    dicts.append(nd)

print(dicts)

values = []

print(outputVals[0])
print(dicts[0])

for i in range(len(outputVals)):
    s = ""
    for v in outputVals[i]:
        s += str(dicts[i]["".join(sorted(v))])
    values.append(int(s))

print(values)
print(sum(values))
