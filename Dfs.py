graph={"A":['B','C'],
       "B":['A','D'],
       "C":['A','F'],
       "D":['B'],
       'E':['B','F'],
       'F':['C','E']
}
def bfs(graph,strt):
       visited={strt}
       q,bfsl=[strt],[strt]
       while len(q)!= 0:
              ver=q.pop(0)
              for i in graph[ver]:
                     if i not in visited:
                            q.append(i)
                            bfsl.append(i)
                            visited.add(i)

       return bfsl
print(bfs(graph,"B"))


def bfspaths(graph, start, end):
       visited={start}
       q,bf=[start],[start]
       z=[]
       while len(q)!=0:
              ver=q.pop(-1)
              for i in graph[ver]:
                     if i==end:
                            bf.append(i)
                            break
                     if i not in visited:
                            q.append(i)
                            bf.append(i)
                            visited.add(i)
                            break

       return bf







start_node = 'A'
end_node = 'E'
print(bfspaths(graph, start_node, end_node))
