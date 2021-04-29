# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None

#     def in_order_traversal(self):
#         array=[]
#         if self.left:
#             array+=self.left.in_order_traversal()
#         array.append(self.data)
#         if self.right:
#             array+=self.right.in_order_traversal()
#         return array

#     def pre_order(self):
#         elements=[]
#         elements.append(self.data)
#         if self.left:
#             elements+=self.left.pre_order()
#         if self.right:
#             elements+=self.right.pre_order()
#         return elements

    # def post_order(self):
    #     elements=[]
    #     if self.left:
    #         elements+=self.left.post_order()
    #     if self.right:
    #         elements+=self.right.post_order()
    #     elements.append(self.data)
    #     return elements



# def leaf_count(node):
#     if not node:
#         return 0
#     if not node.left and not node.right:
#         return 1
#     else:
#         return leaf_count(node.left)+leaf_count(node.right)

# if __name__=="__main__":
    # root=Node(1)
    # root.left=Node(2)
    # root.right=Node(3)
    # root.right.left=Node(4)
    # root.right.right=Node(5)
    # root.left.left=Node(6)
    # print("inorder traversal:-",root.in_order_traversal())
    # print("preorder traversal:-",root.pre_order())
    # print("postorder traversal:-",root.post_order())
    # print("No of leafs:-",leaf_count(root))



###########  iterative methods ######## 


# class Node:

#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None

#     def in_order_traversal(self):
#         array=[]
#         current=self
#         while len(array)>0 or current:
#             if current:
#                 array.append(current)
#                 current=current.left
#             else:
#                 current=array.pop()
#                 print(current.data,end=" ")
#                 current=current.right

#     def pre_order_traversal(self):
#         array=[]
#         current=self
#         while len(array)>0 or current:
#             if current:
#                 print(current.data,end=" ")
#                 array.append(current)
#                 current=current.left
#             else:
#                 current=array.pop()
#                 current=current.right
            


#     def pre_order(self):
#         elements=[]
#         elements.append(self.data)
#         if self.left:
#             elements+=self.left.pre_order()
#         if self.right:
#             elements+=self.right.pre_order()
#         return elements


# if __name__=="__main__":
#     root=Node(1)
#     root.left=Node(2)
#     root.right=Node(3)
#     root.right.left=Node(4)
#     root.right.right=Node(5)
#     root.left.left=Node(6)
#     # root.in_order_traversal()
#     # root.pre_order_traversal()
#     root.post_order_traversal()
