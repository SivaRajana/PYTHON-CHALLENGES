list_given = list(map(int, input().split()))
# print(list_given)
total_numbers = len(list_given)
result= [list_given[0]]
great = list_given[0]
for i in range(total_numbers):
    for j in range(i, total_numbers):
        if (great < sum(list_given[i:j+1])):
            great = sum(list_given[i:j+1])
            result = (list_given[i:j+1])
                
for i in result:
    print (i,end=" ")
