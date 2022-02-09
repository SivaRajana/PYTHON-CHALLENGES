N = int(input())
sum = 0
for i in range(1, N+1):
    is_odd = (i % 2) != 0
    if (is_odd):
        sum += i
print (sum)
        
