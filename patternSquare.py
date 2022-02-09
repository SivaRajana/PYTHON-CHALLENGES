# +----------+
# |          |
# |          |
# |          |
# +----------+

rows = int(input())
cols = int(input())
print ("+" + ("-" * cols) + "+")
for i in range(1, rows+1):
    print ("|" + (" " * cols) + "|")
print ("+" + ("-" * cols) + "+")
