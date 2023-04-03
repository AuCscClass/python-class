def calculate(x,y):
    addition = x + y
    print("The addition of x and y is: " , addition)
    subtraction = x - y
    print("The subtraction of x and y is: " , subtraction)
    multiplication = x * y
    print("The multiplication of x and y is: " , multiplication)
    division = x / y
    print("The division of x and y is: " , division)
    mod = x % y
    print("The mod of x and y is: " , mod)
    return addition, subtraction, multiplication, mod

x = int(input("input a value for x: "))
y = int(input("input a value for y: "))
calculate(x,y)