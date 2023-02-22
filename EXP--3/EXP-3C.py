class Student:  
    def __init__(self, name, id, age): 
        self.name = name  
        self.id = id  
        self.age = age  
s = Student("John", 101, 22) 
print(getattr(s, 'name'))   
setattr(s, "age", 23)    
print(getattr(s, 'age'))   
print(hasattr(s, 'id'))  
delattr(s, 'age') 
