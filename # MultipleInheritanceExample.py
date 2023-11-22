# MultipleInheritanceExample.py

class Animal:
    def speak(self):
        print("Animal speaks")

class Pet:
    def play(self):
        print("Pet plays")

class Dog(Animal, Pet):
    def bark(self):
        print("Dog barks")

# Create an instance of Dog
dog_instance = Dog()
dog_instance.speak()  # Accessing method from the first base class
dog_instance.play()   # Accessing method from the second base class
dog_instance.bark()   # Accessing method from the derived class