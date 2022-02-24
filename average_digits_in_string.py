string = input()
def average_of_integers(*args):
    sum_of_integers = sum(args)
    avg_of_integers = sum_of_integers / len(args)
    avg_of_integers = round(avg_of_integers, 2)
    print ('{}\n{}'.format(sum_of_integers, avg_of_integers))
  
intergers_from_string = []
for i in string:
    if (i.isdigit()):
        intergers_from_string.append(int(i))

average_of_integers(*intergers_from_string)
