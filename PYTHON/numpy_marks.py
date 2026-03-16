import numpy as np

marks = [
    [85, 90, 78],
    [88, 76, 92],
    [90, 89, 84]
]

marks_array = np.array(marks)

average_marks = np.mean(marks_array)
max_marks = np.max(marks_array)
min_marks = np.min(marks_array)

print("Marks Dataset:")
print(marks_array)

print("Average Marks:", average_marks)
print("Maximum Marks:", max_marks)
print("Minimum Marks:", min_marks)