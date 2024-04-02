def calculate(a, b):
    sum = a + b
    diff = a - b
    mod = a % b
    div = a / b
    prod = a * b
    print(f"""
The sum is: {sum}
The difference is: {diff}
The division is: {div}
The modulus is: {mod}
The product is: {prod}
    """)
    
    
    
    
a = int(input("enter first value: "))
b = int(input("enter seond value: "))

calculate(a, b)
