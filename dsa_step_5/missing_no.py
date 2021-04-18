 ##### Finding multiple missing elements in a list #####
 
 ### Approch 2 ####
# a=[1,6,3,4,5,7,8,9]
# length=len(a)+1
# i=1
# while i<length:
#     if i not in a:
#         print(i)
#     i+=1


##### Approch - 2 #####

# a=[1,4,5,2,3]
# sum1=sum(a)
# total_ele=len(a)+1
# total_sum=total_ele//2*(2+total_ele-1)
# missing__no=total_sum-sum1
# print(missing__no)