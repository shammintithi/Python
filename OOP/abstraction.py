class Car:
    def __init__(self):
        self.acc = False
        self.brk = False

    def start(self):
        self.acc = True
        print("Car is started")

#call obejct
car1 = Car()
car1.start()

#abstraction: hide the unnecessary implementation. 
