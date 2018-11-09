file = open('kaffka.txt', 'r')
count = ""
line = file.readline()
words = line.split()
for word in words:
    if len(word) > len(count):
        count = word
print(count)
