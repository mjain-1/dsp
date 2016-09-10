[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> 
````python
import chap01soln
import matplotlib.pyplot as plt
resp = chap01soln.ReadFemResp()
### calculates actual pmf
x_val= []
y_val= []
n=0
for x in resp.numkdhh.value_counts():
    x_val.append(n)
    y_val.append(x/len(resp.numkdhh))
    n+=1
### calculates biased pmf
n = 0
y_val_biased = []
total = 0
for y in y_val:
    y_biased = y*x_val[n]
    y_val_biased.append(y_biased)
    n += 1
    total += y_biased
y_val_norm = []
for y in y_val_biased:
    y_norm= y*(1/total)
    y_val_norm.append(y_norm)
biased_mean = 0
for x, y in zip(x_val, y_val_norm):
    biased_mean += x*y
### plots actual and biased pmf
fig, axes = plt.subplots(1)
axes.plot(x_val, y_val, drawstyle = 'steps-mid', label = 'actual')
axes.plot(x_val, y_val_norm, drawstyle = 'steps-mid', label = 'observed')
axes.legend()
### prints output
print ("Actual Mean", resp.numkdhh.mean())
print ("Observed Mean", biased_mean)
print (fig)
````
