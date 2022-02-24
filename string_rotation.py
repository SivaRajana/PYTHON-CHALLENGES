def right_rotate(string):
    string_a = string[-1]+string[0:-1]
    return (string_a)
    
S1 = input()
S2 = input()

not_matched = True
rotated_string = S1
for i in range(len(S1)):
    if (rotated_string == S2):
        print (i)
        not_matched = False
        break
    rotated_string =  right_rotate(rotated_string)
    # print (rotated_string, S2)
if(not_matched):
    print ("No Match")
