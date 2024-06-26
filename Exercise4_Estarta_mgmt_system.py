class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.name}, a {self.age} years old with a salary of {self.salary}"

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def __str__(self):
        return f"{super().__str__()} Manager in the {self.department} department"

class Developer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def __str__(self):
        return f"{super().__str__()} Developer in {self.programming_language}"

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for employee in self.employees:
            print(employee)

    def calculate_total_salary(self):
        return sum(employee.salary for employee in self.employees)

def main():
    company = Company()
    print("Welcome to Estarta Solutions Employee Management System\n")
    
    while True:
        print("\nWhat task would you like to perform?")
        print("1. Add a new employee")
        print("2. Display employees")
        print("3. Calculate total salary")
        print("4. Exit\n")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            employee_type = input("\nEnter employee type (Manager/Developer): ")
            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            salary = float(input("Enter employee salary: "))
            
            if employee_type.lower() == 'manager':
                department = input("Enter employee department: ")
                company.add_employee(Manager(name, age, salary, department))
            elif employee_type.lower() == 'developer':
                programming_language = input("Enter employee programming language: ")
                company.add_employee(Developer(name, age, salary, programming_language))
            else:
                print("Invalid employee type. Please enter either 'Manager' or 'Developer'.")
                continue

            print("\nEmployee added successfully!")

        elif choice == '2':
            print()
            company.display_employees()

        elif choice == '3':
            total_salary = company.calculate_total_salary()
            print(f"\nTotal salary of all employees is {total_salary}")

        elif choice == '4':
            print("\nThank you for using Estarta Solutions Employee Management System.")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()