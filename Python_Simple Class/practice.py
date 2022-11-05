class Man:
    def __init__(self,name):
        self.name = name
        print('----- Initialized -----')
        
    def hello(self):
        print("Hello " + self.name + "! \n")
        
    def goodbye(self):
        print("Good-bye " + self.name + "! \n") 
        
m = Man("Jack")               
m.hello()
m.goodbye()