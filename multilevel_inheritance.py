'''
Example of multilevel inheritance. 

We have to be aware about overriding the variable or method of the super class.

Details in overriding.py

'''
class Dad:
    basketball_player = True #class variable 

class Son(Dad):
    cricket_player = False
    football_player = True

class Grandson(Son):
    basketball_player = False #class variable of Grandson but this has override the class variable of Dad class.
    football_player = False #class vairable     
    hockey_player = True
    

father = Dad()
son = Son()
naati = Grandson()

print(naati.basketball_player)    


    
    
    