class Cake:
    name = ""
    shape = ""
    flavour = ""
    cost = 0

    def acceptData(self):
        self.name = input("Enter cake name: ")
        self.shape = input("Enter cake shape: ")
        self.flavour = input("Enter cake flavour: ")
        self.cost = int(input("Enter cake cost: "))

    def showData(self):
        print("Cake name:", self.name)
        print("Cake shape:", self.shape)
        print("Cake flavour:", self.flavour)
        print("Cake cost:", self.cost)


c1 = Cake()
c1.acceptData()
c1.showData()

c2 = Cake()
c2.acceptData()
c2.showData()