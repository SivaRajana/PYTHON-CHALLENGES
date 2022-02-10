M = int(input())
N = int(input())

biggest = M
if (M < N):
    biggest = N
lcm_not_found = True
while (lcm_not_found):
    if ((biggest % M == 0) and (biggest % N == 0)):
        lcm_not_found = False
    biggest = biggest + 1
print (biggest-1)
