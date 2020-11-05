import matplotlib.pyplot as plt

labels = 'girls','mans'
sizes = [8, 12]
colors = ['pink', 'blue']
explode = (0.1, 0) # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Pie Chart Graph for Girls & Mans")

plt.axis('equal')
plt.show()