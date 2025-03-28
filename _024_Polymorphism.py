class Animal:
    def speak(self):
        print("Finding my voice...")
        # raise NotImplementedError("Not yest implemented")
    
class Cat:
    def speak(self):
        print("meow")

class Dog:
    def speak(self):
        print("woof")

class Giraffe(Animal):
    pass

def Talk2Animal(obj:Animal):
    obj.speak()

a1:Animal = Cat()
a2:Animal = Dog()
a3:Animal = Giraffe()

Talk2Animal(a1)
Talk2Animal(a2)
Talk2Animal(a3)
