
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

    ### Approch-2 ###
# a=list(map(int,input().split()))
# dict1={}
# for i in a:
#     if i not in dict1:
#         dict1[i]=1
#     else:
#         dict1[i]+=1
# dublicate_no=[]
# for j in dict1:
#     if dict1[j]>1:
#         dublicate_no.append(j)
# if len(dublicate_no)==0:
#     print("No dublicates found")
# else: 
#     print(dublicate_no)

    ### approch-2 ###
# a=list(map(int,input().split()))
# duplicate_no=[]
# for i in range(1,len(a)):
#     if a[i-1] in a[i:]:
#         if a[i-1] not in duplicate_no:
#             duplicate_no.append(a[i-1])
# if len(duplicate_no)==0:
#     print("No duplicates found")
# else
#     print(duplicate_no)