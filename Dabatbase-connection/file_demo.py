f = open("data.txt", "w")

name = input("Enter your name: ")
f.write(name)

subject = input("Enter your subject: ")
f.write("\n" + subject)

f.close()