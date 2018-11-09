first = input("enter first word:")
second = input("enter second word:")
w1 = len(first)
w2 = len(second)
alike = 0.0
for i in first:
    if i in second:
        alike +=1
print(alike / (w1 + w2 - alike))
