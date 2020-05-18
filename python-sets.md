# Python Sets

tags: data structures, python, sets


## Sets vs Lists

Sets are like lists, but they remove all of the duplicate values.
There are also some useful methods that we can use with sets that we cannot with other datatypes.
We can use intersection to get the elements that are the same across sets.
We can use difference to get the elements that are in one list, but not others.
Sets, like lists, are *mutable*

```python

s1 = set([1, 2, 3, 4, 5])
print(s1)

# add value to set
s1.add(6)
print(s1)

# add multiple values to set
s1.update([7, 8, 9])
print(s1)

# empty set
empty_set = set()

# sets remove duplicate values
s2 = {10, 10, 10, 11, 12}
print(s2)

# add set to set
s1.update([13, 14, s2])
print(s1)

# remove value
s1.remove(5)
print(s1)

# removing a vlue that does not exist will throw KeyError
# discard will not
# discard non-existent value
s1.discard(100)
print(s1)
```

Useful set operations

```python
#!/usr/bin/python3

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

# get a set of values that exist in both s1 and s2
s4 = s1.intersection(s2)
print(s4)

# get a set of values that exist in all sets
s4 = s1.intersection(s2, s3)
print(s4)

# get the values that are in s1 that are not in s2
s4 = s1.difference(s2)
print(s4)

# get the values that are in s2 that are not in s1
s4 = s2.difference(s1)
print(s4)

# get the values that are in s2 but not in s1 or s3
s4 = s2.difference(s1, s3)
# there are none, so it s4 will be an empty set
print(s4)

# symmetric difference allows you to compare two sets
# it returns the values that are not in both lists
s4 = s1.symmetric_difference(s2)
print(s4)

```

Practical examples with lists
```python
#!/usr/bin/python

l1 = [1, 2, 3, 1, 2, 3]
print(l1)

# we want to get unique values from list
# we could vis the following:
#   - make a new list
#   - check if the value is in list
#   - if not, append it
# with sets this becomes much simpler

# cast list to a set, removing duplicates, then cast back to list
l2 = list(set(l1))
print(l2)



employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
gym_members = ['April', 'John', 'Corey']
developers = ['Judy', 'Corey', 'Steven', 'Steven', 'Jane', 'April']

# we want to gather info from these lists
# who has a gym membership and is a developer?
# we can pass a list into intersection without casting to a set
result = set(sym_members).intersection(developers)
print(result)

# get all employees who are neither gym members or developers
result = set(employees).difference(gym_members, developers)
print(result)
```

## Complexity of sets and lists

Membership tests are faster in sets.
A membership test on a list is O(n)
A membership test on a set is O(1)

The reason a list is O(n) for membership tests is because we have to traverse the whole list to test.
The reason a set is O(1) is because it is built on a hash table implementation where there are no 'keys', just values and index lookup on hash-tables is contant time.

source: Corey Schafer | youtube: Python Tutorial: Sets = Set Methods and Operations to Solve Common Problems |  https://www.youtube.com/watch?v=r3R3h5ly_8g
