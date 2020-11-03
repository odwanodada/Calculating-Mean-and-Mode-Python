import matplotlib.pyplot as plt

girls_ages = [19,24,19,17]
girls_names = ["Skylar","Nadine","Zoe","lelethu"]
x_pos = [i for i, _ in enumerate (girls_names)]
plt.bar(x_pos, girls_ages, color="blue")
plt.xticks(x_pos, girls_names)
plt.xlabel("Names of Girls")#top or column
plt.ylabel("Ages of girls")#left side or row
plt.title("Names&Ages")
plt.show()
