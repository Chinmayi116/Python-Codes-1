class Company:
    def __init__(self, emp_name, emp_id, designation, monthly_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.designation = designation
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

    def bonus(self):
        return self.monthly_salary * 2   # 2 months bonus

    def display(self):
        print("Employee Name :", self.emp_name)
        print("Employee ID   :", self.emp_id)
        print("Designation   :", self.designation)
        print("Monthly Salary:", self.monthly_salary)
        print("Annual Salary :", self.annual_salary())
        print("Bonus         :", self.bonus())


# Object creation
e1 = Company("Chinmayi", 301, "Software Developer", 40000)
e2 = Company("Amit", 302, "Tester", 32000)

# Method calls
e1.display()
print("---------------------")
e2.display()
