#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

N = int(input())
for i in range(1, (N * 2)):
    if (i <= N):
        print (" " * (N-i) + "* " * i)
    else:
        print ( (" " * (i-N)) + ("* " * ((2*N)-i)) )
