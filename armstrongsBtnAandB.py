A = int(input())
B = int(input())
armstrong =""
armstrong_found = False
for number in range(A, B+1):
    cube_digit_sum = 0
    i = number
    length = len(str(number))
    while (i > 9):
        last_digit = i % 10
        cube_digit_sum = cube_digit_sum + (last_digit ** length)
        i = i // 10
    cube_digit_sum = cube_digit_sum + (i ** length )
    if (cube_digit_sum == number):
        armstrong = armstrong + str (number) + " "
        armstrong_found = True
if (armstrong_found):
    print (armstrong)
else:
    print("-1")
