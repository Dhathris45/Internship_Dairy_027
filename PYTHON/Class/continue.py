for i in range(5):
    num = int(input("Enter positive number: "))

    if num < 0:
        print("Negative number entered. Try again.")
        continue

    print("Cube of number:", num * num * num)