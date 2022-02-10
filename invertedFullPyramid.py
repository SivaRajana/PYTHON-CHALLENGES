N = int(input())
for i in range(N):
    spaces = (" " * i)
    star_pattern = ""
    for j in range(N-i):
        star_pattern = star_pattern + "* "
    print (spaces + star_pattern)
        
        
