# Python Classes

tags: data structures, python, class

# Classes
It is recommended to Uppercase the first letter of your classnames.

```python
#!/usr/bin/python

class User:
    pass

# create an instance of User 
user1 = User()

# give user a name
# this data attached to an object is called a field
# do not capitalize field names, seperate words by underscores (PEP 8 style Guide)
user1.first_name = "Dave"
user1.last_name = "Bowman"

print(user1.first_name)
print(user1.last_name)

# create another instance
user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"

user1.age = 37
user2.favorite_book = "2001: A Space Odyssey"
```

Adding more information to a class

```python
#!/usr/bin/python3

import datetime

class User:
    """ A member of FriendFace. For now we are
        only storing their name and birthday.
        But soon we will store an uncomfortable
        amount of user information."""
    
    # ^ add Docstring ^

    # add a 'constructor'. In python, this is known as init or initialization
    # this method is called every time you create a new instance of a class
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday  #yyyymmdd

        # extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        # l name not attached to self. This means it goes away at the end of the method.
        l_name = name_pieces[-1]
        self.last_name = name_pieces[-1]


    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) # date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365 # ignoring leap years
        return int(age_in_years)


# create an instance
user = User("Dave Bowman", "19710315")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)
print(user.age())

# calling help on the class will display Doctring and methods
help(User)
```

Source: Python Classes and Objects || Python Tutorial https://www.youtube.com/apACNr7DC_s
