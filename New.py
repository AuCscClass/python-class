def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y
def mul(x,y):
    return x*y
def mod(x,y):
    return x%y
x=int(input("Enter the First value\n"))
y=int(input("Enter the Second value\n"))
print("The addition of " + str(x) + " and "+ str(y) + " is: ",add(x,y))
print("The Subraction of " + str(x) + " and "+ str(y) + "is: ",sub(x,y))
print("The Division of " + str(x) + " and "+ str(y) + " is: ",div(x,y))
print("The Multiplication of " + str(x) + " and "+ str(y) + " result is: ",mul(x,y))
print("The Modulus of " + str(x) +  " and "+ str(y) + " is: ",mod(x,y))