class Emp:
    name = ""
    empid = ""
    salary = ""

    def accept_data(self):
        self.name = input("Enter employee name: ")
        self.empid = input("Enter employee id: ")
        self.salary = input("Enter salary: ")

    def show_data(self):
        print("Employee name:", self.name)
        print("Employee id:", self.empid)
        print("Salary:", self.salary)


class perm_emp(Emp):
    mgrid = ""
    deptid = ""

    def accept_data(self):
        Emp.accept_data(self)
        self.mgrid = input("Enter mgr id: ")
        self.deptid = input("Enter dept id: ")

    def show_data(self):
        Emp.show_data(self)
        print("Mgr id:", self.mgrid)
        print("Dept id:", self.deptid)


# create object of the perm emp
employee1 = perm_emp()

employee1.accept_data()
employee1.show_data()