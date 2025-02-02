class Student:  
    

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    @staticmethod
    def university():
        print("University")

    #def function(self): -> Methods
    def welcome(self):
        print("Welcome", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("tithi", 80)
s1.welcome()
print(s1.get_marks())

s2 = Student("shammin", 90)
s2.welcome()