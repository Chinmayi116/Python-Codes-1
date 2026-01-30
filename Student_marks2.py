class InvalidMarksError(Exception):
    def __init__(self, marks):
        self.marks = marks

marks = int(input("Enter marks: "))

try:
    if marks < 0 or marks > 100:
        raise InvalidMarksError(marks)
    print("Marks are valid")
except InvalidMarksError :
    print("Error: Invalid marks entered ", marks)
