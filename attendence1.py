class AttendenceError(Exception):
    pass
att=int(input("Enter your attendence percentage: "))
try:
    if att<75:
        raise AttendenceError
    print("You are eligible for exam")
except AttendenceError:
    print("Error: AttendenceError")
    print("You are not eligible for exam")