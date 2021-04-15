
########## Bubble sort ###########
a=list(map(int,input().split()))
def bubble__sort(a):
    flag=False
    for i in range(1,len(a)+1):
        if flag==True:
            break
        flag=True
        for j in range(len(a)-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                flag=False
    return a
print(bubble__sort(a))
