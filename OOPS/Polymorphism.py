class Factory:
    def production(self):
        print("Production capacity is 20000")

    def packing(self):
        print("Packing using plastic")


class UnitA(Factory):
    def production(self):
        print("Production capacity is 50000")


class UnitB(Factory):
    pass


ua = UnitA()
ub = UnitB()

ua.production()
ub.production()
ub.packing()