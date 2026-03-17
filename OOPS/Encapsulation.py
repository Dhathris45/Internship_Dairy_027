class Account:
    acc_name = "Sunil"
    __deposit = 90000
    loan = 50000
    __password = "123"

    def get_deposit(self):
        pwd = input("Enter password: ")

        if pwd == self.__password:
            print("Deposit amount:", self.__deposit)
        else:
            print("Access denied")


obj = Account()

obj.get_deposit()