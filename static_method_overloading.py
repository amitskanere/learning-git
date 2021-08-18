class Demo:
    def add(self,v1,v2):
        result = self.sum(v1,v2)
        return result

    @staticmethod
    def sum(v1,v2):
        return v1 + v2

class Demo2(Demo):

    @staticmethod
    def sum(v1,v2):
        print("***********************")
        return v1 + v2

    def add(self,v1,v2):
        print("I am adding ",v2,v1)
        return super().add(v1,v2)

class Demo3(Demo):

    @staticmethod
    def sum(v1,v2):
        print(""
              "-------------------------")
        return v1 + v2


d = Demo()
print(d.add(4,4))

d2 = Demo2()
print(d2.add(4,4))

d3 = Demo3()
print(d3.add(4,4))