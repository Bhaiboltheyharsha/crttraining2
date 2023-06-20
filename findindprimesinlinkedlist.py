class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class linkedlist:
    def push(self,head,element):
        new_node=node(element)
        temp=head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
    def findprime(self):
        temp=head
        while temp!=None:
            
            temp=temp.next
        return b
    def prints(self,head):
        temp=head
        while temp!=None:
            print(temp.data,end='->')
            temp=temp.next
ob=linkedlist()
head=node(20)
ob.push(head,10)
ob.push(head,25)
ob.push(head,2)
ob.push(head,3)
ob.prints(head)
print()
print(ob.findprime())
#ob.findprime()
