# def fabonacci(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return fabonacci(n-1)+fabonacci(n-2)
# n=int(input('enter the no'))
# for i in range(1,n+1):
#     print(fabonacci(i))







# memo={}
# def fabonacci(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     if n in memo:
#         return memo[n]
#     else:
#         num=fabonacci(n-1)+fabonacci(n-2)
#         memo[n]=num
#         return num
# n=int(input('enter the no'))
# for i in range(1,n+1):
#     print(fabonacci(i)) 




