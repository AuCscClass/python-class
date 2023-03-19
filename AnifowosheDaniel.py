"""
Anifowoshe Daniel 20/1011
"""

def operation(x, y):
    dict = {
        'Sum': x + y,
        'Multiplication': x*y,
        'Division': x/y,
        'Subtraction': x-y,
        'Modulus': x%y
    }
    return dict


print(operation(20,4))
