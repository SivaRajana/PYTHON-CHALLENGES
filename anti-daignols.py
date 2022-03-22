matrix_size = input().split()
M, N = int(matrix_size[0]), int(matrix_size[1])
def make_int_list(list_a):
    list_to_return = []
    for i in list_a:
        i = int(i)
        list_to_return.append(i)
    return list_to_return
matrix = []
for i in range(M):
    x = input().split(" ")
    x = make_int_list(x)
    matrix.append(x)

diags = []
for i in range(N):
    column = i
    row = 0
    each_diag = []
    while(row < M and column >= 0):
        # print (matrix[row][column])
        each_diag.append(matrix[row][column])
        row = row + 1
        column = column - 1
    diags.append(each_diag)
for j in range(1, M):
    column = N-1
    row = j
    each_diag = []
    while(row < M and column >= 0):
        # print (matrix[row][column])
        each_diag.append(matrix[row][column])
        row = row + 1
        column = column - 1
    diags.append(each_diag)

for i in diags:
    print (*i)

    

