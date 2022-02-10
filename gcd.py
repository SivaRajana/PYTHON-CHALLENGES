M = int(input())
N = int(input())
smallest = M
if (M > N):
    smallest = N
gcd = 1
for i in range(2, smallest+1):
    if (M % i == 0) and (N % i == 0) :
        gcd = i
print (gcd)
