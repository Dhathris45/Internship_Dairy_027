f = open("data.txt", "r")

data = f.readlines()

for i in data:
    print(i)

f.close()