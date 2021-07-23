class Point:
    def __init__(point_obj,x,y):
        point_obj.x=x
        point_obj.y=y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1=Point(10,20)
print(point1.__dict__)
print(Point.__dict__)
print(point1.x)
print(point1.y)


#example 1 of constructor

class Person():
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"Hi, this is {self.name}")

person1=Person("Amit kanere")
person1.talk()
person2=Person("Chetan kolhe")
person2.talk()


#example 2 of constructor
class Emp:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return self.first_name + self.last_name

a = Emp("Amit","kanere")
b = Emp("Chetan","kolhe")

print(a.get_full_name())
print(Emp.get_full_name(a))
print(b.get_full_name())





