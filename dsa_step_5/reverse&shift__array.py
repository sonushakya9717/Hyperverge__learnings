############ Reverse an array and shiftng that arary by gven no. ############


############ for left shft ########

# a= list(map(int,input().split()))
# m=int(input())
# length=len(a)//2
# for i in range(length):
#     a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
# for j in range(m):
#     tem=a[0]
#     for i in range(len(a)-1):
#         a[i]=a[i+1]
#     a[-1]=tem


###### for rght shft ######

# a= list(map(int,input().split()))
# m=int(input())
# length=len(a)//2
# for i in range(length):
#     a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
# for j in range(m):
#     tem=a[-1]
#     for i in range(len(a)-1,0,-1):
#         a[i]=a[i-1]
#     a[0]=tem
# print(a)


#### Approch-2
# a= list(map(int,input().split()))
# m=int(input())
# Reverse__key=m%len(a)
# length=len(a)//2
# for i in range(length):
#     a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
# print(a[Reverse__key:]+a[:Reverse__key])

