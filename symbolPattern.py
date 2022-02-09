# + + + + + + + 
# - - - - - - - 
# + + + + + + + 
# - - - - - - - 
# + + + + + + + 

M = int(input())
N = int(input())
for i in range(1, M+1):
    if (i % 2 != 0):
        print ("+ " * N)
    else:
        print ("- " * N)
        
