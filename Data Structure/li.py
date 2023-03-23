class employeeee:
    name = " "
    dflt = " "
    def __int__(self,name):
        self.name = name
        self.dflt = 8
    def display(self):
        print(f"{self.name}")
    def read_dflt(self):
        print(f"{self.dflt}")

kar = employeeee ( 77)
kar.display()
