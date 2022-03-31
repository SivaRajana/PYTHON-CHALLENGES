list_a = [-50,50,-50,-50]

big = list_a[0]
second_big = None

for number in list_a:
    if (big < number):
        second_big = big
        big = number
    elif (second_big == None or second_big < number):
        if (number != big):
            second_big = number
    
print (big, second_big)
