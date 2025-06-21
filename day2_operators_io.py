# -----------------------------------------
# 📘 1. Arithmetic Operators in Python
# -----------------------------------------

a = 10
b = 3

print("Addition:", a + b)        # ➕ 10 + 3 = 13
print("Subtraction:", a - b)     # ➖ 10 - 3 = 7
print("Multiplication:", a * b)  # ✖️ 10 * 3 = 30
print("Division:", a / b)        # ➗ 10 / 3 = 3.333 (float result)
print("Floor Division:", a // b) # ⬇️ 10 // 3 = 3 (integer result)
print("Modulus:", a % b)         # 🔁 10 % 3 = 1 (remainder)
print("Exponent:", a ** b)       # ⬆️ 10 ** 3 = 1000 (10^3)

# -----------------------------------------
# 📘 2. Assignment Operators
# -----------------------------------------

x = 5        # assigns 5 to x
x += 3       # x = x + 3 → 8
x -= 2       # x = x - 2 → 6
x *= 2       # x = x * 2 → 12
x /= 3       # x = x / 3 → 4.0
x //= 2      # x = x // 2 → 2.0
x %= 2       # x = x % 2 → 0.0
x **= 3      # x = x ** 3 → 0.0

print("Final value of x:", x)

# -----------------------------------------
# 📘 3. Comparison Operators
# -----------------------------------------

a = 10
b = 5

print("Equal:", a == b)          # ❌ False
print("Not Equal:", a != b)      # ✅ True
print("Greater than:", a > b)    # ✅ True
print("Less than:", a < b)       # ❌ False
print("Greater or Equal:", a >= b) # ✅ True
print("Less or Equal:", a <= b)   # ❌ False

# -----------------------------------------
# 📘 4. Logical Operators
# -----------------------------------------

x = True
y = False

print("AND:", x and y)       # False (both must be True)
print("OR:", x or y)         # True (any one is True)
print("NOT x:", not x)       # False (opposite of x)

# Combine conditions
a = 10
b = 5
print("Multiple conditions:", (a > 5 and b < 10))  # ✅ True

# -----------------------------------------
# 📘 5. Input from User
# -----------------------------------------

# Accept string input
name = input("Enter your name: ")    # e.g., Rohit

# Accept number input
age = int(input("Enter your age: ")) # e.g., 25 → converted to int
height = float(input("Enter height in cm: "))  # e.g., 168.5 → float

print("Name:", name)
print("Age:", age)
print("Height:", height)

# -----------------------------------------
# 📘 6. Print Formatting Techniques
# -----------------------------------------

# Method 1: f-strings (recommended)
print(f"Hello {name}, you are {age} years old and {height} cm tall.")

# Method 2: .format()
print("Hello {}, you are {} years old and {} cm tall.".format(name, age, height))

# Method 3: % formatting (older style – not recommended)
print("Hello %s, you are %d years old and %.1f cm tall." % (name, age, height))
