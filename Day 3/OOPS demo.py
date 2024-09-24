class Calculator:
    num = 100

    def getData(self):
        print("Executed as method")

obj = Calculator()
obj.getData()
print(obj.num)