##### Implementation of stack using list #####

# class stack:

#     def __init__(self):
#         self.container=[]

    
#     def push(self,value):
#         self.container.append(value)

#     def is_empty(self):
#         return len(self.container)==0

#     def pop(self):
#         return self.container.pop()
    
#     def peek(self):
#         return self.container[-1]
    
#     def size(self):
#         return len(self.container)
    
#     def whole_stack(self):
#         return self.container

# s=stack()

# s.push(72)
# s.push(76)
# s.push(71)

# print(s.pop())
# print(s.size())
# print(s.pop())
# print(s.peek())
# print(s.is_empty())
# print(s.pop())
# print(s.is_empty())


###### Balanced parenthesis ######

class stack:
    def __init__(self):
        self.container=[]
    
    def is_balanced(self,a):
        for i in a:
            if i in ["(","[","{"]:
                self.container.append(i)
            else:
                if len(self.container)==0:
                    return "not balanced"
                else:
                    current__char=self.container[-1]
                    if current__char=="(" and  i==")":
                        self.container.pop()
                    elif current__char=="{" and  i=="}":
                        self.container.pop()
                    elif current__char=="[" and  i=="]":
                        self.container.pop()
                    else:
                        return "not balanced"
        if len(self.container)==0:
            return 'is balanced'
        else:
            return "not balanced"
balanced=stack()
print(balanced.is_balanced("[{([)]}"))