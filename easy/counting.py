word = input("Enter word:")
vowels = set('aeiouy')
consonant = set('bcdfghjklmnpqrstvxz')
sumV = sum(letter in vowels for letter in word)
sumC = sum(letter in consonant for letter in word)
print('Vowels: {}'.format(sumV))
print('Consonant: {}'.format(sumC))
