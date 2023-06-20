class stack:
    def __init__(self):
        self.arr=[]
    def push(self,element):
        self.arr.append(element)
    def stack_pop(self):
        self.arr.pop()
    def binary_search(self,k):
        self.arr.sort()
        if len(self.arr)!=0:
            low=0
            high=len(self.arr)-1
            while low<=high:
                mid=((low+high)//2)
                if self.arr[mid]==k:
                    print('element found at:',mid)
                    break
                elif k < self.arr[mid]:
                    high=mid-1
                elif k > self.arr[mid]:
                    low=mid+1
            else:
                print('element is not found ')
                
obj=stack()
obj.push(0)
obj.push(10)
obj.push(20)
obj.push(15)
obj.push(40)
obj.push(50)
#print(obj.arr)
obj.stack_pop()
print(obj.arr)
k=int(input('enter the element to search:'))
obj.binary_search(k)
print(obj.arr)
