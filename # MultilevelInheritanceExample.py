# MultilevelInheritanceExample.py

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class GoldenRetriever(Dog):
    def fetch(self):
        print("Golden Retriever fetches")

# Create an instance of GoldenRetriever
golden_retriever_instance = GoldenRetriever()
golden_retriever_instance.speak()  # Accessing method from the base class
golden_retriever_instance.bark()   # Accessing method from the intermediate class
golden_retriever_instance.fetch()  # Accessing method from the derived class