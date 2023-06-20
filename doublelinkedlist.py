class node:
    def __init__(self,value):
        self.data=value
        self.prev=None
        self.next=None
class doublelinkedlist:
    def push(self,head,value):
        new_node=node(value)
        temp=head
        while temp.next!=None:
            temp=temp.next
            temp.prev=None
        temp.next=new_node
        new_node.prev=temp
    def prints(self,head):
        temp=head
        while temp!=None:
            print(temp.data,end='<->')
            temp=temp.next
ob=doublelinkedlist()
head=node(10)
q1=ob.push(head,29)
q2=ob.push(head,30)
q3=ob.push(head,40)
ob.prints(head)
print()
q4=ob.push(head,50)
ob.prints(head)
