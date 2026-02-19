class EmployeeManager:

    def __init__(self):
        # Dictionary inside class
        self.employees = {}

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = int(input("Enter Salary: "))

        self.employees[emp_id] = {
            "Name": name,
            "Salary": salary
        }

        print("Employee added successfully!\n")

    def view_employees(self):
        if not self.employees:
            print("No employees found.\n")
            return

        print("\n--- Employee List ---")
        for emp_id, details in self.employees.items():
            print("ID:", emp_id)
            print("Name:", details["Name"])
            print("Salary:", details["Salary"])
            print("--------------------")

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")

        if emp_id in self.employees:
            details = self.employees[emp_id]
            print("\nEmployee Found")
            print("Name:", details["Name"])
            print("Salary:", details["Salary"])
        else:
            print("Employee not found.\n")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")

        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee deleted successfully.\n")
        else:
            print("Employee not found.\n")


# Main Program
manager = EmployeeManager()

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_employee()
    elif choice == "2":
        manager.view_employees()
    elif choice == "3":
        manager.search_employee()
    elif choice == "4":
        manager.delete_employee()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
