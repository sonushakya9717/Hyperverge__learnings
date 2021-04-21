class stack:
    def __init__(self):
        self.containers=[]

    def postfx(self,strng):
        result=""
        def prec(s):
            if s=="*" or s=="/":
                precedence=2
            elif s=="+" or s=="-":
                precedence=1
            elif s=="^":
                precedence=3
            else:
                precedence=0
            return precedence
        for j in strng:
            if j in ['+',"-","/","*","^"]:
                if len(self.containers)==0:
                    self.containers.append(j)
                else:
                    while len(self.containers)>0 and prec(self.containers[-1])>=prec(j):
                        operator=self.containers.pop()
                        result+=operator
                    else:
                        self.containers.append(j)
            elif j=="(":
                self.containers.append(j)
            
            elif j==")":
                while self.containers[-1]!="(":
                    operator=self.containers.pop()
                    result+=operator
                self.containers.pop()
            else:
                result+=j
        while len(self.containers)>0:
            operator=self.containers.pop()
            result+=operator
        
        return result
                

if __name__ == "__main__":
    a=stack()
    print(a.postfx("(a+b)*(c+d)"))
