class Mega:
    def __init__(self):
        self.input_string = ""
    
    def getString(self):
        self.input_string = input()

    def printString(self):
        print(self.input_string)

usage = Mega()
usage.getString()
usage.printString()


