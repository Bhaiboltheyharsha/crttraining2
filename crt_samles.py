class flower:
    def __init__(self,name,value):
        self.name=name
        self.value=value
        self.next=None
        #self.total=0
class store:
    def push(self,head,name,value):
        total=0
        new_node=flower(name,value)
        temp=head
        while temp.next!=None :
            if temp.name == name:
                new_node.value=temp.value+new_node.value
            temp=temp.next
        temp.next=new_node
    def pop(self,head,name,value):
        new_node=flower(name,value)
        temp=head
        while temp!=None:
            if temp.name == name:
                temp.value=temp.value-new_node.value
            temp=temp.next
    def prints(self,head):
        temp=head
        while temp!=None:
            print(temp.name,temp.value,end='->')
            temp=temp.next
obj=store()
head=flower('jasmine',20)
obj.push(head,'rose',20)
obj.push(head,'lotus',908)
obj.push(head,'lily',40)
obj.push(head,'lotus',39)
obj.prints(head)
#obj.pop(head,'rose',60)
#obj.pop(head,'lily',23)
print()
obj.prints(head)
