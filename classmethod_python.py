class Mobile:
    camera = 4
    
    def __init__(self,batch_name, version, cost): #initiailzing the constructor
        self.batch_name = batch_name
        self.version = version
        self.cost = cost
    
    @classmethod
    def customize_camera_num(cls, no_of_camera):
        '''using decorator @classmethod to make the method a class method. This method can be used to modify the class variable.
        It does not take self, instead takes cls.
        '''
        cls.camera = no_of_camera #changing the class variable

    def print_details(self):
        print(f'The batch name is {self.batch_name} and its version is {self.version}. It cost {self.cost}')
        
        
samsung = Mobile('s-series','s10', 1000)
print('accessing the class variable value before changing through class method:',samsung.camera)

samsung.customize_camera_num(5) #changing the class variable through the instance of the class.
samsung.print_details()
print('accessing the class variable value after changing through class method:',samsung.camera)
        