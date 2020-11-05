import matplotlib.pyplot as plt
#line graph it plot a line
import numpy as np
xs = [1,2,3,4,5]
ys =[x**2 for x in xs]

plt.plot(xs, ys)
plt.show()

#Scatter Plot
x = [5,7,8,2,17,2,9,4,11,12,9,6]
y = [99,86,87,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()


#Scatter Plot using random numbers and colors
N=50

X=np.random.rand(N)
Y=np.random.rand(N)
colors =np.random.rand(N)

area = np.pi *(15*np.random.rand(N))**2 #O-15
plt.scatter(X,Y,s=area,c=colors,alpha=0.5)
plt.show()

#Box plot
West_A = [1.3, 3.4, 2.3, 9.8]
East_B = [3.5, 4.9, 1.3, 2.2]
South_C = [9.7, 1.5, 4.3, 0.9, 11.2]
data1 = [West_A,East_B,South_C]
plt.boxplot(data1)
plt.xlabel("Colleges")
plt.ylabel("Scores")
plt.title("Boxplot for colleges")
plt.show()