###### linear search #####

def linearSearch(arr,element):
    i=0
    while i<len(arr):
        if arr[i]==element:
            return "the element is present at index :-",i
        i+=1
    return -1

arr=[1,9,7,6,6,5,3]
print(linearSearch(arr,75))