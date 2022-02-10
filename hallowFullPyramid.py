N = int(input())
#with using only single loop
for row_number in range(1, N):
    print (" " * (N - row_number), end="")
    print ("*", end =" ")
    print ("  " * (row_number-2), end="")
    if (row_number > 1):
        print ("*")
    else:
        print ("")
print ("* " * N)

#with NestedLoops
