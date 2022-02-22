string_a = input()
numbers_list = []
alphabet_list = []
for char in string_a:
    if (char.isdigit()):
        numbers_list.append(char)
    else:
        alphabet_list.append(char)
result_string = "".join(alphabet_list) + "".join(numbers_list)
print (result_string)
