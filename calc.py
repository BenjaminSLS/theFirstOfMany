# User input numbers
n1 = float(input("#1: "))
n2 = float(input("#2: "))

# User input Symbol
symbol = str(input("select symbol: "))

# Calculate result
if symbol == "/":
    print(n1 / n2)
elif symbol == "+":
    print(n1 + n2)
elif symbol == "-":
    print(n1 - n2)
elif symbol == "*":
    print(n1 * n2)
else:
    print("Failure")
