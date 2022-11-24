class Dog:
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed
        
        
    def dog_breed(self):
        
        print("Dog's breeding type is  " + self.breed + "\n")
    
    def dog_name (self):
        print("Dog name is "+ self.name + "\n")
    
    def get_dog_breed(self):
        return self.breed

    def get_dog_name(self):
        return self.name        
    
class Cat:
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed
        
        
    def cat_breed(self):
        
        print("Cat's breeding type is  " + self.breed + "\n")
    
    def cat_name (self):
        print("Cat name is "+ self.name + "\n")
    
    def get_cat_breed(self):
        return self.breed

    def get_cat_name(self):
        return self.name          
    
        
doggy = Dog('Cookie','Bichon Frise')
doggy.dog_breed()
doggy.dog_name()
dogType = doggy.get_dog_breed()
print(dogType)
dogName = doggy.get_dog_name()
print(dogName)

kitty = Cat('marshie','British Short Hair')


tom = Cat('Tom', 'Korean Short Hair')

kitty.cat_name()
kitty.cat_breed()
tom.cat_name()
tom.cat_breed()
