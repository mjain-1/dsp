[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>
```python
def CohenD(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1*var1 + n2*var2)/(n1+n2)
    d = diff/math.sqrt(pooled_var)
    return var1, var2, n1, n2, pooled_var, d

df = nsfg.ReadFemPreg()

firsts = df[df.birthord == 1]
others = df[df.birthord > 1]

print (firsts['totalwgt_lb'].mean())

print (others['totalwgt_lb'].mean())

firsts['totalwgt_lb'].hist()

others['totalwgt_lb'].hist()

print (CohenD(firsts['totalwgt_lb'], others['totalwgt_lb']))
```

First-born babies have an average weight of 7.2 pounds, while the others have an average weight of 7.3 pounds. Graphing the distributions for each, the mode is around 7 pounds for first-borns and 8 pounds for others with the others distribution being slightly more left-skewed. Cohen's d is -0.08867. This is a greater magnitude of change compared to the length of pregnancy but is still a small effect size. However, it is also negative suggesting that first borns may be lighter than other babies, whereas the effect size was positive for length of pregnancy suggesting pregnancies may be longer for first borns. 
