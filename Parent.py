class Bank:
    first_name=""
    last_name=""
    def __init__(self, fn, ln):
        self.first_name=fn
        self.last_name=ln

    def display(self):
        print("First Name: ", self.first_name)
        print("Last Name", self.last_name)
#b1 = Bank("John","Young")
#b1.display()