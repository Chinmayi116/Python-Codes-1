def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Error: Cannot dived by zero")
        return None
result=divide(10,0)
result=divide(10,5)
print(result)