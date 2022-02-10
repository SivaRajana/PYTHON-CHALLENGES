#Number of triplets that can be formed with the numbers below N
N = int(input())
triplet_count = 0
for a in range(2, N+1):
    for b in range (a+1, N+1):
        for c in range(b+1,N+1):
            triplet_condition = ((a * a) + (b * b) == (c * c))
            if (triplet_condition):
                triplet_count = triplet_count + 1
print (triplet_count)
