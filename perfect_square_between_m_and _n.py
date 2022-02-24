def is_perfect_square(number):
    root_value = int(number ** 0.5)
    if (root_value ** 2 == number):
        return True
    return False
    
M = int(input())
N = int(input())

not_found_perfect_square = True
for i in range(M, N+1):
    is_perfect_sq = is_perfect_square(i)
    if (is_perfect_sq):
        print (i)
        not_found_perfect_square = False
        break
if(not_found_perfect_square):
    print ("No Perfect Square")
