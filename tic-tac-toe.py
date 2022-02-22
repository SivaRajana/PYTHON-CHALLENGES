input_matrix = []
for i in range(3):
    line = input().split(" ")
    input_matrix.append(line)
def row_winner_check(row):
    set_a = set(row)
    if (len(set_a) == 1):
        if (row[0] == 'O'):
            # print ("Abhinav Wins")
            return "Abhinav Wins"
        elif(row[0] == 'X'):
            # print ("Anjali Wins")
            return "Anjali Wins"
    else:
        return 'Tie'
x = "Tie"
for line in range(3):
    if (line <= 1):
        x = row_winner_check(input_matrix[line])
        if (x != 'Tie'):
                break
        # print ("1", x)
    elif (line == 2 and x == 'Tie'):
        for i in range(3):
            if (i == 0):
                anti_diganol = input_matrix[0][2] + input_matrix[1][1] + input_matrix[2][0]
                x = row_winner_check(anti_diganol)
                # print (x)
                if (x != 'Tie'):
                    break
                column = input_matrix[0][0] + input_matrix[1][0] + input_matrix[2][0]
                x = row_winner_check(column)
                if (x != 'Tie'):
                    break
            elif(i==1):
                column = input_matrix[0][i] + input_matrix[1][i] + input_matrix[2][i]
                x = row_winner_check(column)
                # print (x)
                if (x != 'Tie'):
                    break
            else:
                diganol = input_matrix[0][0] + input_matrix[1][1] + input_matrix[2][2]
                x = row_winner_check(diganol)
                if (x != 'Tie'):
                    break
                # print (x)
                column = input_matrix[0][i] + input_matrix[1][i] + input_matrix[2][i]
                x = row_winner_check(column)
                # print (x)
                if (x != 'Tie'):
                    break
                x = row_winner_check(input_matrix[line])
                if (x != 'Tie'):
                    break
print (x)
        
        
        
        
        
        
            
