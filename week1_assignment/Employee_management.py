class Employee:
    def __init__(self, emp_id, name, salary):
        self.__employee_id = emp_id
        self.__name = name
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_employee_id(self, emp_id):
        self.__employee_id = emp_id

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary

    def display_info(self):
        print(f"Employee ID: {self.__employee_id}")
        print(f"Name: {self.__name}")
        print(f"Salary: ₹{self.__salary}")
        print("-" * 30)

    def give_hike(self, percent):
        if percent > 0:
            hike_amount = self.__salary * (percent / 100)
            self.__salary += hike_amount
            print(f"{self.__name} got a hike of {percent}% (₹{hike_amount:.2f})")

employees = []

n = int(input("How many employees you want to enter? "))
for i in range(n):
    print(f"\nEnter details for Employee {i+1}:")
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    salary = float(input("Salary: "))
    emp = Employee(emp_id, name, salary)
    employees.append(emp)

print("\nInitial Employee Information:")
for emp in employees:
    emp.display_info()

for emp in employees:
    percent = float(input(f"Enter hike percentage for {emp.get_name()}: "))
    emp.give_hike(percent)

print("\nUpdated Employee Information After Salary Hikes:")
for emp in employees:
    emp.display_info()
