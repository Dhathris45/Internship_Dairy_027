class MyError(Exception):
    pass

temp = int(input("Enter temperature: "))

try:
    if temp > 400:
        raise MyError
    else:
        print("Temperature is normal")
except MyError:
    print("Temperature too high!")
finally:
    print("Program ended")