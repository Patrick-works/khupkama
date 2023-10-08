graph={"A":[['B',12,6],['C',7,8]],
       "B":[['A',12,5],['D',6,8],['E',8,9]],
       "C":[['A',7,5],['F',10,7]],
       "D":[['B',6,6]],
       'E':[['B',8,6],['F',3,7]],
       'F':[['C',10,8],['E',3,9]]
}
for k in graph:
       for v in graph[k]:
              m=v.pop(-1)
              n=v.pop(-1)
              v.append(m+n)

print(graph)
ruf=[]
def check_tc(path):
    colts=0
    z=len(path)
    for i in range(0,z):
        if i !=z-1:
            for j in graph[path[i]]:
                if j[0] == path[i + 1]:
                    colts = colts + j[-1]
    return colts



def astar(graph, start, end):
    stack = [(start, [start])]
    all_paths = []
    tc,pc=0,[]
    while stack:
        node, path = stack.pop(-1)
        if node == end:
            cost=check_tc(path)
            all_paths.append(path)
            pc.append(cost)
        for neighbor in graph[node]:
            neighbor=neighbor[0]
            if neighbor not in path:
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))
    return all_paths,pc

start_node = 'A'
end_node = 'E'

all_paths,tot =astar(graph, start_node, end_node)
z=tot.index(min(tot))
print("print the best possible path using astar is ",all_paths[z],"with a cost of ",tot[z])
