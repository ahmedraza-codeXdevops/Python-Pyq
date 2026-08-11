class Animals:
    def sound(self):
        print("Animals make different sounds")

class Dog(Animals):
    def sound(self):
        print("Dog barks")

class Cat(Animals):
    def sound(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()