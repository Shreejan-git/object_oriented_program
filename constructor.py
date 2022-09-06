class Mobile:
    camera = 4 #class variable
    
    #self keyword is must. This carries the information about the instance we are calling
    
    def __init__(self,batch_name, version, cost): #constructor and class's parameters. Constructor is also initialized first.
        self.batch_name  = batch_name 
        self.version = version
        self.cost = cost
        
    def print_details(self):
        print(f' The batch_name is {self.batch_name} and its version is {self.version} and its cost is {self.cost}')
        
Samsung = Mobile('series A', '1',2342)
print(Samsung.camera)
print(Samsung.batch_name)
Samsung.print_details()

