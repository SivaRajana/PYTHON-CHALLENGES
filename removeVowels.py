#should not use lists or regular expressions techniques
sentence = input()
test_sentence = sentence.lower()#convert string to lower case so that no need to check 12 ceses (AEIOU and aeiou)
result_sentence = ""
for i in range(len(sentence)):
    if ((test_sentence[i] != 'a') and (test_sentence[i] != 'e') and (test_sentence[i] != 'i') and (test_sentence[i] != 'o') and (test_sentence[i] != 'u')):
        result_sentence += sentence[i]
print(result_sentence)
