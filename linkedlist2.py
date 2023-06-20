class node:
    def __init__(self,element):
        self.element=element
        self.next=None
class linkedlist:
    def appends(self,head,element):
        new_node=node(element)
        temp=head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
    def prints(self,head):
        temp=head
        while temp!=None:
            print(temp.element,end='->')
            temp=temp.next
    def insert_at_position(self,head,pos,value):
        new_node=node(value)
        prev=None
        curr=head
        while pos!=0:
            prev=curr
            curr=curr.next
            pos=pos-1
        prev.next=new_node
        new_node.next=curr
    def add_at_first(self,head,value):
        new_node=node(value)
        new_node.next=head
        head=new_node
        return head
    def reverse(self,head):
        cur=head
        prev=None
        while cur!=None:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        return prev
s=linkedlist()
for i in range(5):
    if i==0:
        head=node(int(input()))
    else:
        s.appends(head,int(input()))
#s.insert_at_position(head,2,int(input()))
#s.prints()
#head=s.add_at_first(head,60)
#s.reverse(head)
s.prints(head)
print()
head=s.reverse(head)
s.prints(head)
