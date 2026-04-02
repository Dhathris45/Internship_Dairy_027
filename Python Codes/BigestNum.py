def biggest(nums):
    global t
    t = 0

    for x in nums:
        if x > t:
            t = x

numbers = [45, 12, 76, 78, 11]

biggest(numbers)

print("Biggest number:", t)