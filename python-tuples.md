# Python Tuples 

tags: data structures, python, tuples

## Tuples vs Lists

Tuples are similar to lists, except that they are immutable.
Both tuples and lists can be iterated over, but lists have more methods available to them.
Because of the reduced capability, tuples are faster than lists.
We can view the available methods of lists and tuples with ```dir```.


```python
#!/usr/bin/python3

# list example
nums = [1, 3, 5, 7, 9, 11]

# tuple example
chars = ('a', 'b', 'c', 'd')

# listing methods available

print("List Methods")
print(dir(nums))

print(80*"-")

print("Tuple Methods")
print(dir(chars))
```

Lists occupy more memory than tuples.
We can compare this in python using ```sys.getsizeof()```

```python
#!/usr/bin/python3

import sys

print(dir(sys))
# print(help(sys.getsizeof))

list_ex = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_ex = (1, 2, 3, "a", "b", "c", True, 3.14159)

print("\n")
print("List size = %d" % sys.getsizeof(list_ex))
print("Tuple size = %d" % sys.getsizeof(tuple_ex))
```

## Caveats

Creating a single element tuple 

```python
#!/usr/bin/python3

# this actually creates a string
single_tuple = ("a")
print(single_tuple)

# this is how to create a single-element tuple
real_single_tuple = ("a",)
print(real_single_tuple)

# tuple assignment

# (age, country, knows_python)

survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age = ", age)
print("Country = ", country)
print("Knows Python? ", knows_python)

# although the above is valid, tuples provide us with a faster method
survey2 = (21, "Switzerland", False)

# python can unpack the values and assign them for us
age, country, knows_python = survey2

print("Age = ", age)
print("Country = ", country)
print("Knows Python? ", knows_python)
```


Tuples can also be created without parenthesis

```python
#!/usr/bin/python3

# these are valid tuples

a = 1,
print(a)

b = 1, 2, 3
print(b)
```


Source: Socratica | youtube: Python Tuples|  https://www.youtube.com/watch?v=NI26dqhs2Rk
