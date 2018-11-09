from collections import Counter
file = open('lorem.txt', 'r')
line = file.readline().lower()
words = line.split()
counter = Counter(words)
print(counter)



