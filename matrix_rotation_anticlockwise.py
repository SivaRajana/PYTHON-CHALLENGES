matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
          

rotated_matrix = []
for i in range(len(matrix[0])):
  temp_list = []
  for j in range(len(matrix)):
    temp_list.append(matrix[j][i])
  rotated_matrix.append(temp_list)

rotated_matrix.reverse()

for row in matrix:
  print (*row)

for row in rotated_matrix:
  print (*row)
