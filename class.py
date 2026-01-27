class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks
s1 = Student("Chinmayi", 90)
print(s1.get_marks())   # 90
s1.set_marks(95)
print(s1.get_marks())   # 95
