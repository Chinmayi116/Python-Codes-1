def divide(x,y):
    return x/y
try:
    result=divide(10,0)
    print(result)
except ZeroDivisionError:
    print("Error:Cannot divide by zero")