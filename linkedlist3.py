class node:
    def __init__(self,element):
        self.element=element
        self.next=None
class linkedlist:
    def __init__(self):
        self.b=0
    def push(self,head,value):
        new_node=node(value)
        temp=head
        while temp.next!=None:
            temp=temp.next
            self.b=self.b+1
        temp.next=new_node
    def reverse_first_half(self,head,n):
        first=head
        cur= head
        prev= None
        while n!=0:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            n = n-1
        first.next=cur
        return prev
    def reverse(self,head):
        cur=head
        prev=None
        while cur!=None:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        return prev
    def prints(self,head):
        temp=head
        while temp!=None:
            print(temp.element,end='->')
            temp=temp.next
ob=linkedlist()
head=node(10)
ob.push(head,30)
ob.push(head,699)
ob.push(head,69)
ob.push(head,40)
ob.push(head,50)
ob.prints()
print('\n')
head=ob.reverse_first_half(int(input()))
#head=ob.reverse()
ob.prints()
