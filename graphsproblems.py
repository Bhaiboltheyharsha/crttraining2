def  graph(graph,start,last):
    q=[start]
    visited=[start]
    while len(q)!=0:
        ele=q.pop(0)
        print(ele)
        graph[ele]=[]
        for i in graph[ele]:
            if i not in visited:
                if i != last:
                    temp=False
                    q.append(i)
                    visited.append(i)
                elif i == last:
                    q.append(i)
                    visited.append(i)
                    temp=True
                    print(*visited,sep='->')
                    print('path found')
                    break

d={
    }
for i in range(int(input())):
    ll=[]
    first,last=input().split('->')
    ll.append(last)
    if i not in d:
        d[first]=ll
print('enter the desired path:')
f,l=input().split('->')
graph(d,f,l)
