
########## Check if Array is Sorted ########

a=list(map(int,input().split()))
def is__sorted(a):
    tem=a[0]
    j=1
    while j<len(a):
        if a[j]==tem or a[j]>tem:
            tem=a[j]
        else:
            return False
        j+=1
    if j==len(a):
        return True
print(is__sorted(a))
