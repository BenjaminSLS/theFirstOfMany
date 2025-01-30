number01 = int(input("Number 01: "))

if number01 <= 10 and number01 >= 0:
    print(number01)
    if number01 == 7:
        print("Found lucky number 7.")
    else:
        print("Missed the lucky number.")
else:
    print("Not within range. Your number is", str(number01) + ".")