############ Merge Sort #########  

def merge(left,right):
    sorted_lst=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_lst.append(left[i])
            i+=1
        else:
            sorted_lst.append(right[j])
            j+=1
    while i<len(left):
        sorted_lst.append(left[i])
        i+=1
    while j<len(right):
        sorted_lst.append(right[j])
        j+=1
    return sorted_lst

def merge__sort(a):
    if len(a)==1:
        return a
    else:
        mid=len(a)//2
        left=merge__sort(a[:mid])
        right=merge__sort(a[mid:])
        return merge(left,right)

a=[9,8,7,5,6,4,1]
print(merge__sort(a))
