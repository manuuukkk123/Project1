class Calculator():
    num = 100  # class variables

    def __init__(self, a,b):
        self.firstnumber = a
        self.secondnumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num


obj = Calculator(2, 3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Summation())
