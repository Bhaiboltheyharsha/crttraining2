class stack:
    def __init__(self):
        self.arr=[]
        self.firsthalf=[]
        self.secondhalf=[]
    def push(self,element):
        self.arr.append(element)
    def popo(self):
        self.arr.pop()
    def halfreverse(self):
        low=0
        high=len(self.arr)-1
        mid=((low+high)//2)
        for i in range(mid,-1,-1):
            self.firsthalf.append(self.arr[i])
        for i in range(high,mid,-1):
            self.secondhalf.append(self.arr[i])
        self.arr=self.firsthalf+self.secondhalf

stin=input()
ob=stack()
for i in list(stin):
    ob.push(i)
ob.balancedstring()
ob.push('(')
ob.push('(')
ob.push(')')
ob.push(')')
ob.halfreverse()
#print(ob.arr)
#ob.popo()
#print(ob.arr)
ob.balancedstring()

