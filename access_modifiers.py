'''
ACCESS MODIFIER OF PYTHON.
We have 3 access modifier on python. We can either set the variable to public or protected or private.
To set the variable public, just declare and initialize the way we normally do.
To set the variable protected, we have to add single underscore before declaring the variable name, ex:. _name, _age
To set the variable private, we have to add double underscore before declaring the variable name, ex: __name, __age. 

IN PYTHON, THESE ARE JUST FOR THE HINT. IF WE WERE USING OTHER LANGUAGE, WE WOULD BE RESTRICTED COMPLETELY. BUT IN PYTHON, EVEN IF THEY ARE
PROTECTED OR PRIVATE, WE WILL BE ABLE TO ACCESS. THEY ARE THERE SO THAT IT WILL ALERT THE DEVELOPERS THAT A PERTICULAR VARIABLE IS PROTECTED OR PRIVATE AND 
SEEING THAT ONE SHOULD WORK ACCORDINGLY.

'''


class Parent:
    apply_leave = False #public variable, anyone can access to this variable
    _office_code = 234 #protected variable, the parent class and the classes derived from the parent can only access this variable
    __no_of_leaves = 15 #private varaible, only Parent class can access this variable
    

class Child(Parent):
    pass

class Stranger(Child):
    pass

father = Parent() #instance of the parent class
son = Child() #instance of the child class
random = Stranger() #instance of the Stranger class

print(father.apply_leave)
print(father._office_code)
print(father._Parent__no_of_leaves) #Concept of name mangling. To access the private variable, we cannot do that directly. We must wirte the 'classname_' 
                                    #before the variable name

# print(dir(Parent)) #doing this we will be able to see the access specifier of every variable declared inside it.

print(son._office_code) #accessing the proetected variable of the parent class.
print(random._Parent__no_of_leaves) #Example of the private variable being accessed by its multilevel inherit class. 