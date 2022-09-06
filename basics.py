class Mobile: #defining the class
    receive_calls = True #class variable
    camera = 3 #class variable

samsung = Mobile() #instance of the class
iphone = Mobile() #instance of the class

samsung.version = 'galaxy' #version is instance variable
iphone.version = 'iphone2' #version is instance variable
iphone.cost = 24342
samsung.cost = 34234


#we cannot change the value of the class variable from instanc of the class
print('before changing',Mobile.receive_calls)
samsung.receive_calls = False
print('after changing',Mobile.receive_calls)
print('From instance',samsung.receive_calls)


samsung.camera = 5
print(samsung.camera)
samsung.camera = 4
print(samsung.camera)
print(Mobile.camera) #class variable remains the same.
Mobile.camera = 2
print(Mobile.camera) #only class can change the class variable