##### quick sort #####

def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        lesser_elements=[]
        greater_elements=[]
        pivot=arr.pop()
        for j in arr:
            if j >pivot:
                greater_elements.append(j)
            else:
                lesser_elements.append(j)
        return quicksort(lesser_elements)+[pivot]+quicksort(greater_elements)

print(quicksort([8,7,5,6,4,1,9]))