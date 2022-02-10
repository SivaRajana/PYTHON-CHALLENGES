N = int(input())
for i in range(N):
    spaces = " " * i
    pattern = ""
    for j in range(N-i):
        pattern = pattern + str(j+1) + " "
    print (spaces + pattern)
