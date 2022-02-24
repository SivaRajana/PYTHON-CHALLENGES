given_string__ = input()
given_string_list = given_string__.split()

# print (given_string)
intergers_container = []
for given_string in given_string_list:
    i = 0
    number = 0
    for each_letter in given_string:
        if each_letter.isdigit():
            if (i < len(given_string)-1):
                if(given_string[i+1].isdigit()):
                    number = number * 10 + (int(each_letter))
                else:
                    number = number * 10 + (int(each_letter))
                    intergers_container.append(number)
                    number = 0
            else:
                number = number * 10 + (int(each_letter))
                intergers_container.append(number)
        i += 1
# print (intergers_container)
    


if (len(intergers_container)> 0):
    sum_result = sum(intergers_container)
    avg = sum_result / len(intergers_container)
    avg_result = round (avg, 2)
    print ("{}\n{}".format(sum_result, avg_result))
    
