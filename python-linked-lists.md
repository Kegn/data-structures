# Python Linked Lists

tags: data structures, python, linked-lists

linked lists are a way to store data in an ordered manner

## Comparison to array

An array is a fixed address chunk in memory
the chunk is then subdivided that can be accesed via indicies.
The benefit is that we can access the indicies in constant time O(1)
We can access index 1 and index 100000 in the same time.
The reason for this is that we only calculate a single memory address, then tell the computer to pull the data from that location for any spot in the array.

The **Linked List** structure does not have a linear chunk or structure in memory.
Instead, the ordering is controlled by the data structure, which maintains the order of each element.
Rather than fixed length spaces in memory, the linked list uses *nodes* to wrap each one of its elements.
The node contains the pointer to the next element in the list.

## Efficieny of various operations

+----------------------------------+--------------------+--------------------+
|          Operation               | Singly-linked List | Doubly-linked List |
+----------------------------------+--------------------+--------------------+
|Access an element                 |        O(n)        |       O(n)         |
|Add/remove an iterator position   |        O(1)        |       O(1)         |
|Add/remove first element          |        O(1)        |       O(1)         |
|Add last element                  |        O(1)        |       O(1)         |
|Remove last element               |        O(n)        |       O(1)         |
+----------------------------------+--------------------+--------------------+

## Code: linked-list.py


```python
class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head = node() # not indexable, never contains data, used as placeholder
                           # to point to first index in the list
    
    def append(self, data):     # pass in the data point
        new_node = node(data)   # pass in data into class instantiation of node
        cur = self.head
        while cur.next != None:
            cur = cur.next      # traverse through list
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    # define helper function to display current contents of list
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)


    # extractor, pull out data point at index
    def get(self, index):
        # make sure index is not out of range
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        # iterate over the nodes until index is reached
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1

    # erase function
    def erase(self,index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        cur_index = 0
        cur_node = self.head
        # iterate over list until we get to the item to remove
        while True:
            # save current node because we need previous node 
            # to still point to next node after erasing
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index==index:
                last_node.next = cur_node.next
                return
            cur_index += 1

                

my_list = linked_list()

my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

# test get function
print("element at index 2: %d" % my_list.get(2))

my_list.erase(1)
my_list.display()

```


source: Brian Faure | youtube: Python Datastructures #2: Linked List | https://youtube.com/watch?v=JlMyYuY1aXU
