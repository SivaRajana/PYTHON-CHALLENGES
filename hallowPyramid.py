N = int(input())
for row_number in range(1,N+1):
    if (row_number == 1):
        print ("* ")
    elif (row_number == N):
        print ("* " * N)
    else:
        print ("*", end =" ")
        for j in range(row_number-2):#eliminate first start and last star
            print (" ", end=" ")
        print ("*")
# * 
# * *
# *   *
# *     *
# * * * * * 
