
############ Finding Duplicates in a Sorted Array ############
# a=[3,4,5,6,7,7,8,8,9]
# duplicates=[]
# c=a[0]
# for i in range(1,len(a)):
#     if c==a[i]:
#         duplicates.append(a[i])
#     else:
#         c=a[i]
# print(duplicates)


########## Finding Duplicates in a Unsorted Array ##############

    ### Approch-1 ###
# a=list(map(int,input().split()))
# dict1={}
# for i in a:
#     if i not in dict1:
#         dict1[i]=1
    #     else:
    #         dict1[i]+=1
# duplicate_no=[]
# for j in dict1:
#     if dict1[j]>1:
#         duplicate_no.append(j)
# if len(duplicate_no)==0:
#     print("No duplicates found")
# else: 
#     print(duplicate_no)

    ### approch-2 ###
a=list(map(int,input().split()))
duplicate_no=[]
for i in range(len(a)-1):
    if a[i] in a[i+1:] and a[i] not in duplicate_no:
            duplicate_no.append(a[i])
if len(duplicate_no)==0:
    print("No duplicates found")
else:
    print(duplicate_no)