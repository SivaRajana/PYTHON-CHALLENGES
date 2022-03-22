string_a = input()
string_b = input()
result = "No overlapping"
for i in range(len(string_a), 0, -1):
    string_test = string_a[(-1 * i)::]
    if (string_b.startswith(string_test)):
        result = string_test
        break
print (result)

#complexity decreased
string_a = input()
string_b = input()
result = "No overlapping"
for i in range(len(string_a)):
    string_test = string_a[i::]
    if (string_b.startswith(string_test)):
        result = string_test
        break
print (result)
