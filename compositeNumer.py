#Number which got factors more than 2 (1,N) = non prime numbers
N = int(input())
prime = False
for i in range(2, N):
    if (N % i == 0):
        prime = True
print (prime)
