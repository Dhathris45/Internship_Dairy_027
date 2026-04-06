x = 10
y = 0

try:
    z = x / y
    print(z)
except:
    print("Error occurred")
finally:
    print("This will always execute")

print("Rest of the program")