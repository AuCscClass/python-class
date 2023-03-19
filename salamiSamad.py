def argsas(a, b):
    print("which operator do you want: ")
    operator = input().lower()
    if operator == "addition":
        print(a + b)
    elif operator == "subtraction":
        print(a - b)
    elif operator == "division":
        print(a / b)
    elif operator == "multiplication":
        print(a * b)
    elif operator == "modulus":
        print(a % b)
    else:
        print("this is not a valid input you have, addition, subtraction, division, multiplication and modulus ")


argsas(10, 3)

