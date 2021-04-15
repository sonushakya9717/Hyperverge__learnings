
######### selection sort ##########

def selection__sort(a):
    for i in range(len(a)):
        min1=i
        for j in range(i,len(a)):
            if a[j]<a[min1]:
                min1=j
        a[i],a[min1]=a[min1],a[i]
    return a

a=list(map(int,input().split()))
print(selection__sort(a))
