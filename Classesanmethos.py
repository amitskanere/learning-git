class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1=Point()
point1.move()
point1.x=10
point1.y=20
point1.draw()
print(point1.x)

point2=Point()
print("\n")
point2.draw()
