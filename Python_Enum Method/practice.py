from enum import Enum

class Rank(Enum):
    Professor = ("Professor","1",'P_0')
    Associated_Professor = ("Associated_Professor",'2','AP_1')
    Assistant_Professor = ("Assistant_Professor",'3','AP_2')
    
    def __init__(self, position, rank, code):
        self.position = position
        self.rank = rank
        self.code = code
    
print(Rank.Professor.value)        
print(Rank.Professor.position)