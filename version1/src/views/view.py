

class ViewMain: pass 

class ViewPick:
    def __init__(self):
        self.choice = 0 
        
        
    def choice_mode(self): 
        print("""
            Mode 1: email:password
            Mode 2: email       
        """)
        self.choice =  input('Veuillez choisir un mode: ') # FIXME verifier si c'est un nombre 
        

class ViewGoogleDork: 
    def __init__(self):
        pass
    
    def pivot(self): 
        print('Les identifiant on pivoter')
        