# 24 
# 23 22 
# 21 20 19 
# 18 17 16 15 
# 14 13 12 11 10 when startingNumber=10 and Rows = 5

K = int(input())
rows = int(input())
elements_count = 0
i = 0
#first count the elements which required to build triangle
while (i < rows):
    elements_count = elements_count + (i + 1)
    i = i + 1
starting_number = K + elements_count#add total elements_count to the starting number
starting_number = starting_number -1 # to include the entered starting_number at the end
for i in range(1, rows + 1):
    line_pattern = ""
    for j in range(1, i+1):
        line_pattern = line_pattern + str(starting_number) + " "
        starting_number = starting_number -1
    print (line_pattern)

