first = int(input("Enter first number:"))
second = int(input("Enter second number:"))
operation = input("Enter operator:")
if operation == '+':
    print(first+second)
elif operation == '-':
    print(first-second)
elif operation == '*':
    print(first*second)
elif operation == '/':
    print(first/second)
else:
    print("Wrong operator! try again")

