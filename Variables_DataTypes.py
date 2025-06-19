# -------------------------------
# ✅ 1. What is a Variable in Python?
# -------------------------------
# A variable is a name used to store data.
# Python is dynamically typed — you don’t need to declare the type.

x = 10              # integer variable
name = "Rohit"      # string variable
pi = 3.14           # float variable

print(x)
print(name)
print(pi)

# -------------------------------
# ✅ 2. Python Data Types
# -------------------------------
# ➤ int: Whole numbers
# ➤ float: Decimal numbers
# ➤ str: Text
# ➤ bool: True/False
# ➤ list: Ordered, mutable collection
# ➤ tuple: Ordered, immutable collection
# ➤ dict: Key-value pairs
# ➤ set: Unordered, unique elements

a = 100                   # int
b = 3.14                  # float
c = "Python"              # str
d = True                  # bool

my_list = [1, 2, 3]       # list
my_tuple = (4, 5, 6)      # tuple
my_dict = {"name": "Sam", "age": 25}  # dict
my_set = {1, 2, 2, 3}     # set (removes duplicates)

print(type(a))        # <class 'int'>
print(type(b))        # <class 'float'>
print(type(c))        # <class 'str'>
print(type(d))        # <class 'bool'>
print(type(my_list))  # <class 'list'>
print(type(my_tuple)) # <class 'tuple'>
print(type(my_dict))  # <class 'dict'>
print(type(my_set))   # <class 'set'>
print(my_set)         # Output: {1, 2, 3} — duplicate removed

# -------------------------------
# ✅ 3. Built-in Functions: type(), id(), input(), print()
# -------------------------------

# ➤ type(): tells the data type
value = 20
print(type(value))  # <class 'int'>

# ➤ id(): gives the memory location
print(id(value))

# ➤ input(): gets user input (string by default)
# ➤ print(): displays output

user_name = input("Enter your name: ")  # string input
print("Hello,", user_name)

# -------------------------------
# ✅ 4. Typecasting: Converting from one data type to another
# -------------------------------

# ➤ str(): Converts to string
num = 100
num_str = str(num)
print(num_str, type(num_str))  # Output: '100', <class 'str'>

# ➤ int(): Converts to integer
str_num = "50"
int_num = int(str_num)
print(int_num, type(int_num))  # Output: 50, <class 'int'>

# ➤ float(): Converts to float
val = "3.14"
float_val = float(val)
print(float_val, type(float_val))  # Output: 3.14, <class 'float'>

# ➤ Example: age calculator using input and typecasting
user_age = input("Enter your age: ")   # always a string
user_age = int(user_age)               # convert to int
print("Next year, you will be:", user_age + 1)

