def get_transpose_of_matrix(matrix, m, n):
    transpose_matrix = []
    for col_index in range(n):
        each_row = []
        for row_index in range(m):
            each_row.append(matrix[row_index][col_index])
        transpose_matrix.append(each_row)
    return transpose_matrix
    
def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

# Call the get_transpose_of_matrix function
matrix = get_transpose_of_matrix(num_list, m, n)
for each_row in matrix:
    print (each_row)
