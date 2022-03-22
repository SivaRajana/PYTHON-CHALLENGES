N = int(input())
for i in range(N):
    spaces = " " * i
    pattern = ""
    for j in range(N-i):
        pattern = pattern + str(j+1) + " "
    print (spaces + pattern)

#METHOD 2
N = int(input())
for row in range(N,0,-1):
    print (" " * (N-row), end="")
    for col in range(1, row+1):
        print (col, end=" ")
    print ()
