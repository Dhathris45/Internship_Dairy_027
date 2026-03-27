def sum_numbers(n):

    total = 0

    for i in range(1, n + 1):

        if i > 50:
            print("Loop stopped because number exceeded 50")
            break

        total += i

    return total


n = int(input("Enter a number: "))

result = sum_numbers(n)

print("Sum of numbers:", result)
