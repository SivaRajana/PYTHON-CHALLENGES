M = int(input())
N = int(input())
for i in range(M):
    if (i == 0) or (i == (M-1)):
        print ("* " * N)
    else:
        print ("* " + "  " * (N-2) + "* ")
