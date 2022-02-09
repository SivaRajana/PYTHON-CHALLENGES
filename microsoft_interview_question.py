#Given a string and N integers, where N is the length of the string, write a program to print the string after 
#shuffling the characters as per the order of the integers given.
# For example, if the given string is "goindc", then read the inputs in the next six lines (length of the string is six). 
# If the given input integers in the next six lines are 5, 1, 4, 2, 3, and 0. By shuffling the word as per the given order
string = input()
new_string = ""
for i in range(len(string)):
    index_input = int(input())
    new_string = new_string + string[index_input]
print(new_string)

