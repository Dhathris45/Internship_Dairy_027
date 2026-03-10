candidates = ["Anil", "Kiran", "Manish", "Reena"]

print("Original List:", candidates)

pos = candidates.index("Reena")

candidates.insert(pos, "Mohan")

print("After inserting Mohan:", candidates)