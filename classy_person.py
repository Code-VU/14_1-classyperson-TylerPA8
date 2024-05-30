class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        
    def increase_age(self):
        self.age += 1

    def say_greeting(self):
        print(f"Hello world! My name is {self.name}!")
    
    def count_to_age(self):
        x = 1
        while x <= self.age:
            print (x)
            x += 1

# You won't need to call anything here.