import  numpy #import for mean and median
from scipy import stats#import is for mode

#Calculating Mean
test_scores = [12,99,86,88,45,87,94,78,77,85,86]
my_mean = numpy.mean(test_scores)
print("the mean is: ", round(my_mean))


#Calculating Median
test_scores = [12,99,86,88,45,87,94,78,77,85,86]
my_median =  numpy.median(test_scores)
print("the median is: ", my_median)


#Calculating Mode
test_scores = [12,99,86,88,45,87,94,78,77,85,86]
my_mode = stats.mode(test_scores)
print("the mode is: ", my_mode)

#Calculating Range
test_scores = [12,99,86,88,45,87,94,78,77,85,86]
my_range = numpy.ptp(test_scores)
print("the range is: ", my_range)

#Inter Quartile Range
test_scores = [12,99,86,88,45,87,94,78,77,85,86]
my_inter = numpy.percentile(test_scores, 50)#you change the 75% to 25% and 50%
x = numpy.percentile(test_scores, 75)
y = numpy.percentile(test_scores, 25)
print("50% percentile for the marks is: ", my_inter)
print("75% percentile for the marks is: ", x)
print("25% percentile for the marks is: ", y)

#Calculating Variance
test_scores = [12,99,86,88,45,87,94,78,77,85,86]
n = numpy.var(test_scores)
print("the variance of the marks is: ", n)


#Calculating standard deviation
test_scores = [12,99,86,88,45,87,94,78,77,85,86]
x = numpy.std(test_scores)
print("the standard deviation marks is: ", x)

