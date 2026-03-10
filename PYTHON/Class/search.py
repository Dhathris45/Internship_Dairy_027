x = []

print("Enter 10 nos")

for i in range(10):
    x.append(int(input()))

sr = int(input("Which no do you want to search? "))

for n in x:
    if n == sr:
        print("Number found!!!")
        break
else:
    print("Oops! Number not found!")