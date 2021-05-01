########## BINARY  SEARCH TREE  ############

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

    def LNR_method(self):
        elements=[]
        if self.left:
            elements+=self.left.LNR_method()
        elements.append(self.data)
        if self.right:
            elements+=self.right.LNR_method()

        return elements


    def NLR_method(self):
        elements=[]
        elements.append(self.data)
        if self.left:
            elements+=self.left.NLR_method()
        if self.right:
            elements+=self.right.NLR_method()
        return elements

    def Level_order(self):         
        queue=[]
        queue.append(self)
        while len(queue)>0:
            node=queue.pop(0)
            print(node.data)

            if node.left!=None:
                queue.append(node.left)
            
            if node.right!=None:
                queue.append(node.right)
    


    def LRN_method(self):
        elements=[]
        if self.left:
            elements+=self.left.LRN_method()
        if self.right:
            elements+=self.right.LRN_method()
        elements.append(self.data)
        return elements


    def search(self,data):
        if self.data==data:
            return True
        if data>self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False
        else:
            if self.left:
                return self.left.search(data)
            else:
                return False

  

def build_treee(elements):
    root=TreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root


if __name__=="__main__":
    numbers=[3,7,9,6,4,2]
    build_treee(numbers)
    print(build_treee(numbers).LNR_method())
    print(build_treee(numbers).NLR_method())
    print(build_treee(numbers).LRN_method())
    print(build_treee(numbers).search(90))
    build_treee(numbers).Level_order()