try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    result=num1/num2
    print("Result",result)
except ValueError:
    print("Error: Please enter a valid numbers and make  sure the second number is not zero")