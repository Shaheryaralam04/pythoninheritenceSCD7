# SingleInheritanceExample.py

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create an instance of Dog
dog_instance = Dog()
dog_instance.speak()  # Accessing method from the base class
dog_instance.bark()   # Accessing method from the derived class