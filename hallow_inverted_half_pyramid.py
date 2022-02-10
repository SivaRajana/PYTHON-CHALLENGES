N = int(input())
for row_number in range(N,0,-1):
    if (row_number == N):
        print ("* " * N)
    elif (row_number == 1):
        print("*")
    else:
        print ("*", end=" ")
        for spaces in range(row_number-2):
            print (" ", end=" ")
        print ("*")
# * * * * * 
# *     *
# *   *
# * *
# *
