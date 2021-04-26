def power_of_number(n,x):
    if x==0:
        return 1
    elif x==1:
        return n
    else:
        return n*power_of_number(n,x-1)
n=int(input("enter the number"))
x=int(input("enter the degree of no."))
print(power_of_number(n,x))