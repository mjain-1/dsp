# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Both are sequences of values that can be of any type, e.g. string or float and that are indexed by numbers. This indexing also allows both to be sliced in order to return a range of elements. However, lists are mutable, meaning that an element can be changed, while tuples are not. Instead, you can replace an element in a tuple by creating a new one. Tuples work as keys in dictionaries because they are immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets are both sequences of values, however lists can contain duplicates and preserve order while sets cannot. Lists are best used when you need to iterate through contents, however sets are much faster for finding an element (e.g. checking to see whether someone is already a member, finding whether a word has already been used). The latter is true because sets are implemented using hashtables, so an object is found using its hash, rather than having to go through all of the contents as with a list. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is another way to build functions in addition to defining (def) one. It's best used in situations where the function is only going to be used once so it does not need to be named and/or does not disrupt the flow of code so it does not need to be separated out. It can only take in one expression. The below shows lambda being used to sort the members by age:     

members = [('John', 26, 2013), ('Mary', 23, 2015), ('Paul', 25, 2014)]    
sorted(members, key = lambda member: member[1])
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions more concisely create lists with one line of code, and therefore much faster than writing out a function. For example, the below creates a new list of the squares of each value in the original list.    

numbers = [2, 4, 5, 9]    
numbers_squared = [x**2 for x in numbers]     
    
This is the same as mapping those values as follows:    
    
numbers_squared = []

def square_numbers(numbers):
  for number in numbers:    
    numbers_squared.append(number**2)
  return numbers_squared
  
Below is a function that filters for even numbers only:   
even_num = []    
def find_even(numbers):    
  for number in numbers:
    if number % 2 == 0:    
      even_num.append(number)
  return even_num    
    
This is the same function using a list comprehension:    
even_num = [num for num in numbers if num % 2 == 0]    
    
Set and dictionary comprehensions use the same form except they are enclosed in {}. Example first for sets and then for dictionaries below.    
      
new_set = {s for s in 'MEGHA' if s not in 'ME'}    
new_set = {'G', 'H', 'A'}    
    
members = {'John': 2013, 'Mary': 2015, 'Paul': 2014}    
new_members = {name: year_joined for name, year_joined in members.items() if year_joined > 2014}    
new_members = {'Mary': 2015}

    
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





