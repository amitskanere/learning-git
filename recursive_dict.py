a={
    "k1":"v1",
    "k2":"v2",
    "k3":[[5,4,3,2,1],{"lk2":"lkv2"}],
    "k4":[1,2,3,4]
}

def printvalues(inputdl):
    if isinstance(inputdl,dict):
        for key,value in inputdl.items():
            printvalues(value)
        return
    if isinstance(inputdl,list):
        for each in inputdl:
            printvalues(each)
        return

    print(inputdl)

printvalues(a)

