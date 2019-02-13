from Employee import Employee

# Main function
if __name__ == '__main__':
    employee = Employee('Yousaf', 50000)
    employee.displayCount()
    employee.displayEmployee()

    # Gettter and setters'
    employee.__setattr__('age', 10)
    print ('Employee age: ', employee.__getattribute__('age'))

    # Check if an attribute exists or not
    hasattr(employee, 'data')

    if Employee.__name__ == 'Employee':
        print('\n')
        print(Employee.__doc__)
        print(Employee.__dict__)