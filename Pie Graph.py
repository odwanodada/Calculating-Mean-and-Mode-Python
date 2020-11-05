import matplotlib.pyplot as plt

labels = 'girls','mans'
sizes = [8, 12]
colors = ['pink', 'blue']
explode = (0, 0) # to space the pie inside between girls and mans

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%2.0f%%', shadow=True, startangle=140)#Explode have been declare on top with Labels and size
plt.title("Pie Chart Graph for Girls & Mans")

plt.axis()
plt.show()