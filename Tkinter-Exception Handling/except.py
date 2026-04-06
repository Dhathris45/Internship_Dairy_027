x = 10
y = 0

try:
    z = x / y
    print(z)
except ZeroDivisionError:
    print("Division by zero error")
finally:
    print("Finally block executed")