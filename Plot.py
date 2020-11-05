import matplotlib.pyplot as plt
#line graph it plot a line
xs = [1,2,3,4,5]
ys =[x**2 for x in xs]

plt.plot(xs, ys)
plt.show()