#### NOT FOR SNAKE GAME JUST INHERITANCE EXAMPLE CODE:->>

class Animal:               #Parent class
    def __init__(self):
        self.num_eyes=2

    def breathe(self):
        print("Inhale!!Exhale!!")

class Fish(Animal):         #using parent class in child class
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()       #adding some of its own function in super class or child class
        print("Under Water!!!!")

    def swim(self):             #its own methods..
        print("Moving in Water!")

nemo=Fish()
print(nemo.num_eyes)
nemo.breathe()