import matplotlib.pyplot as plt
categories = ['Contractors', 'Agents', 'Employees']
values = [25, 36, 25]
plt.pie(values, labels=categories, autopct='%1.1f%%',
colors=['red', 'green', 'blue'])
plt.title("Type of People in Company")
plt.show()