class Employee:
    '''
    Employee is the class that tracks the details of all the employess of all the departments.
    ''' 
    no_of_leaves = 10
    
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact
        
    @classmethod
    def change_leaves(cls, updated_leaves):
        cls.no_of_leaves = updated_leaves
        
    @staticmethod
    def wish_employee(name):
        print('Hello',name)
    
    def print_details(self):
        print(f'Name of the employee is {self.name}. Age is {self.age} and the contact number is {self.contact}')
        

hr = Employee('Shreejan',55,9324324)
print('before changing the leaves',hr.no_of_leaves)
hr.change_leaves(14)
print('after changning the leaves',hr.no_of_leaves)

class Programmer(Employee):
    '''
    Single inheritance. Inheriting from Employee class. Doing this we can use all the method and variable of the parents class (Employee class)
    '''
    designation = 'software engineer'
    

shreejan = Programmer('Shreejan', 23,432432432)
shreejan.print_details()