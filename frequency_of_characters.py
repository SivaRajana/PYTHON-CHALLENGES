input_string = input()
input_string = input_string.lower()
list_a = list(input_string)
set_a = set(list_a)
set_a.discard(" ")
list_unique_alphabets = sorted(set_a)
for item in list_unique_alphabets:
    print ("{}: {}".format(item,list_a.count(item)))
    
#----------------------------------------------------------    
string = input()
dict_a = {}
for char in string:
    if char not in dict_a:
        dict_a[char] = 1
        continue
    dict_a[char] += 1
del dict_a[" "]
for key in sorted(dict_a):
    print (key, "---", dict_a[key])
    
