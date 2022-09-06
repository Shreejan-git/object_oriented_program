class Mobile:
    camera = 4 #class variable
    
    def __init__(self, batch_name, version, cost): #constructor
        self.batch_name = batch_name
        self.version = version
        self.cost = cost 
    
    @classmethod
    def customize_camera_num(cls, new_num): #class method
        cls.camera = new_num
        
    def print_details(self):
        print(f'The batch name is {self.batch_name} and its version is {self.version} and it costs {self.cost}')
        
    @staticmethod
    def wish_the_user(username):
        '''
        Using the decorator @staticmethod. This method does not take self or cls. Its a plain method and is used when 
        we have to display some information or messages.
        '''
        print('Hello',username)
        

samsung = Mobile('abc','s-series', 1324)
samsung.wish_the_user('Shreejan')