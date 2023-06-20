def bfs(graph,start):
    q=[start]
    visited=[start]
    while len(q)!=0:
        ele=q.pop(0)
        print(ele)
        for i in graph[ele]:
            if i not in visited:
                q.append(i)
                visited.append(i)
    print(visited)
d={
    'a':['b','c'],
    'b':['a','d'],
    'c':['a','d'],
    'd':['e','c','b'],
    'e':['d']
    }
bfs(d,'d')
