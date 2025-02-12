# User input numbers
number_one = input("Insert your first number: ")
number_two = input("Insert your second number: ")

# User input symbol
number_one = float(number_one)
number_two = float(number_two)

symbol = input("What symbol: ")

if symbol == "/":
    print(number_one / number_two)
elif symbol == "-":
    print(number_one - number_two)
elif symbol == "*":
    print(number_one * number_two)
elif symbol == "+":
    print(number_one + number_two)
elif symbol == "**":
    print(number_one ** number_two)
else:
    print("Failure")
