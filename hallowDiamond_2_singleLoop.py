N = int(input())
hallow_spaces = 0
total_rows = N * 2
for row in range(total_rows):
    if (row < N):
        row = (N - row)
    else:
        row = (row % N) + 1
    stars = row * "* "
    hallow_spaces = 4 * (N-row)
    line_pattern = stars + (hallow_spaces * " ") + stars
    print (line_pattern)
    
