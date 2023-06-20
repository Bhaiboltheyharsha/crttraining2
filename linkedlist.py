class node:
    def __init__(self,element):
        self.element=element
        self.next=None
class linkedlsit:
    def addelementlast(self,head,value):#ADDING AT LAST
        new_node=node(value)
        temp=head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
    def removingelementlast(self):
        temp=head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
    def addatfirst(self,head,value):#ADDING AT FIRST
        new_node=node(value)
        new_node.next=head
        head=new_node
        return head
    def prints(self):
        temp=head
        while temp!=None:
            print(temp.element,end='->')
            temp=temp.next
    def insert_at_position(self,head,pos,value):
        prev=None
        current=head
        new_node=node(value)
        while pos!=0:
            prev=current
            current=current.next
            pos=pos-1
        prev.next=new_node
        new_node.next=current
o=linkedlsit()
head=node(10)
o.addelementlast(head,20)
o.addelementlast(head,30)
o.addelementlast(head,40)
#o.prints()
head=o.addatfirst(head,0)
#o.removingelementlast()
#o.prints()
o.insert_at_position(head,5,69)
#head=o.addatfirst(head,220)
o.prints()
