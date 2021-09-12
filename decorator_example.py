def percent(fun):
    def inner(*key,**keyargs):
      print('%'*30)
      fun(*key,**keyargs)
      print('%'*30)
    return inner  

@percent
def printer(msg,age):
    print(msg,age)
@percent
def gift(a,b,c,d):
    print(d,c,b,a)

gift(1,2,3,4)