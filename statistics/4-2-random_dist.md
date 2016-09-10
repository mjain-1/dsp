[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> 
````python
import pandas as pd
import random
import matplotlib.pyplot as plt
###creates dataframe with 1000 random numbers from 0 - 1
series = [random.random() for i in range(0, 1000)]
data = pd.DataFrame({"Numbers": series})
### finds pmf
x_pmf = []
y_pmf = []
for x in data.Numbers:
    x_pmf.append(x)
    y_pmf.append(len(data[data.Numbers == x])/len(data.Numbers))
### plots pmf
plt.bar(x_pmf, y_pmf, width = 0.001)
### finds cdf
x_cdf = []
y_cdf = []
for x in data.Numbers:
    count = 0
    x_cdf.append(x)
    for x_test in data.Numbers:
        if x_test <= x:
            count+=1
    y_cdf.append(count/len(data.Numbers))
### plots cdf 
plt.plot(x_cdf, y_cdf, 'bo', markersize = 4)
````
> Plotting the cdf shows that this distribution is uniform forming approximately an x=y line.
