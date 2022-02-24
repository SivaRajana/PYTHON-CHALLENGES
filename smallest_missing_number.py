list_a = input().split(" ")
def numbered_list(list_a):
    new_list = []
    for i in list_a:
        i = int(i)
        new_list.append(i)
    return new_list

list_a = numbered_list(list_a)
max_from_given_numbers = max(list_a)
for i in range(1,max_from_given_numbers+2):
    if (i not in list_a):
        print (i)
        break
