def f(i):
    if i <= 1:
        return i
    x = 0
    y = 1
    z = 1
    for n in range(2, i + 1):
        z = x + y
        x = y
        y = z
    return z
n = int(input())
print(f(n))

#...................................

def fabonocci(n):
    if (n <= 1):
        return n
    else:
        return fabonocci(n-1)+fabonocci(n-2)

n = int(input())
print (fabonocci(n))

#solved it while solving hackerrank challenges
