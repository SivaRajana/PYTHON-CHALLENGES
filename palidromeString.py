#You are given a string, write a program to find whether the string is palindrome or not.
# Treat uppercase letters and lowercase letters as same when comparing letters. Ignore spaces and quotes within the string.

string = input()
string = string.lower()
modified_string =""
for i in string:
    if (i != " " and i != "'" and i != " \""):
        modified_string = i + modified_string
print (modified_string == modified_string[::-1])

#-------------------------------
# Perfect Method to solve this problem
string = input()
string = string.lower()
modified_string =""
for i in string:
    if (ord(i) >= 65 and ord(i)<=90) or (ord(i)>= 97 and ord(i)<=122):#removing the spaces and special chars
        modified_string = i + modified_string
print (modified_string == modified_string[::-1])
