[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 
````python
import thinkstats2
import thinkplot
import scipy.stats
df = ReadBrfss()
df_men = df[df.sex == 1]
cdf = thinkstats2.Cdf(df_men.htm3)
thinkplot.Cdf(cdf)
thinkplot.Show()
print ("% of men between 5'10 and 6'1:", 100*(scipy.stats.norm.cdf(185.42, loc = 178, scale = 7.7) - scipy.stats.norm.cdf(177.8, loc = 178, scale = 7.7)))
````
> Around 34% of men are between 5'10 and 6'1.
