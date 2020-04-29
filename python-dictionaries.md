# Python Dictionaries 

tags: data structures, python, dictionaries

## What is a Dictionary?

A dictionary is basically a mapping from a string or integer to a value or an object.
This is known as a key-value pair.
The key maps directly to the value, but not the other way around.
Dictionary has no ordering.

## Dictionaries vs Lists

In a list, an index is provided and an object is returned. 
An array, or list is a solid chunk in memory.
A dictionary on the otherhand is a hashmap, or a function.
It takes an input to find where to get the output.


## Code

```python

#!/usr/bin/python3

d = {}

d[1] = "yes"
d["1"] = "no"


# python treats integer keys and string keys differently
d[1]
d["1"]

d[2] = 9000
d[2]


# dictionaries can have keys that point to objects, such as classes

class my_class:
    def __init__(self):
        self.data = "data"

instance = my_class()

d['object'] = instance
d['object']


# to iterate over the fictionary, use keys() or items()
d.keys()
d.items()   # list of tuples, where each tuple is a key-value pair


print(d)
```


## Comparing time of Lists and Dictionaries

```python

class_names = [ "jack","bob","mary","jeff","ann","pierre","martha","clause","pablo","susan","gustav"]

def create_dataset():
    import random
    num_entries = 5000000
    f = open("data.txt","w")
    for i in range(num_entries):
        current = random.choice(class_names)
        f.write(current+"\n")
    f.close()

def read_dataset_list():
    class_counts = []
    for c in class_names:
        class_counts.append(0)
    with open("data.txt","r") as f:
        for line in f:
            line = line.strip()
            if line !="":
                class_counts[class_names.index(line)] += 1
    print(class_counts)

def read_dataset_dict():
    class_counts = {}
    for c in class_names:
        class_counts[c] = 0
    with open("data.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                class_counts[line] += 1
        print(class_counts)

import time

t0 = time.time()
create_dataset()
t1 = time.time()
print("Dataset creation took %0.1f seconds \n" % (t1-t0))

t0 = time.time()
read_dataset_list()
t1 = time.time()
print("List took %0.1f seconds \n" % (t1-t0))

t0 = time.time()
read_dataset_dict()
t1 = time.time()
print("Dictionary took %0.1f seconds \n" % (t1-t0))

```



source: Brian Faure | youtube: Python Data Structures #1: Dictionary Object|  https://www.youtube.com/watch?v=TW_e9FFEDeY
