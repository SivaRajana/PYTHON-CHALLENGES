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

#second way of solving it
string1=input()
string2=input()

set_a = set(string1)
set_b = set(string2)

result = sorted(set_a & set_b)
print (*result)
