class InvaildMarksError(Exception):
    pass
marks=int(input("Enter a marks: "))
try:
    if marks<0 or marks>100:
        raise InvaildMarksError
    print("Marks is vaild")
except InvaildMarksError:
    print("Error: InvaildMarksError")