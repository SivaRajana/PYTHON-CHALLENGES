starting_number = int(input())
rows = int(input())
for i in range(rows):
    line = ""
    for j in range(i+1):
        line = line + str (starting_number) + " "
        starting_number = starting_number + 1
    print (line)
    
