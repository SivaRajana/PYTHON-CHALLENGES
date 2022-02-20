def make_intergered_list (list_given):
    new_list = []
    for i in list_given:
        new_list.append(int(i))
    return new_list

N = int(input())

max_numbers_container = []
for i in range(N):
    list_input = input().split(" ")
    list_input = make_intergered_list(list_input)
    max_from_list = max(list_input)
    max_numbers_container.append(max_from_list)

print (max_numbers_container) 
