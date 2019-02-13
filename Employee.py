class Employee:
    'Common base class for all employees'
    count = 0
    age = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def displayCount(self):
        print ("Total Employees: %d" % self.count)

    def displayEmployee(self):
        print ("Name: ", self.name, " Salary: ", self.salary, " Age: ", self.age)


if __name__ == '__main__':
    employee = Employee('Yousaf', 50000)
    employee.displayCount()
    employee.displayEmployee()

    employee.age = 7;
    employee.displayEmployee()