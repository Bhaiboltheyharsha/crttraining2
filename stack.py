class stack:
    def __init__(self):
        self.arr=[]
        self.arr2=[]
    def push(self,element):
        self.arr.append(element)
    def stackpop(self):
        if len(self.arr)!=0:
            self.arr.pop()
        else:
            print('under flow')
    def isempty(self):
        if len(self.arr)!=0:
            return False
        else:
            return True
o=stack()
o.push(10)
o.push(20)
o.push(30)
o.push(40)
print(o.arr)
o.stackpop()
print(o.arr)
        
