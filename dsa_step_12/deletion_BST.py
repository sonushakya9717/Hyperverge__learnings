class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def add_child(self,val):
        if self.data==val:
            return
        elif val<self.data:
            if self.left != None:
                self.left.add_child(val)
            else:
                self.left=TreeNode(val)
        else:
            if self.right != None:
                self.right.add_child(val)
            else:
                self.right=TreeNode(val)
    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self.data

    def delete(self,data):
        if data<self.data:
            if self.left:
                self.left=self.left.delete(data)

        elif data>self.data:
            if self.right:
                self.right=self.right.delete(data)

        else:
            if self.right==None and self.left==None:
                return None
            if self.left==None:
                return self.right
            if self.right==None:
                return self.left
            else:
                max_val=self.left.max()
                self.data=max_val
                self.left=self.left.delete(max_val)
        return self


if __name__ == "__main__":
    a=TreeNode(10)
    a.add_child(5)
    a.add_child(12)
    a.add_child(4)
    a.add_child(6)
    a.add_child(11)
    a.add_child(20)
    a.delete(5)