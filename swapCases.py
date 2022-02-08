#method 1
word = input()
modified = ""
for i in word:
    if(i == i.lower()):
        modified += i.upper()
    else:
        modified += i.lower()
print(modified)

#method 2
word = input()
for i in word:
    if(i == i.lower()):
        print(i.upper(), end="")
    else:
        print(i.lower(),end="")
