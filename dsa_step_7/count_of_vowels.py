string="FriEnds"
string=string.lower()
vowels="aeiou"
count_of_vowels=0
count_of_consonants=0
for i in string:
    if i in vowels:
        count_of_vowels+=1
    else:
        count_of_consonants+=1

print("Consonants :-",count_of_consonants)
print("Vowels :-",count_of_vowels)
