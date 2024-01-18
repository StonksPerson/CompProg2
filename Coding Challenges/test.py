import random as rand

def func():
    print("wawa")

def funt():
    print("wewe")

funcs = {"1": func(), "2": funt()}

funcs[str(rand.randint(1,2))]