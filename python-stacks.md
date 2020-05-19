# Python Stacks

tags: data structures, python, stack

## What is a Stack?

A stack is a LIFO (last-in-first-out) list that contains elements. 
Elements can be pushed onto the stack or popped off of the stack.

```
#!/usr/bin/python3

"""
Stack Data Structure

    A B C D

       |
       v

       D
       C
       B
       A

Read D first, then C, then B, then A
"""

class Stack():
    """ Stack implementation using lists."""
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            # return last item in the list
            return self.items[-1]

s = Stack()
s.push("A")
s.push("B")
print(s.get_stack())
s.push("C")
print(s.get_stack())
print("calling pop()")
s.pop()
print(s.get_stack())

print("is stack empty?")

print(s.is_empty())

print("peeking at first element in stack")
print(s.peek())
```

source: Lucid Programming | youtube: Data Structures in Python: Stack |  https://www.youtube.com/watch?v=lVFnq4zbs-g
