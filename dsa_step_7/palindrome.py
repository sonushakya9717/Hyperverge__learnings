string = "racecar"
reverse_string=""
for i in string:
    reverse_string=i+reverse_string

if reverse_string==string:
    print("Palindrome")
else:
    print('it is not a palindrome')