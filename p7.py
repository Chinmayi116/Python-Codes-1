class Student:
    roll_no=1
    def __init__(self,name,marks):
        Student.roll_no=self.roll_no
        self.roll_no=self.roll_no+1
        self.name=name
        self.marks=marks
    def cal(self):
        if self.marks>=150:
            print("you pass the exam")
        else:
            print("Fail")
    def display(self):
        print(self.roll_no, self.name, self.marks)
d1=Student("chinmayi",180)
d2=Student("Megha",150)
d3=Student("Poornima",140)
d1.display()
d1.cal()
d2.display()
d2.cal()
d3.display()
d3.cal()