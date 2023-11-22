# HierarchicalInheritanceExample.py

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Create instances of Dog and Cat
dog_instance = Dog()
cat_instance = Cat()

dog_instance.speak()  # Accessing method from the base class
dog_instance.bark()   # Accessing method from the derived class

cat_instance.speak()  # Accessing method from the base class
cat_instance.meow()   # Accessing method from the derived class