marks=int(input("Enter your marks "))
if marks<0 or marks>100:
    raise ValueError("marks must between 0 to 100")
print("Marks is: ",marks)