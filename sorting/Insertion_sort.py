############# Insertion Sort ########

def insertion__sort(a):
    for i in range(1,len(a)):
        tem=a[i]
        j=i-1
        while j>=0 and a[j]>tem:
            a[j+1]=a[j]
            j-=1
        a[j+1]=tem
    return a
a=list(map(int,input().split()))
print(insertion__sort(a))