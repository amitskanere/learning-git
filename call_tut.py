class MyMath:
    def __init__(self,value):
        self.value = value


    def __call__(self,callvalue):
        return callvalue ** self.value

square = MyMath(2)
cube = MyMath(3)
rest_5 = MyMath(5)


print(rest_5(4))
