print('Hello World!')

# tuples are IMMUTABLE - consists of group of values
# dog = ('Bruce', 'cocker spaniel', 19, False)
# print(dog[0])		# output: Bruce
# dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)


# lists are MUTABLE (can be updated/changed/modified)consists of group of values
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.insert(1,'Rose')
print(ninjas)	# output: ['Francis','Rose', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
print(type(ninjas))
print(len(ninjas))

ninjas_copy = ninjas[:] # makes a copy
ninjas_copy[0] = 'Helen' # you can modify a copy and it will not alter the original
print(ninjas_copy)
print(ninjas)


# Dictionaries - group of key-value pairs
# from email.errors import NoBoundaryInMultipartDefect


# empty_dict = {}
# new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}


# new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
# new_person['hobbies'] = ['climbing', 'coding']
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}


# w = new_person.pop('weight')	# removes the specified key and returns the value
# print(w)		# output: 160.2
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}


# items = new_person.items() # Returns a list containing a tuple for each key value pair
# print(items)
# # output: dict_items([('name', 'Jack'), ('age', 38), ('has_glasses', False), ('hobbies', ['climbing', 'coding'])])'


# age = new_person.get('age') # Returns the value of the specified key
# print(age)
# # output: 38


# keys = new_person.keys() # Returns a list containing the dictionary's keys
# print(keys)
# # output: dict_keys(['name', 'age', 'has_glasses', 'hobbies'])


# values = new_person.values() # 	Returns a list of all the values in the dictionary
# print(values)
# # output: dict_values(['Jack', 38, False, ['climbing', 'coding']])


# new_person.popitem() # Removes the last inserted key-value pair
# print(new_person)
# # output: {'name': 'Jack', 'age': 38, 'has_glasses': False}


# copy = new_person.copy() # returns copy of the dictionary
# print(new_person, copy)
# # output: {'name': 'Jack', 'age': 38, 'has_glasses': False}
# # {'name': 'Jack', 'age': 38, 'has_glasses': False}


# new_person.update({'profession': 'developer'}) # update()	Updates the dictionary with the specified key-value pairs
# print(new_person)
# # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'profession': 'developer'}


# new_person.clear() # removes all elements from the dictionary
# print(new_person)  
# # output: {} 


# Numbers
# # function type()     types of variable
# print(type(2.63))		# output: <class 'float'>
# print(type(new_person))		# output: <class 'dict'>

# # function len()      length of an attribute
# print(len(new_person))		# output: 4 (the number of key-value pairs)
# print(len('Coding Dojo'))	# output: 11 (including space)


# print(type(24))
# print(type(3.9))
# print(type(3j))
# # output: 
# # <class 'int'>
# # <class 'float'>
# # <class 'complex'>

# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))
# # output: 
# # 35.0
# # 44
# # (35+0j)
# # <class 'float'>
# # <class 'int'>
# # <class 'complex'>


# import random
# print(random.randint(2,5)) # provides a random number between 2 and 5
# print(random.randint(2,5))
# print(random.randint(2,5))
# print(random.randint(2,5))
# print(random.randint(2,5))
# # output: 4
# # 4
# # 3
# # 2
# # 5

# String concatenations
# name = "Zen"
# print("My name is", name)
# # output: 
# # My name is Zen

# name = "Zen"
# print("My name is" + name)
# # output: 
# # My name isZen


# name = "Zen"
# print("My name is " + name) # you need to add space inside quotes
# # output: 
# # My name is Zen


# Type cast/type conversion to str or int
# print("Hello" + 42)			# output: TypeError
# print("Hello" + str(42))		# output: Hello 42

# total = 35
# user_val = "26"
# total = total + user_val		# output: TypeError
# total = total + int(user_val)		# total will be 61


# # String interpolation with f-string
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")


# # String interpolation with string.format()
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# # output: My name is Zen Coder and I am 27 years old.
# print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# # output: My name is 27 Zen and I am Coder years old.


# Template string
from string import Template
name = 'world'
program ='python'
new = Template('Hello $name! This is $program.')
print(new.substitute(name = name, program = program))


# # %-formatting
# hw = "Hello %s" % "world" 	# with literal values
# py = "I love Python %d" % 3 
# print(hw, py)
# # output: Hello world I love Python 3
# name = "Zen"
# age = 27
# print("My name is %s and I'm %d" % (name, age))		# or with variables
# # output: My name is Zen and I'm 27


# # string methods
# x = "hello world"
# print(x.title()) # makes words capitalized as title
# # output: 
# # Hello World
# print(x)
# # output:
# # hello world


# other string methods
# string.upper(): returns a copy of the string with all the characters in uppercase.
# string.lower(): returns a copy of the string with all the characters in lowercase.
# string.count(substring): returns number of occurrences of substring in string.
# string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
# string.find(substring): returns the index of the start of the first occurrence of substring within string.
# string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
# string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
# string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.
