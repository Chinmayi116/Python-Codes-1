class Company:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display_details(self):
        print("Employee Name :", self.name)
        print("Employee ID   :", self.emp_id)
        print("Department    :", self.department)
        print("Salary        :", self.salary)


# Creating objects of the Company class
e1 = Company("Chinmayi", 201, "IT", 45000)
e2 = Company("Rahul", 202, "HR", 38000)

# Calling methods
e1.display_details()
print("------------------")
e2.display_details()
