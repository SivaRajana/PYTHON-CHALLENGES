N = int(input())
dict_a = {}
for i in range(N):
    x,y = list(map(int, input().split()))
    dict_a[x] = y
# print (dict_a)
def get_term(i):
    if (dict_a[i] == 0):
        return ""
    elif (dict_a[i] == 1):
        return (" + " + "x^" + str(i) )
    elif (dict_a[i] < 0):
        if (dict_a[i] == -1):
            return (" - " + "x^" + str(i) )
        return (" - " + str(dict_a[i] * -1) + "x^" + str(i) )
    return (" + " + str(dict_a[i]) + "x^" + str(i) )
        
string = ""
for i in range(N-1, -1, -1):
    if (i == N-1):
        string = string + str(dict_a[i]) + "x^" + str(i)
    elif (i == 1):
        if (dict_a[i] == 0):
            continue
        elif(dict_a[i] < 0):
            string += " - " + str(dict_a[i] * -1)+"x"
        else:
            string += " + " + str(dict_a[i])+"x" 
    elif (i == 0):
        if (dict_a[i]==0):
            string += " + " + str(0)
        elif(dict_a[i] > 0):
            string += " + " + str(dict_a[i])
        else:
            string += " - " + str(dict_a[i] * -1)
    else:
        string += get_term(i)
            
print (string)  
    
    
    
