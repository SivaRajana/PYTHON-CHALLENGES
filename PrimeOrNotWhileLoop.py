#finding the whether the given number is prime number or not with the help of While loop
N = int(input())
flag = 0
i=2
while (i < N):
    if (N % i == 0):
        flag = 1
        break
    i += 1
if (flag == 0):
    print ("Y")
else:
    print ("N")
