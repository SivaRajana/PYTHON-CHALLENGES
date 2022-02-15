abbreviation = input()
words_of_abbreviation = abbreviation.split()
acronym = []
for word in words_of_abbreviation:
    acronym += [word[0]] 
print (".".join(acronym))
