class AttendenceError(Exception):
    def __init__(self,att):
        self.att=att
att=int(input("Enter your attendence percentage: "))
try:
    if att<75:
        raise AttendenceError(att)
    print("You are eligible for exam")
except AttendenceError:
    print("Error: AttendenceError")
    print("You are not eligible for exam",att)


