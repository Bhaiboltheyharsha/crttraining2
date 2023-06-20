l=[1,23,34,1,34,3,15,25,22,34,34,22,54,29,73]
for i in range(1,len(l)):
    j=i
    while l[j-1]>l[j] and j>0:
        l[j-1],l[j]=l[j],l[j-1]
        j=j-1
print(l)
