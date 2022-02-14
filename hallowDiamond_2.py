N = int(input())
hallow_spaces = 0
for row in range(N,0,-1):
    stars = row * "* "
    line_pattern = stars + (hallow_spaces * " ") + stars
    print (line_pattern)
    hallow_spaces = hallow_spaces + 4 
for row in range(1, N + 1):
    hallow_spaces = hallow_spaces - 4 
    stars = row * "* "
    line_pattern = stars + (hallow_spaces * " ") + stars
    print (line_pattern)
    
# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * * 
# * *             * * 
# *                 * 
# *                 * 
# * *             * * 
# * * *         * * * 
# * * * *     * * * * 
# * * * * * * * * * * 
