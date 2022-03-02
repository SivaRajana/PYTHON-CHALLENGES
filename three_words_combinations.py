words_list = sorted(input().split())
length = len(words_list)
result = set()
if (length <= 3):
    print (*words_list)
else:
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                result.add((words_list[i],words_list[j],words_list[k]))
result_list = list(result)
result_list.sort()
for each_combo in result_list:
    print (*each_combo)
