class Mammal():
    def walk(self):
        print("walks")


class Dog(Mammal):
    def barks(self):
        print("dog barks")


class Cat(Mammal):
    def cat_loves(self):
        print("cat loves")

dog = Dog()
dog.walk()
dog.barks()
cat=Cat()
cat.walk()
cat.cat_loves()
