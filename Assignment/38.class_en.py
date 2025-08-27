class Maximum:
    def __init__(self, num1, num2):  # parameterized constructor.
        self.num1 = num1
        self.num2 = num2

    def show(self):
        if self.num1 > self.num2:
            print(self.num1)
        else:
            print(self.num2)


c1 = Maximum()
c1.show()