# class queue:
#     def __init__(self):
#         self.container=[]

#     def peek(self):
#         return self.container[-1]

#     def pop(self):
#         return self.container.pop()

#     def push(self,val):
#         self.container.insert(0,val)
    
#     def is_empty(self):
#         return len(self.container)==0
    
#     def length(self):
#         return len(self.container)
#     def show(self):
#         print(self.container)

# if __name__ == "__main__":
#     a=queue()
#     a.push(5)
#     a.push(9)
#     a.push(9)
#     print(a.is_empty())
#     print(a.length())
#     a.show()
    


##### Queue using stacks  #####

class queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    
    def push(self,val):
        self.stack1.append(val)

    def pop(self):
        if len(self.stack1)==0 and len(self.stack2)==0:
            return "Queue is empty"
        elif len(self.stack1)>0 and len(self.stack2)==0:
            while len(self.stack1)>0:
                element=self.stack1.pop()
                self.stack2.append(element)
            return self.stack2.pop()
        else:
            return self.stack2.pop()
    


if __name__ == "__main__":
    a=queue()
    a.push(5)
    a.push(7)
    a.push(8)
    a.push(9)
    a.push(8)
    a.pop()
    print(a.pop())