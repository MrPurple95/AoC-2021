f = open("day14.txt", "r")


pol = f.readline().strip()
print(pol)
f.readline()
rules = [l.strip().split(" -> ") for l in f.readlines()]
rules = {l[0]: l[1] for l in rules}
print(rules)

f.close()

pairs = {}
for i in range(len(pol) - 1):
    key = pol[i:i+2]
    if key in pairs:
        pairs[key] = pairs[key] + 1
    else:
        pairs[key] = 1
#pairs = [pol[i:i+2] for i in range(len(pol)-1)]

print(pairs)

count = {}

for i in range(len(pol)):
    if pol[i] in count:
        count[pol[i]] = count[pol[i]] + 1
    else:
        count[pol[i]] = 1
    
print(count)

for j in range(40):
    tmp_pairs = {}
    for key, value in pairs.items():
        if key not in tmp_pairs:
            tmp_pairs[key] = 0

        new_key1 = key[0] + rules[key]
        new_key2 = rules[key] + key[1]
        if rules[key] in count:
            count[rules[key]] = count[rules[key]] + value
        else:
            count[rules[key]] = value
        if new_key1 in tmp_pairs:
            tmp_pairs[new_key1] = tmp_pairs[new_key1] + value
        else:
            tmp_pairs[new_key1] = value
        if new_key2 in tmp_pairs:
            tmp_pairs[new_key2] = tmp_pairs[new_key2] + value
        else:
            tmp_pairs[new_key2] = value
    pairs = tmp_pairs

print(pairs)

print(count)

values = list(count.values())

values.sort()

print(values)

print(values[-1] - values[0])
