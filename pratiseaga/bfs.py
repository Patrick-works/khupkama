graph={"A":['B','C'],
       "B":['A','D','E'],
       "C":['A','F'],
       "D":['B'],
       'E':['B','F'],
       'F':['C','E']
}

strt='A'
end='F'
def bfs(graph,strt):

    visited,bfst=[strt],[strt]
    while len(bfst)!=0:
        ver=bfst.pop(0)
        for i in graph[ver]:
            if i not in visited:
                visited.append(i)
                bfst.append(i)
    return visited

print(bfs(graph,strt))
from collections import deque

def bfs_paths(graph, start, end):
    queue = deque([(start, [start])])
    all_paths = []

    while queue:
        node, path = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == end:
                all_paths.append(path + [neighbor])
            elif neighbor not in path:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return all_paths


def bfs_multiple_paths(graph, start, end):
    queue = [(start, [start])]
    all_paths = []
    print(queue)
    while queue:
        node, path = queue.pop(0)
        for neighbor in graph[node]:
            print("pathis",end="")
            print(path)

            if neighbor == end:
                all_paths.append(path + [neighbor])
                 # Remove the first element as in a queue

            elif neighbor not in path:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                print("new path is",end='')
                print(new_path)
                print("queue is ",end='')
                print(queue)# Remove the first element as in a queue

    return all_paths
start_node = 'A'
end_node = 'F'
all_paths = bfs_multiple_paths(graph, start_node, end_node)
print(all_paths)
# if all_paths:
#     for i, path in enumerate(all_paths, 1):
#         print(f"Path {i} from {start_node} to {end_node}: {path}")
# else:
#     print(f"No paths from {start_node} to {end_node} found.")
