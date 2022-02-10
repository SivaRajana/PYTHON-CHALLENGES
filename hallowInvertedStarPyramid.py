N = int(input())
i = N
while (i > 0):
    spaces = " " * (N-i)
    if (i == 1) or (i == N):
        start = "* " * i
        print (spaces + start)    
    else:
        hallow_spaces = "  " * (i-2)
        print (spaces + "* " + hallow_spaces + "*")
    i = i-1
