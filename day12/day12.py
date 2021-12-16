import sys
f = open("day12.txt", "r")

input = [l.strip() for l in f.readlines()]

f.close()

print(input)

nodes = [l.split('-') for l in input]

nodes = list({i for l in nodes for i in l})

#for l in nodes:
#    for c in l:
#        if 

paths = [l.split('-') for l in input]

node_paths = { n: set() for n in nodes}

print(nodes)
print(paths)
#print(node_paths)

for p in paths:
    node_paths[p[0]].add(p[1])
    node_paths[p[1]].add(p[0])

print(node_paths)

lower_nodes = {n for n in nodes if n.islower()}

def find_paths(G, s, e,):
    visited = []
    paths = []
    path = ""

    find_path(G, s, e, path, paths, visited, "")

    print(len(paths))


def find_path(G, s, e, path, paths, visited, small):
    path = path + s  + " "
    
    #print(path)
    if s == e:
        paths.append(path.strip())
        #print(path)
        return
    else:
        visited.append(s)
        for v in G[s]:
            if v == "start":
                continue
            elif v == "end":
                find_path(G, v, e, path, paths, visited, small)
            elif v in lower_nodes and v not in visited:
                find_path(G, v, e, path, paths, visited, small)
            elif v not in lower_nodes:
                find_path(G, v, e, path, paths, visited, small)
            elif small == "" and v in lower_nodes:
                find_path(G, v, e, path, paths, visited, v)
    visited.remove(s)
            

find_paths(node_paths, "start", "end")
#print(lower_nodes)
#print(node_paths["start"])