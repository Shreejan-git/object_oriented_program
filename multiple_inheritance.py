'''
Details of overriding is in overriding.py
This is just an exapmple of multiple inheritance.
'''

class A:
    #1st parent class
    a_class_var = 4
    
    
class B: #2nd parent class
    b_class_var = 5
    

class C(A,B): #child class inherting from 2 classes.
    '''
    Things to remember:
    1: The python follows the Method Resolution Order (MRO). This concept works Left-to-Right. Following this concept, 
    the class inheriting from 2 classes will consider the left side's parent class first then only right sides'.
    2: In inheritance, while fetching the data from the variable/calling any variable, at first, it will look whether
    or not the variable is there inside itself as an istance variable. If there is not, then it will go it to its parent and 
    check whether its parent has the instance variable. If not, it will return back to its own class and then check whether the 
    called variable is in the form of class variable. If not, it will go its parent and check for the same.
    '''
    c_class_var = 6
    
    

    
    
    

