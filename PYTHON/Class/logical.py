bill = int(input("Enter bill amount: "))

if bill > 100 and bill <= 200:
    print("10% discount")
elif bill > 200 and bill <= 500:
    print("20% discount")
elif bill > 500:
    print("30% discount")
else:
    print("No discount")