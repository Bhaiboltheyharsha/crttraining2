class stack:
    def __init__(self):
        self.arr=[]
        self.arr2=[]
    def push(self,element):
        self.arr.append(element)
    def stack_pop(self):
        self.arr.pop()
    def reverse_array(self):
        while len(self.arr)!=0:
            pop=self.arr.pop()
            self.arr2.append(pop)
        temp=self.arr2
        self.arr2=self.arr
        self.arr=temp
        
            #print(len(self.arr))
        #print(self.arr2)
        #print(self.arr)
    def linear_search(self,k):
        z=0
        for i in self.arr:
            if k==i:
                print('found at:',z)
            z=z+1
obj=stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
#obj.stack_pop()
print(obj.arr)
#obj.reverse_array()
#obj.stack_pop()
#print(obj.arr)
obj.linear_search(10)
