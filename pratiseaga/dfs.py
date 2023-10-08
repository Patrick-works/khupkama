graph={"A":['B','C'],
       "B":['A','D','E'],
       "C":['A','F'],
       "D":['B'],
       'E':['B','F'],
       'F':['C','E']
}
strt='B'
visited, dft = [strt], [strt]
g=len(graph.keys())
def dfs(graph,strt):

       while len(dft)!=0:
              ver = dft.pop(-1)
              for i in graph[ver]:
                     if i not in visited:
                            visited.append(i)
                            dft.append(i)
                            break

       while len(visited)!=g:
              for i in (reversed(visited)):
                     for j in graph[i]:
                            if j not in visited:
                                   visited.append(j)
       return(visited)
def dfs_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for neighbor in graph[start]:
        if neighbor not in path:
            new_paths = dfs_paths(graph, neighbor, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths
start_node = 'A'
end_node = 'F'

all_paths = dfs_paths(graph, start_node, end_node)

print(dfs(graph,strt))
print(all_paths)

