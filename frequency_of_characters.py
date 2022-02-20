input_string = input()
input_string = input_string.lower()
list_a = list(input_string)
set_a = set(list_a)
set_a.discard(" ")
list_unique_alphabets = sorted(set_a)
for item in list_unique_alphabets:
    print ("{}: {}".format(item,list_a.count(item)))
