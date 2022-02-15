given_sentence = input()
list_of_words = given_sentence.split()
reversed_words_list = []
for i in list_of_words:
    reversed_words_list += [i[::-1]]
print (" ".join(reversed_words_list))
  
