try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    result=num1/num2
    print("Result",result)
except ValueError:
    print("Error: Please Enter a valid integer")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except Exception as e:
    print("An error occured",e)