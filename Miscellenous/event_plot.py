import matplotlib.pyplot as plt
sports = [1, 3, 5, 7, 9]
cultural = [2, 4, 6, 8, 10]
plt.eventplot([sports, cultural], colors=['green',
'blue'])
plt.title("College Events Timeline")
plt.show()