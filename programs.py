l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l2=list(input())
for i in range(0,len(l2)):
    for j in range(i,len(l2)):
        if l.index(l2[i]) > l.index(l2[j]):
            temp=l2[i]
            l2[i]=l2[j]
            l2[j]=temp
print(*l2,sep='')
