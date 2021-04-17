 ##### Finding multiple missing elements in a list #####
 
a=list(map(int,input().split()))
length=max(a)
i=1
while i<length:
    if i not in a:
        print(i)
    i+=1
