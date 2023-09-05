graph={"A":['B','C'],
       "B":['A','D','E'],
       "C":['A','F'],
       "D":['B'],
       'E':['B','F'],
       'F':['C','E']
}


def bfs(graph, strt):
    visited = {strt}
    q, bfsl = [strt], [strt]
    while len(q) != 0:
        ver = q.pop(0)
        for i in graph[ver]:
            if i not in visited:
                q.append(i)
                bfsl.append(i)
                visited.add(i)

    return bfsl

def dfs(graph, strt):
    visited.add(strt)
    q, dfsl = [strt], [strt]
    while len(q) != 0:
        ver = q.pop(-1)
        for i in graph[ver]:
            if i not in visited:
                q.append(i)
                dfsl.append(i)
                visited.add(i)

                break
    for i in bfs(graph,strt):

        if i not in visited:

            return dfsl +dfs(graph,i)



    return dfsl




strt="A"
visited = set()
print(bfs(graph, strt))
print(dfs(graph, strt))


def graphpaths(graph, start_node, end_node):
    queue = [(start_node, [start_node])]
    visited = set()
    paths = []

    while queue:
        print(queue)
        node, path = queue.pop(0)
        visited.add(node)
        if node == end_node:
            paths.append(path)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return paths


print(graphpaths(graph,"A","F"))

