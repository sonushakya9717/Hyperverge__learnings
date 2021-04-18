A = [1,5,4,6,9]

max=A[0]
min=A[0]
for i in range(len(A)):
    if max<A[i]:
        max=A[i]
    if min>A[i]:
        min=A[i]
print("maximum :",max," minimum is :",min)

