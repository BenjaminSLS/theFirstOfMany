# Get input
numberOne = input("Number 1: ")
numberTwo = input("Number 2: ")

# Swap input to an integer
n1 = int(numberOne)
n2 = int(numberTwo)

# Choose symbol
print("Choose your symbol: (1) (2) (3)")
symbolInput = input()
symbol = int(symbolInput)

# Final math
if symbol == 1:
    finalNumber = n1 + n2
    print("Answer: " + str(finalNumber))
elif symbol == 2:
    finalNumber = n1 - n2
    print("Answer: " + str(finalNumber))
elif symbol == 3:
    finalNumber = n1 * n2
    print("Answer: " + str(finalNumber))
else:
    print("Failure!")