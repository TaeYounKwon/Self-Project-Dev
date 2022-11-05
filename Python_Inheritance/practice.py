from enum import Enum

class Rank(Enum):
    Professor = ("Professor","1",'P_0')
    Associated_Professor = ("Associated_Professor",'2','AP_1')
    Assistant_Professor = ("Assistant_Professor",'3','AP_2')
    
    def __init__(self, position, rank, code):
        self.position = position
        self.rank = rank
        self.code = code
        
    def __del__(self):
        print('Enum Removed')    
        
class Person():
    
    def __init__(self, name='John', birthday='DD/MM/YY'):
        self.name = name
        self.birthday = birthday
                    
    def PrintInfo(self):
        print('Personal Information below! ')
        print('Name: ', self.name)
        print('Birthday: ',self.birthday)            
    
    def GetName(self):
        return self.name 
    
    def GetBirthday(self):
        return self.birthday     
                
    def __del__(self):
        print('Person Class Removed')            
    
    
class Student(Person):
    def __init__(self, major, credits, gpa):
        self.major = major
        self.credits = credits
        self.gpa = gpa 
        
    def PrintStudentInfo(self):
        Person.PrintInfo(self)
        print('Major: ', self.major)
        print('Credits: ',self.credits)
        print('GPA: ',self.gpa)
    
    def GetGrade(self):
        return self.gpa 
    
    def GetGPA(self):
        return self.gpa
    
    def GetCredits(self):
        return self.credits
    
    def AddGrade(self,grade,credits):
        currentGPA = self.gpa
        
        numbCredit = self.credits
        
        calGPA = self.gpa * numbCredit + grade
        calCredits = numbCredit + credits
        finalGPA = calGPA/calCredits
        self.gpa = finalGPA
        self.credits = calCredits
        
        print('Grade Added')        
    
    def __del__(self):
        print('Student Class Removed')       
    
    


peter = Person('Peter',)
peter.PrintInfo()

tom = Student('Computer Science',18,3.5)
tom.name = 'Tom'
tom.birthday = '03/06/1999'
tom.PrintStudentInfo()