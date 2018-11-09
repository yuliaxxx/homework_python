import random, math
i = 1
array = []
for i in range(10):
    array.append(random.uniform(-100.0, 100.0))
print(sorted(array, key=lambda  array: abs(math.modf(array)[0])))

