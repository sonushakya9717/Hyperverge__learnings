
################# Bineary search ###############

# a=[7,6,5,4,3,2,1]
# l=0
# r=len(a)-1
# element=int(input())

# def Bineary_search(a,l,r,element):
#     if l>r:
#         return "Not Found"
#     else:
#         mid=(l+r)//2
#         if a[mid]==element:
#             return mid
#         elif a[mid]>element:
#             r=mid-1
#             return Bineary_search(a,l,r,element)
#         else:
#             l=mid+1
#             return Bineary_search(a,l,r,element)
# print(Bineary_search(a,l,r,element))


#####  bineary search for sorted list in a reverse order #####

# def Bineary_search(a,l,r,element):
#     if l>r:
#         return "Not Found"
#     else:
#         mid=(l+r)//2
#         if a[mid]==element:
#             return mid
#         elif a[mid]>element:
#             l=mid+1
#             return Bineary_search(a,l,r,element)
#         else:
#             r=mid-1
#             return Bineary_search(a,l,r,element)
# print(Bineary_search(a,l,r,element))