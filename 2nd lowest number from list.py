arr = [-50,51]

lowest = arr[0]
lowest_2 = None

for i in arr:
    if (i < lowest):
        lowest_2 = lowest
        lowest = i 
    elif (lowest_2 == None or i < lowest_2):
        if (i != lowest):
            lowest_2 = i

print (lowest, lowest_2)
