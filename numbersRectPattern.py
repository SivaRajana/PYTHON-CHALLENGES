# 1 2 3 
# 4 5 6 
rows = int(input())
cols = int(input())
number = 0
for i in range(rows):
    string_to_print = ""
    for j in range(cols):
        number = number + 1
        string_to_print = string_to_print + str (number) + " "
    print (string_to_print)
