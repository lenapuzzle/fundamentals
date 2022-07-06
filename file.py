# - Data Types
# - Primitive
num1 = 42 # - variable declaration  - Numbers
num2 = 2.3 # - variable declaration  - Numbers
boolean = True # - variable declaration  - Boolean
string = 'Hello World' # - variable declaration  - Strings

# - Data Types - Composite
#  - List
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 
# - initialize

#  - Dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# - Tuples
fruit = ('blueberry', 'strawberry', 'banana')
#  - initialize

print(type(fruit)) # -log statement
print(pizza_toppings[1]) # - log statement

# - Composite - List
pizza_toppings.append('Mushrooms') # - add value

#  - Dictionary
print(person['name']) # - log statement
person['name'] = 'George' #  - change value
person['eye_color'] = 'blue' # - add value
print(fruit[2]) # - log statement


# - conditional
if num1 > 45: # - if
    print("It's greater") # - log
else: # - else
    print("It's lower") # - log

if len(string) < 5: # - if
    print("It's a short word!") # - log
elif len(string) > 15: # - else if
    print("It's a long word!") # - log
else: # - else
    print("Just right!") # - log

# - for loop
for x in range(5): # - start
    print(x) # - log
for x in range(2,5): # - start, end, sequence
    print(x) # - log
for x in range(2,10,3):  # - start, end, increment, sequence
    print(x) # - log

# - while loop
x = 0 # - start
while(x < 5): # - stop
    print(x) # - log
    x += 1 # - increment

pizza_toppings.pop() # - List  - delete value
pizza_toppings.pop(1) # - List  - delete value 

# - Dictionary
print(person) # - log statement
person.pop('eye_color') # - delete value
print(person) # - log statement

# - List 
# - for loop
for topping in pizza_toppings:
# - conditional
# - if
    if topping == 'Pepperoni':
        continue # - continue
    print('After 1st if statement') # - log statement

    if topping == 'Olives': # - conditional - if
        break

# - function
def print_hello_ten_times():
# - conditional - for loop
    for num in range(10):
        print('Hello') # - log

print_hello_ten_times() # - invoke function

def print_hello_x_times(x): # - parameter (x)
    # - for loop
    for num in range(x):
        print('Hello') # - log

print_hello_x_times(4) # - invoke function - argument (4)

def print_hello_x_or_ten_times(x = 10):  # - parameter (x = 10)
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() # - invoke function
print_hello_x_or_ten_times(4)  # - invoke function


# - comment  - multiline
"""
Bonus section
"""


print(num3) # - NameError: name <variable name> is not defined
num3 = 72 

fruit[0] = 'cranberry' # - TypeError: 'tuple' object does not support item assignment

print(person['favorite_team']) # - KeyError: 'favorite_team'

print(pizza_toppings[7]) # - IndexError: list index out of range 

print(boolean) # - IndentationError: unexpected indent

fruit.append('raspberry') # - AttributeError: 'tuple' object has no attribute 'append'

fruit.pop(1) # - AttributeError: 'tuple' object has no attribute 'pop'