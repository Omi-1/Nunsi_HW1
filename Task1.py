class Numbs:

    def __init__(self,input1,input2,input3):
        self.input1 = input1
        self.input2 = input2
        self.input3 = input3

    def max_min_remaining(self):
        maximum= max(self.input1,self.input2,self.input3)
        minimum= min(self.input1,self.input2,self.input3)
        remaining= sum([self.input1,self.input2,self.input3]) - maximum - minimum

        print(maximum)
        print(minimum)
        print(remaining)

input1 = (float(input("Enter first number")))
input2 = (float(input("Enter second number")))
input3 = (float(input("Enter third number")))


Numbers= Numbs(input1,input2,input3)
Numbers.max_min_remaining()

