# __repr__ : Developer
# __str__  : End user client


class Emp(object):
    def __init__(self,first_name,last_name):
        self.last_name = last_name
        self.first_name = first_name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.first_name},{self.last_name})"


    def __str__(self):
        return self.first_name + " " + self.last_name

if __name__ == "__main__":
    e = Emp("amit","kanere")
    import pdb
    pdb.set_trace()
    print(e)