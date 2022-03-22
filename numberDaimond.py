N = int(input())
for i in range(1, (N * 2)):
    string = ""
    if (i < N):
        left_spaces = " " * (N-i)
        number_of_elements = i % N
    else:
        left_spaces = " " * (i-N)
        number_of_elements = N - (i % N)
        
    for j in range(1, number_of_elements + 1):
        string = string + str(j) + " "
    print (left_spaces + string)
# ------------------ METHOD 2 --------------------------------------------
N = int(input())
for i in range(1,N+1):
    print (" " * (N-i), end="")
    for j in range(1, i+1):
        print (j, end=" ")
    print ()

for i in range(N-1, 0, -1):
    print (" " * (N-i), end="")
    for j in range(1, i+1):
        print (j, end=" ")
    print()
    
