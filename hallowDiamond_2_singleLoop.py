N = int(input())
hallow_spaces = 0
total_rows = N * 2
for row in range(total_rows):
    if (row < N):
        row = (N - row)
    else:
        row = (row % N) + 1 # this step avoid creating chaos of when 10%2 ==  0 like that, if we iterate from 0 to 2*n, then 10 won't come into picture.
    stars = row * "* "
    hallow_spaces = 4 * (N-row)
    line_pattern = stars + (hallow_spaces * " ") + stars
    print (line_pattern)
    
