import seaborn as sns
import matplotlib.pyplot as plt
tips = {
    "total_bill": [16.99, 10.34, 21.01, 23.68, 24.59],
    "tip": [1.01, 1.66, 3.50, 3.31, 3.61],
    "sex": ["Female", "Male", "Male", "Male", "Female"],
    "smoker": ["No", "No", "No", "No", "No"],
    "day": ["Sun", "Sun", "Sun", "Sun", "Sun"],
    "time": ["Dinner", "Dinner", "Dinner", "Dinner", "Dinner"],
    "size": [2, 3, 3, 2, 4]
}
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()