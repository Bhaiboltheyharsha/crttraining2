class queue:
    def __init__(self):
        self.arr=[]
        self.temp=[]
    def push(self,element):
        self.temp.append(element)
    def enqueue(self,ele):
        #self.temp.append(ele)
        while len(self.temp)!=0:
            pop_ele=self.temp.pop(0)
            self.arr.append(pop_ele)
        while len(self.arr)!=0:
            pop_ele=self.arr.pop(0)
            self.arr.append(pop_ele)
    def dequeue(self):
        self.arr.pop(0)
obj=queue()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
print(obj.arr)
print(obj.temp)
#print(obj.arr)
obj.enqueue(40)
print(obj.arr)
print(obj.temp)
