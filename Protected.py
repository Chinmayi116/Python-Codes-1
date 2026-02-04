class Student:
    def _show(self):
        print("This is a protected method")

class BCAStudent(Student):
    def call(self):
        self._show()   # ✔ Allowed

b = BCAStudent()
b.call()
