class student:
    roll_no = 1   

    def insert_data(self):
        self.rollno = student.roll_no
        student.roll_no += 1
        self.name = input("Enter your name: ")
        self.marks = int(input("Enter your marks: "))

    def display(self):
        print(self.rollno, self.name, self.marks)


s1 = student()
s1.insert_data()
s1.display()

s2 = student()
s2.insert_data()
s2.display()
