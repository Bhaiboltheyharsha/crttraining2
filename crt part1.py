class stack:
    arr=[]
    size=5
    def push(self,element):
        if len(self.arr)<self.size:
            self.arr.append(element)
        else:
            return 'overflow'
    def stack_pop(self):
        if len(self.arr)==0:
            return 'under flow'
        else:
            self.arr.pop()
    def isempty(self):
        if len(self.arr)!=0:
            return False
        else:
            return True
    def prints(self):
        return self.arr
    def peek(self):
        return self.arr[-1]
    def reverse(self):
        temp=len(self.arr)
        for i in range(len(self.arr)):
            s
obj=stack()
print(obj.isempty())
print(obj.stack_pop())
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
print(obj.isempty())
print(obj.push(60))
print(obj.prints())
print(obj.isempty())
print(obj.peek())
