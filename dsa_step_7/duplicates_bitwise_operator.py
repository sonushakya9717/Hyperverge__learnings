s=input("enter a string")
duplicates_string=""
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if s[i] in duplicates_string:
            break
        elif ord(s[i])^ord(s[j])==0:
            if s[i] not in duplicates_string:
                duplicates_string+=s[i]+" "
                
print(duplicates_string)