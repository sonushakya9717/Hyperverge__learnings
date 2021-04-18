string1="night"
string2="thing"

string1_letter={}
string2_letter={}
if len(string1)==len(string2):
    for i in range(len(string1)):
        if string1[i] not in string1_letter:
            string1_letter[string1[i]]=1
        else:
            string1_letter[string1[i]]+=1
        if string2[i] not in string2_letter:
            string2_letter[string2[i]]=1
        else:
            string2_letter[string2[i]]+=1
    if string1_letter==string2_letter:
        print("Anagram")
    else:
        print("Not a anagram")
else:
    print("Not a anagram")
