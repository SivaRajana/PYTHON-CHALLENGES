words_list = sorted(input().split())
length_of_list = len(words_list)
set_result = set()
for i in range(length_of_list):
    for j in range(i+1, length_of_list):
         set_result.add((words_list[i], words_list[j]))
result = list(set_result)
result.sort()
for i in result:
    print (*i)
