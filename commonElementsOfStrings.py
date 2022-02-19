list_a = input().split(",")
list_b = input().split(",")
set_a = set(list_a)
set_b = set(list_b)
result_set = set_a & set_b
list_final = []
for i in result_set:
    list_final.append(int(i))
list_final.sort()
print (list_final)
