import matplotlib.pyplot as plt


test_scores = [12,99,65,85,42]
test_names = ["Andy", "Martin", "Zahara", "Vuyo","Ziyaad" ]
test_graph = [x for x ,_ in enumerate(test_names)]
plt.bar(test_graph, test_scores, color="blue")#to display numbers on the Y or left side
plt.xticks(test_graph, test_names)
plt.title("Python Marks for 5 Students")
plt.xlabel("Test Names")#top or column
plt.ylabel("Test Scores")#left side or row
plt.show()