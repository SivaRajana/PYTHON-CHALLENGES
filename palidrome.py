#using string slicing
given_string = input()
given_string = given_string.lower()
reversed_string = given_string[::-1]
print (given_string == reversed_string)


#method 2 using loops and trick here is add character from given string first and then add the new string that is getting formed
given_string = input()
given_string = given_string.lower()
reversed_string = ""
for i in given_string:
    reversed_string = i + reversed_string
print (given_string == reversed_string)

#method 3
given_string = input()
given_string = given_string.lower()
reversed_string = ""
for i in range(len(given_string)):
    reversed_string = reversed_string + given_string[len(given_string)-i-1]
print (given_string == reversed_string)

