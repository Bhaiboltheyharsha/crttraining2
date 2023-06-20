



class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class bstree:
    def add_element(self,root,value):
        new_node=node(value)
        if new_node.value < root.value:
            if root.left != None:
                self.add_element(root.left,value)
                return 
            else:
                root.left = new_node
                return
        else:
            if root.right != None:
                self.add_element(root.right,value)
                return
            else:
                root.right = new_node
    def search(self,root,value):
        if root==value:
            print('found')
            return root
        if value < root.value and root.left is not None:
            return self.search(root.left,value)
        if value > root.data and root.right is not None:
            return self.search(root.right,value)
    def sumsubtree(self,root):
        sums=root.value
        if root.left is not None:
            sums=sums+self.sumsubtree(root.left)
        if root.right is not None:
            sums=sums + self.sumsubtree(root.right)
        return sums
    def height(self,root):
        if root == None:
            return -1
        left_height=self.height(root.left)
        right_height=self.height(root.right)
        return 1+max(left_height,right_height)
    def inorder(self,root):
        if root.left != None:
            self.inorder(root.left)
        print(root.value,end=' ')
        #sums=sums+root.value
        if root.right != None:
            self.inorder(root.right)
    def preorder(self,root):
        print(root.value,end=' ')
        if root.left != None:
            self.preorder(root.left)
        if root.right != None:
            self.preorder(root.right)
    def postorder(self,root):
        if root.left!= None:
            self.postorder(root.left)
        if root.right!=None:
            self.postorder(root.right)
        print(root.value)
    def levelorder(self,root):
        q=[]
        q.append(root)
        while len(q)!=0:
            ele = q.pop(0)
            print(ele.value,end=',')
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
            #print(ele.value)
obj=bstree()
root=node(10)
obj.add_element(root,20)
obj.add_element(root,24)
obj.add_element(root,4)
obj.add_element(root,2)
obj.add_element(root,40)
obj.add_element(root,30)
obj.add_element(root,6)
obj.levelorder(root)
print()
obj.inorder(root)

print()
print(obj.sumsubtree(root.right))
print(obj.height(root))
print(obj.height(root.left))
print(obj.height(root.left.right))
